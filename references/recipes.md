# ISS recipes

All examples use JSON and deliberately keep payloads small.

## Search for an instrument

```text
https://iss.moex.com/iss/securities.json?q=Сбербанк&iss.meta=off
```

Then inspect the chosen security:

```text
https://iss.moex.com/iss/securities/SBER.json?iss.meta=off
```

## Discover valid markets/boards

```text
https://iss.moex.com/iss/index.json?iss.only=markets,boards,boardgroups&iss.meta=off
```

Filter locally by engine/market IDs; do not hardcode from memory.

## Current security + marketdata only

```text
https://iss.moex.com/iss/engines/stock/markets/shares/securities/SBER.json?iss.only=securities,marketdata&iss.meta=off
```

For a lean marketdata payload:

```text
.../SBER.json?iss.only=marketdata&marketdata.columns=SECID,BOARDID,LAST,BID,OFFER,UPDATETIME&iss.meta=off
```

Validate that the requested columns exist in the live schema before depending on them.

## Multiple selected securities

```text
https://iss.moex.com/iss/engines/stock/markets/shares/securities.json?marketdata.securities=SBER,GAZP,LKOH&iss.only=marketdata&iss.meta=off
```

The documented filter limit is 10 instruments.

## Incremental market updates

Initial call:

```text
.../securities.json?iss.only=marketdata,dataversion&iss.meta=off
```

Store the largest/current `SEQNUM` and dataversion state, then:

```text
.../securities.json?marketdata.seqnum=<last_seqnum>&iss.only=marketdata,dataversion&iss.meta=off
```

If dataversion changes, rebuild the state.

## Historical security range

```text
https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/SBER.json?from=2026-01-01&till=2026-09-29&iss.only=history,history.cursor&iss.meta=off
```

Advance `start` using cursor `INDEX + PAGESIZE`.

## Historical bond yields

```text
https://iss.moex.com/iss/history/engines/stock/markets/bonds/securities/<SECID>.json?from=2026-01-01&till=2026-09-29
```

If yield measures are required, check/use the corresponding `/yields/<SECID>` route rather than assuming they are in `history`.

## Board-aware historical lookup

1. Inspect `/iss/securities/{SECID}` boards.
2. For long history, query `/iss/history/.../listing` to identify historical board intervals.
3. Query the appropriate `/boards/{board}/securities/{SECID}` history route.

## Candles

Find range:

```text
.../securities/SBER/candleborders.json
```

Then:

```text
.../securities/SBER/candles.json?from=2026-09-01&till=2026-09-29&interval=24&start=0
```

Confirm interval support via `/iss/index` `durations`.

## Live trades safely

First poll:

```text
.../boards/TQBR/securities/SBER/trades.json?limit=1000&iss.meta=off
```

Store last `TRADENO`; next poll:

```text
.../trades.json?tradeno=<last>&next_trade=1&limit=1000&iss.meta=off
```

For FORTS/OPTIONS, prefer `recno` if available.

## RMS documented object

```text
https://iss.moex.com/iss/rms/engines/futures/objects/limits.json?date=2026-09-29&iss.meta=off
```

## RMS unknown/underdocumented object probe

```text
https://iss.moex.com/iss/rms/engines/stock/objects/marketrates.json?iss.meta=on
```

Do not select columns until the returned schema is inspected.

## Bulk history archive discovery

```text
https://iss.moex.com/iss/archives/engines/stock/markets/shares/securities/years.json
```

Only use returned archive URLs after confirming access/licensing and file scope.
