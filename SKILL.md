---
name: moex-iss-api
description: "Query, inspect and integrate the Moscow Exchange ISS API reliably: discover engines/markets/boards and instruments, choose current/history/statistics/RMS/reference-data endpoints, handle ISS blocks, metadata, pagination and SEQNUM, and avoid subscription-only data unless access is explicitly available."
---

# MOEX ISS API

Use this skill when the user asks to obtain, inspect, automate, debug, or explain data from the Moscow Exchange Information & Statistical Server (ISS), including securities, market data, trades, order books, candles, history, statistics, archives, reference data, or risk-management (RMS) datasets.

## Operating rules

1. **Discover before hardcoding.** Resolve `engine`, `market`, `boardgroup`, `board`, security type/group/collection and supported capabilities from `/iss/index` or the corresponding hierarchy. Do not assume `stock/shares/TQBR` is appropriate merely because the instrument is an equity.
2. **Resolve the instrument identity.** If the user gives a name, ISIN, registration number, issuer identifier or uncertain ticker, search `/iss/securities?q=...`, then inspect `/iss/securities/{SECID}` and its `boards` block. Treat `SECID`, ISIN and board as different identifiers.
3. **Choose the smallest correct route.** Prefer a security or board scoped route over market-wide data when the task targets one instrument. Prefer `iss.only` and block-specific `.columns` to reduce payloads.
4. **Use JSON by default.** Parse ISS tables by pairing each block's `columns` with each row in `data`. Never hardcode column positions. Turn `iss.meta=on` on when discovering an unfamiliar schema; use `iss.data=off` if only metadata is needed.
5. **Keep block parameters scoped.** A parameter can affect all applicable blocks when unqualified. Use `marketdata.securities=...`, `securities.columns=...`, etc. when only one block should be filtered.
6. **Do not invent endpoint arguments.** Parameter names and semantics are endpoint-specific. Consult [references/endpoint-catalog.md](references/endpoint-catalog.md) and the family reference before constructing a request. If the live reference differs from this snapshot, prefer the live reference.
7. **Handle pagination by the endpoint's mechanism.** For `*.cursor` responses use `INDEX`, `PAGESIZE`, `TOTAL`; otherwise advance `start` by rows received until the target block is empty. For live trades prefer `tradeno` or, on FORTS/OPTIONS, `recno`; `start` is deprecated there. Some analytical-product single-security routes have no normal pagination and require advancing `from` by date.
8. **Handle live deltas correctly.** For blocks supporting `seqnum`, persist the last sequence number and request only later changes. Also track `dataversion`; a trading-day/version transition can reset or reduce sequence values.
9. **Respect precision metadata.** Use `PRECISION` when present; otherwise honor instrument `DECIMALS`. Do not infer display precision from Python/JSON float representation.
10. **Retry only transient HTTP failures.** Retry 500–504 with bounded exponential backoff. Do not blindly retry 403/entitlement errors or semantic 4xx responses.
11. **Treat access separately from route existence.** A path appearing in `/iss/reference/` does not guarantee anonymous/public access. Inspect HTTP status and `X-MicexPassport-Marker` when authentication is in use.
12. **Exclude CCI by default.** `/iss/cci/**` is a commercial corporate-information family. Do not route normal tasks there unless the user explicitly says they have CCI access and asks to use it. This skill intentionally does not reproduce the CCI method catalog.
13. **Gate other entitled products.** `/iss/analyticalproducts/**`, parts of `/iss/sdfi/**`, some archives/statistics/other information products may depend on subscription or authentication. Use them only after checking access; never silently substitute a paid source for an open one.
14. **Distinguish documented, underdocumented and observed RMS objects.** The reference exposes several `/iss/rms/.../objects/[object]` pages whose actual object names are hidden in the block name. Use the explicit object map in [references/rms.md](references/rms.md). For `cashflow` use the MOEX-published schema notes; for `marketrates` treat the route as observed/underdocumented and inspect live metadata instead of hardcoding fields.
15. **Prefer primary MOEX evidence.** Use the live ISS reference and ISS responses first; use MOEX notices/manuals for undocumented behavior; use GitHub/Habr/Smart-Lab only as secondary evidence when official documentation is incomplete.

## Workflow

### 1. Classify the request

Route the task to one of these families:

- instrument discovery/specification → `/iss/securities...`
- market/board discovery → `/iss/index`, `/iss/engines...`
- current securities/marketdata → `/iss/engines/.../securities...`
- live trades/order book → `/trades`, `/orderbook`
- candles → `/candles`, `/candleborders`
- historical end-of-day/yields/listing → `/iss/history/...`
- bulk downloadable history → `/iss/archives/...`
- exchange-calculated statistics → `/iss/statistics/...`
- current/historical reference master data → `/iss/referencedata/...`
- risk parameters/calendars → `/iss/rms/...`
- analytical products / SDFI → only after entitlement check
- `/iss/cci/**` → excluded unless explicitly requested with access

