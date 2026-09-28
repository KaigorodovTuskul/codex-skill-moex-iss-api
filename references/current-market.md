# Current market data

## Core current-security response

`/iss/engines/{engine}/markets/{market}/securities` and the scoped variants commonly return:

- `securities` — relatively static session/instrument fields;
- `marketdata` — dynamic market values;
- `dataversion` — snapshot/version state;
- `marketdata_yields` — where applicable.

Notable filters documented for the market-level security route include:

- `first`
- `marketprice_board`
- `primary_board`
- `index`
- `security_collection`
- `previous_session`
- `securities` (max 10)
- `sort_column`, `sort_order`
- `leaders`
- `nearest`
- `assets` (max 5; derivatives)
- `sectypes` (max 5; deprecated for derivatives in favor of `assets`)
- `lang`
- `seqnum` on dynamic blocks

Apply block-qualified filters when necessary, e.g.:

```text
?marketdata.securities=GAZP,AFLT&iss.only=marketdata
```

## `marketprice_board` vs `primary_board`

`marketprice_board=1` is documented for `engine=stock` with markets `shares`, `bonds`, `foreignshares`; board/boardgroup filtering must be disabled.

`primary_board` is available for stock and currency but should be used cautiously outside the principal trading modes.

## Trades

Current trade routes exist at market, board, boardgroup and single-security scope.

Important arguments:

- `tradeno` — start from this trade number;
- `recno` — FORTS/OPTIONS execution-order sequence; supersedes `tradeno`;
- `next_trade=1` — exclude the anchor trade and continue after it;
- `securities` — security filter where supported;
- `limit` — commonly 1/10/100/1000/5000;
- `reversed`
- `previous_session`
- `start` — deprecated for current trades;
- `yielddatetype` on trade-yield blocks (`MBS`, `MATDATE`, `OFFERDATE`).

For a streaming/polling client, persist the final `RECNO` or `TRADENO` and use `next_trade=1` on the next request.

## Order book

Order-book routes exist at market, board, boardgroup and single-security levels. `securities` can filter multi-security routes. Some routes include `dataversion`.

Do not assume orderbook availability from route existence alone. Check `/iss/index` `has_orderbook`, entitlement/headers and actual response.

## Candles

Routes:

```text
/iss/engines/{engine}/markets/{market}/securities/{security}/candles
/iss/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}/candles
/iss/engines/{engine}/markets/{market}/boards/{board}/securities/{security}/candles
```

Typical candle arguments include `from`, `till`, `interval`, and `start`. Use `candleborders` first when the available range is unknown. Use `/iss/index` `durations` rather than guessing supported `interval` values.

## Current turnover and session results

- `/iss/turnovers` — aggregate market turnover; supports `date`, `is_tonight_session`.
- `/iss/engines/{engine}/turnovers` — turnover by markets in an engine; same main filters.
- `/iss/engines/{engine}/markets/{market}/turnovers` — current market turnover.
- `/iss/engines/{engine}/markets/{market}/secstats` — intermediate end-of-session summaries for stock; `tradingsession` 1 main, 2 evening, 3 total; `securities` max 10, `boardid` max 10.

## ZCYC note

The older `/iss/engines/{engine}/markets/zcyc` reference explicitly states that calculations ceased on 2018-01-03. Do not use it for current curve work merely because the endpoint remains documented. A separate `/iss/engines/{engine}/zcyc` family exists; verify the intended curve/source/date before use.
