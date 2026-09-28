# Routing and `/iss/index`

## Why `/iss/index` comes first

`/iss/index` is the current global ISS dictionary. Use it to avoid stale hardcoded market topology.

Main blocks:

- `engines`
- `markets`
- `boards`
- `boardgroups`
- `durations`
- `securitytypes`
- `securitygroups`
- `securitycollections`

Useful query filters include `lang`, `boardgroups.engine`, `boardgroups.is_traded`, `securitytypes.engine`, and security-group filters.

## Market capability flags

The current reference documents these fields on `markets`:

- `is_otc`
- `has_history_files`
- `has_history_trades_files`
- `has_trades`
- `has_history`
- `has_candles`
- `has_orderbook`
- `has_tradingsession`
- `has_extra_yields`
- `has_delay`

Use the flag as a routing hint, not as proof that the caller has a subscription.

## Current engines observed in the 2026-09-29 snapshot

The live index included, among others:

```text
stock, state, currency, futures, commodity, interventions,
offboard, agro, otc, quotes, money
```

Do not freeze this list in application logic; refresh it from `/iss/index`.

## Resolution chain

When building an endpoint dynamically:

1. `/iss/index?iss.only=engines` → select `engine`.
2. `/iss/engines/{engine}/markets` or `/iss/index?iss.only=markets` → select `market`.
3. `/iss/engines/{engine}/markets/{market}/boards` and/or `boardgroups` → select scope.
4. `/iss/securities?q=...` → resolve `SECID` if needed.
5. `/iss/securities/{SECID}` → inspect all boards and primary board.
6. Choose current/history/statistics/RMS route by task and capabilities.

## Route decision tree

### “What is this instrument?”

Use:

```text
/iss/securities/{SECID}
```

For uncertain identifiers, search first with `/iss/securities?q=`.

### “What is trading now / current quote-like fields?”

Use one of:

```text
/iss/engines/{engine}/markets/{market}/securities
/iss/engines/{engine}/markets/{market}/securities/{SECID}
/iss/engines/{engine}/markets/{market}/boards/{board}/securities/{SECID}
```

Prefer board scope when price/settlement meaning differs by board.

### “Give me executions / trade tape”

Use `/trades`, preferably scoped to one security or board. Advance using `tradeno`/`recno`, not generic `start`.

### “Give me best bids/asks / orderbook”

Use `/orderbook`. Check entitlement and `has_orderbook`.

### “Give me candles”

Use `/candles`; use `/candleborders` to discover available range and `/iss/index` `durations` for supported intervals.

### “Give me historical close/yield/turnover”

Use `/iss/history/...`, not current marketdata. Choose market, board or boardgroup scope deliberately.

### “Where was this security traded historically?”

Use `/listing` rather than assuming its current primary board existed historically.

### “Give me a full large historical dump”

If `has_history_files`/`has_history_trades_files` is present and the archive endpoint covers the need, prefer `/iss/archives/...` over thousands of paginated API calls.

### “Risk rates / limits / clearing risk data”

Use `/iss/rms/...`; read `rms.md` because generic `[object]` pages hide actual object names.

### “Master/reference snapshot by date”

Use `/iss/referencedata/...` where available.

## Board and boardgroup caution

- `primary_board` means the instrument's current primary board; it is not automatically the correct board for historical analysis.
- `marketprice_board` is documented for selected stock markets and has restrictions when board/boardgroup filters are active.
- For historical stock data, `tradingsession` can materially change values; specify it if the question is session-specific.
