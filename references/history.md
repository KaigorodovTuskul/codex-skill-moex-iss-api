# History, listing and archives

## History families

Historical trading results are available at market, board and boardgroup scope, with separate routes for:

- `securities`
- `yields`
- `dates`
- `listing`
- stock `sessions/...`
- stock `totals/...`

Do not derive history by repeatedly sampling current marketdata.

## One-date collection queries

Typical all-security history route:

```text
/iss/history/engines/{engine}/markets/{market}/securities.json?date=YYYY-MM-DD
```

Common filters across collection history endpoints:

- `date`
- `tradingsession` — stock: 0 morning, 1 main, 2 evening, 3 total
- `interim` — currency intermediate results
- `security_collection`
- `marketprice_board`
- `assetcode` — futures/options
- `numtrades`
- `sort_column`, `sort_order`
- `start`, `limit`
- `lang`

Do not blindly send every parameter to every route; use the specific reference page.

## Single-security interval queries

Typical route:

```text
/iss/history/engines/{engine}/markets/{market}/securities/{security}.json?from=YYYY-MM-DD&till=YYYY-MM-DD
```

Frequently supported:

- `from`
- `till`
- `numtrades`
- `lang`
- `limit`
- `sort_column` (often `TRADEDATE`)
- `sort_order`
- `start`
- `tradingsession`
- `marketprice_board`

Note: some reference pages contain inconsistent/default text for sorting. Do not copy a default blindly; verify live output when sort order matters.

## Cursor

Many history endpoints expose `history.cursor` or `<block>.cursor`. Use the cursor as the termination criterion rather than assuming a fixed 100-row page size.

## Sessions

Stock history exposes `/sessions` and session-scoped security routes. Use them when the user needs a specific morning/main/evening/total session rather than relying on combined day values.

## Listing history

Use `/listing` when an instrument may have changed boards/listing status. This is especially important for long historical series; the current primary board is not a valid substitute for historical board membership.

## Yields

Bond/eligible-market history has separate `/yields` routes at market, board and boardgroup scope. Do not assume yield fields are present in the price-history block.

## Stock totals

`/iss/history/engines/stock/totals/...` provides generalized stock-market totals by date, board and security. Collection routes use `date`, `start`, `tradingsession`; single-security routes use `from`, `till`, `start`, `tradingsession` and expose cursor/date blocks.

## OTC NSD aggregates

- `/iss/history/otc/providers/nsd/markets`
- `/.../{market}/daily?date=...`
- `/.../{market}/monthly?year=...&month=...`

The monthly route requires `year` and `month` together.

## Archive files

Routes:

```text
/iss/archives/engines/{engine}/markets/{market}/{datatype}/years
/iss/archives/engines/{engine}/markets/{market}/{datatype}/{period}
/iss/archives/engines/{engine}/markets/{market}/{datatype}/years/{year}/months
```

`datatype` values documented by MOEX:

- `securities`
- `trades`

`period` values:

- `yearly`
- `monthly`
- `daily`

The reference states that monthly data in this archive route is available only for the last 30 days. Check current product access/licensing before assuming a downloadable file is anonymous/public.
