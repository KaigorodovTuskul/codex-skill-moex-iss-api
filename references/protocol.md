# ISS protocol and response rules

## Baseline

The MOEX ISS developer guide v1.4 (2016) remains useful for protocol mechanics, but it is not a current endpoint catalog. Treat the live `/iss/reference/` and `/iss/index` as authoritative for current route structure.

Base URL:

```text
https://iss.moex.com
```

ISS is REST-like: path segments identify engines, markets, boards/boardgroups and securities, while query parameters filter blocks and rows.

## Output formats

ISS supports endpoint suffixes such as:

- `.json`
- `.xml`
- `.csv`
- `.html`

Prefer JSON for automation. CSV has additional formatting controls (`iss.dp`, `iss.delimiter`, `iss.df`, `iss.tf`, `iss.dtf`) but JSON avoids locale-sensitive parsing.

## Global parameters

These are broadly reusable unless a live route behaves differently:

| Parameter | Meaning |
|---|---|
| `iss.meta=on|off` | Include/exclude block metadata. |
| `iss.data=on|off` | Include/exclude data rows. |
| `iss.only=block1,block2` | Return only selected response blocks. |
| `<block>.columns=A,B` | Restrict fields for a specific block. `first.columns`, `second.columns`, etc. can also address blocks by ordinal. |
| `iss.json=compact|extended` | JSON representation mode. |
| `iss.version=on|off` | Request query/statement version headers where supported. |

A parameter passed without a block prefix may affect every response block to which the parameter applies. Prefer explicit block prefixes if different blocks need different filtering.

## JSON table decoding

Typical block:

```json
{
  "history": {
    "columns": ["SECID", "TRADEDATE", "CLOSE"],
    "data": [
      ["MOEX", "2026-09-28", 221.15]
    ]
  }
}
```

Decode rows as:

```python
[dict(zip(block["columns"], row)) for row in block["data"]]
```

Never parse by fixed numeric column indices. ISS schemas can evolve.

## Metadata and precision

When interpreting numeric output:

1. If a field metadata entry has `PRECISION`, round/display using it.
2. Otherwise use the instrument's `DECIMALS` where applicable.
3. Treat `is_signed`, `has_percent`, and `alias` metadata as presentation hints.

For an unfamiliar/underdocumented route, first request:

```text
?iss.meta=on&iss.data=off
```

If the route does not return useful metadata with `iss.data=off`, retry a small live request with both metadata and data.

## Pagination

### Cursor-backed blocks

Many endpoints return `<block>.cursor` with:

- `INDEX` — first row index of current page;
- `TOTAL` — total rows;
- `PAGESIZE` — rows in the current page.

Loop until:

```text
INDEX + PAGESIZE >= TOTAL
```

Set the next `start` to `INDEX + PAGESIZE`.

### Start-only blocks

If there is no cursor but the endpoint supports `start`, request repeatedly and advance `start` by the count of returned rows. Stop when the target data block is empty.

### Live trades

Do not apply generic `start` pagination to live trade feeds if `tradeno`/`recno` exists. `start` is explicitly deprecated on current trade endpoints.

- `tradeno=<last_trade>` plus `next_trade=1` → next trade onward.
- on FORTS/OPTIONS, `recno` filters in execution order and supersedes `tradeno`.
- `limit` commonly allows 1, 10, 100, 1000, 5000.
- a later FORTS trade can have a smaller `TRADENO`; that is why `RECNO` is safer when available.

### Analytical product exception

Single-security NetFlow2/FutOI routes state that normal page navigation is absent and return at most 1000 rows. Advance `from` to a date after the last received data point rather than assuming `start`.

## SEQNUM and dataversion

Some current market blocks expose `SEQNUM` and accept `seqnum` to return only updates since a previous snapshot. Store the last processed sequence.

Also monitor the `dataversion` block. A data-version/trading-day transition may reset or reduce sequence numbers. On version change, rebuild the current state instead of assuming monotonic `SEQNUM` across sessions.

## HTTP failures and retries

- Retry 500, 501, 502, 503, 504 only as transient failures, with bounded exponential backoff and jitter.
- Do not retry 403 as if it were transient. It usually indicates access/entitlement or a genuinely forbidden resource.
- Validate content-type and expected block names; a 200 response with an unexpected payload is not a successful dataset retrieval.

## Authentication and entitlements

Historical developer documentation describes Basic authentication and the `MicexPassportCert` cookie. Current CCI documentation still describes the same cookie-based flow.

When authenticated, inspect `X-MicexPassport-Marker` where available:

- `granted` — response matches authenticated rights;
- `denied` — can indicate no subscription; depending on service it may produce 403 or a delayed/open variant.

Never store credentials in repository files, prompts, shell history or source code.

## Delay and access assumptions

Do not hardcode the 2016 guide's blanket access/delay rules as timeless policy. Current market capabilities and product licensing change. Use:

1. `/iss/index` capability flags;
2. current product documentation;
3. actual HTTP status and headers;
4. the live `/iss/reference/` page.