Read [references/routing.md](references/routing.md) for the decision tree and `/iss/index` capability flags.

### 2. Discover identifiers and capabilities

Query `/iss/index.json` with `iss.only=engines,markets,boards,boardgroups,securitytypes,securitygroups,securitycollections` as needed. Use market flags such as `has_history`, `has_candles`, `has_orderbook`, `has_tradingsession`, `has_extra_yields`, `has_history_files`, and `has_history_trades_files` before choosing a route.

For a known security:

```text
/iss/securities/{SECID}.json?iss.meta=off
```

For a search:

```text
/iss/securities.json?q=<query>&iss.meta=off
```

### 3. Build the lean request

Default base URL:

```text
https://iss.moex.com
```

Prefer:

```text
?iss.meta=off&iss.only=<block>&<block>.columns=<col1>,<col2>,...
```

For schema discovery instead use:

```text
?iss.meta=on&iss.data=off
```

Read [references/protocol.md](references/protocol.md) for global ISS parameters, formats, metadata, authentication and retry rules.

### 4. Fetch all required data safely

- Cursor-backed: read `<block>.cursor`, then set `start = INDEX + PAGESIZE` until `INDEX + PAGESIZE >= TOTAL`.
- Start-only: increment `start` by the number of rows received; stop on an empty target block.
- Live trades: advance by `TRADENO` plus `next_trade=1`; for FORTS/OPTIONS prefer `RECNO` where supported.
- `seqnum`: request only updates after the stored sequence, but reset state when `dataversion` changes.
- Analytical single-security NetFlow2/FutOI: respect the 1000-row block behavior and move `from` forward by date rather than assuming `start` pagination.

### 5. Validate the result

Before answering or saving output, verify:

- requested instrument and board are the intended ones;
- current vs historical source is appropriate;
- trading session filter is explicit when it matters;
- units/currency/price representation are understood;
- pagination is complete;
- no entitlement-denied response was mistaken for empty data;
- precision rules were applied;
- source URL and effective date/time are recorded for reproducibility.

## Reference routing

Read only the relevant files:

- [references/protocol.md](references/protocol.md) — request/response protocol, global parameters, auth, precision, pagination, retries.
- [references/routing.md](references/routing.md) — `/iss/index`, hierarchy discovery and route selection.
- [references/current-market.md](references/current-market.md) — current marketdata, trades, order books and candles.
- [references/history.md](references/history.md) — history, sessions, yields, listing, totals and archives.
- [references/statistics.md](references/statistics.md) — statistics and specialized exchange datasets.
- [references/rms.md](references/rms.md) — risk-management endpoints, explicit `[object]` mapping, underdocumented objects.
- [references/reference-data.md](references/reference-data.md) — Reference Data 2.0, analytical products, SDFI and access notes.
- [references/endpoint-catalog.md](references/endpoint-catalog.md) — all non-CCI entries from the live `/iss/reference/` snapshot, including official reference-page IDs.
- [references/recipes.md](references/recipes.md) — reusable request recipes.
- [references/source-notes.md](references/source-notes.md) — provenance, research date and documentation limitations.

## Helper script

Use `scripts/moex_iss.py` for deterministic request work instead of rewriting a client each time. It has no third-party dependencies.

Examples:

```bash
python scripts/moex_iss.py index --only markets,boards
python scripts/moex_iss.py search "RU000A10..."
python scripts/moex_iss.py get /iss/engines/stock/markets/bonds/securities.json \
  --param securities=RU000A10XXXX --only securities,marketdata
python scripts/moex_iss.py probe /iss/rms/engines/stock/objects/marketrates.json
python scripts/moex_iss.py paginate /iss/history/engines/stock/markets/bonds/securities/RU000A10XXXX.json \
  --block history --param from=2026-01-01 --param till=2026-09-29
```

Do not pass credentials on a command line that may be logged. If authenticated access is required, use an authorized secret mechanism in the user's environment and do not store credentials in this skill.

## Completion gate

Before delivery confirm that the route exists for the intended engine/market; route parameters match the live reference or a clearly labeled underdocumented source; identifiers were discovered rather than guessed; current/history/session semantics are correct; pagination or live sequencing is complete; CCI and other entitled products were not used without explicit access; undocumented RMS fields were discovered from the response rather than invented; and the final answer includes the exact ISS request(s) needed for reproducibility.
