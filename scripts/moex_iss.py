#!/usr/bin/env python3
"""Small stdlib-only CLI for the Moscow Exchange ISS API.

Designed for Codex/agent workflows: deterministic URL construction, metadata
probing, table decoding, bounded retries, generic cursor/start pagination and
optional HTTP Basic auth via environment variables.

Environment variables:
  MOEX_ISS_BASIC_USER
  MOEX_ISS_BASIC_PASSWORD

Do not put credentials on the command line.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

BASE_URL = "https://iss.moex.com"
RETRYABLE = {500, 501, 502, 503, 504}
DEFAULT_TIMEOUT = 30.0
USER_AGENT = "codex-skill-moex-iss-api/1.0"


def parse_kv(items: Optional[Sequence[str]]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for item in items or []:
        if "=" not in item:
            raise ValueError(f"Expected KEY=VALUE, got: {item!r}")
        key, value = item.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"Empty parameter name in: {item!r}")
        out[key] = value
    return out


def build_url(path_or_url: str, params: Optional[Mapping[str, Any]] = None) -> str:
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        base = path_or_url
    else:
        path = path_or_url if path_or_url.startswith("/") else "/" + path_or_url
        base = BASE_URL + path

    parts = urllib.parse.urlsplit(base)
    existing = dict(urllib.parse.parse_qsl(parts.query, keep_blank_values=True))
    for key, value in (params or {}).items():
        if value is None:
            continue
        existing[str(key)] = str(value)
    query = urllib.parse.urlencode(existing, doseq=False, safe=",")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


def auth_header() -> Optional[str]:
    user = os.getenv("MOEX_ISS_BASIC_USER")
    password = os.getenv("MOEX_ISS_BASIC_PASSWORD")
    if not user and not password:
        return None
    if not user or password is None:
        raise RuntimeError("Set both MOEX_ISS_BASIC_USER and MOEX_ISS_BASIC_PASSWORD")
    token = base64.b64encode(f"{user}:{password}".encode("utf-8")).decode("ascii")
    return f"Basic {token}"


def request_json(
    path_or_url: str,
    params: Optional[Mapping[str, Any]] = None,
    *,
    timeout: float = DEFAULT_TIMEOUT,
    retries: int = 4,
) -> Tuple[Dict[str, Any], Mapping[str, str], str]:
    url = build_url(path_or_url, params)
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    auth = auth_header()
    if auth:
        headers["Authorization"] = auth

    last_error: Optional[BaseException] = None
    for attempt in range(max(1, retries)):
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                charset = resp.headers.get_content_charset() or "utf-8"
                payload = json.loads(raw.decode(charset))
                return payload, dict(resp.headers.items()), resp.geturl()
        except urllib.error.HTTPError as exc:
            last_error = exc
            body = exc.read().decode("utf-8", "replace")
            if exc.code not in RETRYABLE or attempt + 1 >= retries:
                marker = exc.headers.get("X-MicexPassport-Marker") if exc.headers else None
                extra = f"; X-MicexPassport-Marker={marker}" if marker else ""
                raise RuntimeError(f"HTTP {exc.code} for {url}{extra}: {body[:500]}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt + 1 >= retries:
                raise RuntimeError(f"Network error for {url}: {exc}") from exc

        time.sleep(min(8.0, 0.5 * (2 ** attempt)))

    raise RuntimeError(f"Request failed for {url}: {last_error}")


def table_rows(block: Any) -> List[Dict[str, Any]]:
    """Decode a normal ISS JSON table block into list[dict]."""
    if not isinstance(block, Mapping):
        return []
    columns = block.get("columns")
    data = block.get("data")
    if not isinstance(columns, list) or not isinstance(data, list):
        return []
    return [dict(zip(columns, row)) for row in data if isinstance(row, list)]


def block_names(payload: Mapping[str, Any]) -> List[str]:
    return [key for key, value in payload.items() if isinstance(value, Mapping)]


def print_json(obj: Any) -> None:
    json.dump(obj, sys.stdout, ensure_ascii=False, indent=2, sort_keys=False)
    sys.stdout.write("\n")


def add_common_request_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--param", action="append", default=[], metavar="KEY=VALUE", help="ISS query parameter; repeatable")
    parser.add_argument("--only", help="Convenience for iss.only=block1,block2")
    parser.add_argument("--columns", action="append", default=[], metavar="BLOCK=A,B", help="Convenience for BLOCK.columns=A,B; repeatable")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    parser.add_argument("--retries", type=int, default=4)


def request_params(args: argparse.Namespace) -> Dict[str, str]:
    params = parse_kv(args.param)
    if getattr(args, "only", None):
        params["iss.only"] = args.only
    for spec in getattr(args, "columns", []) or []:
        if "=" not in spec:
            raise ValueError(f"Expected BLOCK=A,B for --columns, got {spec!r}")
        block, cols = spec.split("=", 1)
        params[f"{block}.columns"] = cols
    return params


def cmd_index(args: argparse.Namespace) -> int:
    params = request_params(args)
    if not args.only:
        params.setdefault("iss.only", "engines,markets,boards,boardgroups,securitytypes,securitygroups,securitycollections")
    payload, headers, url = request_json("/iss/index.json", params, timeout=args.timeout, retries=args.retries)
    if args.raw:
        print_json({"url": url, "headers": selected_headers(headers), "response": payload})
        return 0
    decoded = {name: table_rows(block) for name, block in payload.items() if isinstance(block, Mapping)}
    print_json({"url": url, "blocks": decoded})
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    params: Dict[str, str] = {"q": args.query, "iss.meta": "off"}
    if args.limit is not None:
        params["limit"] = str(args.limit)
    if args.engine:
        params["engine"] = args.engine
    if args.market:
        params["market"] = args.market
    payload, _headers, url = request_json("/iss/securities.json", params, timeout=args.timeout, retries=args.retries)
    print_json({"url": url, "securities": table_rows(payload.get("securities"))})
    return 0


def cmd_get(args: argparse.Namespace) -> int:
    params = request_params(args)
    payload, headers, url = request_json(args.path, params, timeout=args.timeout, retries=args.retries)
    if args.raw:
        print_json({"url": url, "headers": selected_headers(headers), "response": payload})
        return 0
    decoded = {name: table_rows(block) for name, block in payload.items() if isinstance(block, Mapping)}
    print_json({"url": url, "blocks": decoded})
    return 0


def selected_headers(headers: Mapping[str, str]) -> Dict[str, str]:
    wanted = {
        "Content-Type",
        "X-MicexPassport-Marker",
        "X-Micex-ISS-Query-Version",
        "X-Micex-ISS-Statement-Version",
    }
    return {k: v for k, v in headers.items() if k in wanted}


def cmd_probe(args: argparse.Namespace) -> int:
    params = request_params(args)
    params.setdefault("iss.meta", "on")
    # Do not force iss.data=off: some underdocumented routes expose useful columns
    # more reliably with a tiny data response. The caller can still pass it.
    payload, headers, url = request_json(args.path, params, timeout=args.timeout, retries=args.retries)
    summary: Dict[str, Any] = {}
    for name, block in payload.items():
        if not isinstance(block, Mapping):
            continue
        item: Dict[str, Any] = {}
        if isinstance(block.get("columns"), list):
            item["columns"] = block["columns"]
        if isinstance(block.get("metadata"), Mapping):
            item["metadata"] = block["metadata"]
        rows = table_rows(block)
        if rows:
            item["sample_rows"] = rows[: min(3, len(rows))]
        item["row_count"] = len(block.get("data", [])) if isinstance(block.get("data"), list) else 0
        summary[name] = item
    print_json({"url": url, "headers": selected_headers(headers), "blocks": summary})
    return 0


def cursor_state(payload: Mapping[str, Any], block: str) -> Optional[Dict[str, Any]]:
    candidates = [f"{block}.cursor", "cursor"]
    for name in candidates:
        rows = table_rows(payload.get(name))
        if rows:
            row = rows[0]
            keys = {str(k).upper(): v for k, v in row.items()}
            if {"INDEX", "TOTAL", "PAGESIZE"}.issubset(keys):
                return {"INDEX": keys["INDEX"], "TOTAL": keys["TOTAL"], "PAGESIZE": keys["PAGESIZE"], "block": name}
    # Fallback: any block ending in .cursor
    for name, obj in payload.items():
        if not name.endswith(".cursor"):
            continue
        rows = table_rows(obj)
        if rows:
            keys = {str(k).upper(): v for k, v in rows[0].items()}
            if {"INDEX", "TOTAL", "PAGESIZE"}.issubset(keys):
                return {"INDEX": keys["INDEX"], "TOTAL": keys["TOTAL"], "PAGESIZE": keys["PAGESIZE"], "block": name}
    return None


def cmd_paginate(args: argparse.Namespace) -> int:
    base_params = request_params(args)
    start = int(base_params.pop("start", args.start))
    all_rows: List[Dict[str, Any]] = []
    pages = 0
    last_url = None
    mode = None

    while pages < args.max_pages:
        params = dict(base_params)
        params["start"] = str(start)
        payload, _headers, url = request_json(args.path, params, timeout=args.timeout, retries=args.retries)
        last_url = url
        rows = table_rows(payload.get(args.block))
        cur = cursor_state(payload, args.block)
        pages += 1

        if rows:
            all_rows.extend(rows)

        if cur:
            mode = "cursor"
            index = int(cur["INDEX"])
            total = int(cur["TOTAL"])
            pagesize = int(cur["PAGESIZE"])
            next_start = index + pagesize
            if next_start >= total or not rows:
                break
            start = next_start
            continue

        mode = mode or "start"
        if not rows:
            break
        start += len(rows)

    if pages >= args.max_pages:
        raise RuntimeError(f"Stopped after --max-pages={args.max_pages}; increase it if the response is intentionally larger")

    print_json({"last_url": last_url, "mode": mode, "pages": pages, "row_count": len(all_rows), "rows": all_rows})
    return 0


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Stdlib-only Moscow Exchange ISS API helper")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("index", help="Read /iss/index and decode hierarchy blocks")
    add_common_request_args(p)
    p.add_argument("--raw", action="store_true")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("search", help="Search /iss/securities?q=...")
    p.add_argument("query")
    p.add_argument("--limit", type=int)
    p.add_argument("--engine")
    p.add_argument("--market")
    p.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    p.add_argument("--retries", type=int, default=4)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("get", help="GET an ISS JSON route and decode all table blocks")
    p.add_argument("path")
    add_common_request_args(p)
    p.add_argument("--raw", action="store_true", help="Keep native ISS JSON and selected response headers")
    p.set_defaults(func=cmd_get)

    p = sub.add_parser("probe", help="Inspect columns/metadata/sample rows of an unfamiliar endpoint")
    p.add_argument("path")
    add_common_request_args(p)
    p.set_defaults(func=cmd_probe)

    p = sub.add_parser("paginate", help="Fetch a block through cursor or start pagination")
    p.add_argument("path")
    p.add_argument("--block", required=True, help="Target data block, e.g. history or securities")
    p.add_argument("--start", type=int, default=0)
    p.add_argument("--max-pages", type=int, default=1000)
    add_common_request_args(p)
    p.set_defaults(func=cmd_paginate)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = make_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (ValueError, RuntimeError) as exc:
        parser.error(str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
