# Statistics endpoints

The `/iss/statistics/**` family is heterogeneous. Do not treat it as one schema. The reference catalog is the source of truth for each dataset.

## Futures/options

Useful routes include:

- `/iss/statistics/engines/futures/promo`
- `/markets/options/assets`
- `/assets/{asset}`
- `/assets/{asset}/volumes`
- `/assets/{asset}/optionboard`
- `/assets/{asset}/openpositions`
- `/assets/{asset}/turnovers`
- `/markets/forts/series`
- `/markets/options/series`
- `/series/{series_name}/securities`
- `/markets/{market}/openpositions`
- `/markets/{market}/openpositions/{asset}`

Notable arguments:

- option series: `asset_code`, `show_expired`; unfiltered output capped at 500 rows according to the reference;
- series securities: `option_type=P|C`;
- open positions: `date`, `from`, `till`, plus option filters `option_type`, `margin_style`, `exec_type`, `settle_type`, `option_on_spot`, `lang`.

## Stock

Routes include:

- correlations (`date`, `start`, cursor/dates);
- splits;
- deviation coefficients (`date`, `start`, cursor/dates);
- quoted securities (`date`, dates);
- current prices (`date`, `start`, `tradingsession`; also session 5 = weekend additional session);
- month-end accrued interest (`date=latest` by default);
- bond aggregates and columns;
- index analytics, index ticker history, bulletins, RUSFAR, capitalization;
- complex-instrument markers.

## Repo/state

- `/iss/statistics/engines/state/markets/repo/mirp` — `date`, `lang`, sorting, `start`, cursor/dates.
- `/dealers` — `date`, `lang`, dates.
- `/cboper` — weighted central-bank operation rates by `date`, `lang`.
- `/iss/statistics/engines/state/rates` and `/columns` — state-rate datasets; inspect live metadata for columns.

## Currency/fixing/indicative rates

- `/iss/statistics/engines/currency/markets/selt/rates` → `cbrf`, `wap_rates`, `date`.
- `/iss/statistics/engines/currency/markets/fixing` and `/{security}` → MOEX fixings.
- `/iss/statistics/engines/futures/markets/indicativerates/securities` and `/{security}` → derivatives-market indicative FX rates.

## Collateral repricing

Generic route family:

```text
/iss/statistics/engines/{engine}/markets/{market}
/iss/statistics/engines/{engine}/markets/{market}/securities
/iss/statistics/engines/{engine}/markets/{market}/securities/{security}
```

The live reference describes these as collateral-instrument repricing rates. Use route-specific dates/range parameters; do not confuse them with live trade prices.

## Derivatives reports

Weekly route:

```text
/iss/statistics/engines/{engine}/derivatives/{report_name}
```

Documented report names include:

- `numtrades`
- `participants`
- `openpositions`
- `expirationparticipants`
- `expirationopenpositions`

There is also `/iss/statistics/engines/{engine}/monthly/{report_name}`.

## Markup datasets

Current:

```text
/iss/statistics/markup/{markup_name}/{markup_type}/{markup_view}
```

Historical:

```text
/iss/history/statistics/markup/{markup_name}/{markup_type}
```

Current supports `q`, `start`, `limit` (1/10/20/50/100/1000), cursor and columns. Historical requires `from` and `till`, supports the same text search/pagination controls, and has a columns block.

These may be information products with separate access conditions. Check actual entitlement before relying on them.
