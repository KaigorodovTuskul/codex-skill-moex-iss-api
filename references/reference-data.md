# Reference Data 2.0, analytical products and SDFI

## Reference Data 2.0

### Securities listing

```text
/iss/referencedata/engines/{engine}/markets/all/securitieslisting
```

Arguments:

- `date` (current/latest semantics when omitted; reference default `today`)
- `start=0`
- `limit` — 1, 10, 20, 100, 1000, 5000; reference notes `limit` applies only with an unfilled `date`
- `lang`

Blocks include `securitieslisting`, cursor and dates.

### Stock full instrument list

```text
/iss/referencedata/engines/stock/markets/all/securities
```

Arguments: `date`, `start`, `limit`; cursor/dates. The reference lists allowed limits up to 1000 but also shows a default of 5000 — an internal inconsistency. Do not rely on the displayed default; specify an accepted limit or test the live route.

### Stock shorts

```text
/iss/referencedata/engines/stock/markets/all/shorts
```

Same documented date/start/limit/cursor pattern and the same default-vs-allowed inconsistency.

### Futures Reference Data 2.0

```text
/iss/referencedata/engines/futures/markets/{market}/risks
/iss/referencedata/engines/futures/markets/{market}/params
/iss/referencedata/engines/futures/markets/{market}/securities
```

Each uses `date`, `start`, `limit` (1/10/20/100/1000, default 1000 in the reference) and cursor/dates blocks.

## Analytical products — entitlement-controlled

Routes:

```text
/iss/analyticalproducts/netflow2/securities
/iss/analyticalproducts/netflow2/securities/{security}
/iss/analyticalproducts/futoi/securities
/iss/analyticalproducts/futoi/securities/{security}
```

NetFlow2 all-securities: `date`.

NetFlow2 one security: `from`, `till`; reference says there is no normal page navigation and one block is limited to 1000 rows, so move `from` forward after retrieved data.

FutOI all-securities: `date`, `latest=1` for last slice of day; dates block.

FutOI one security: `from`, `till`, `latest`; same 1000-row/no-normal-pagination note; dates block.

**Access rule:** these are information products. Current terms can include subscription, trial or delayed access. Verify the caller's entitlement and actual returned data before treating an empty/denied response as “no observations”.

## SDFI curves — mixed access model

Routes:

```text
/iss/sdfi/curves
/iss/sdfi/curves/{curveid}?date=YYYY-MM-DD
```

The directory route accepts `lang`; a curve route accepts `date`.

MOEX product documentation states that curves based on SDFI-market trades/orders require authorization plus a paid subscription, while curves based on external market-data sources require authorization but not necessarily a paid subscription.

Therefore do not label the entire `/iss/sdfi/**` family as either free or paid. Resolve the curve ID, authenticate as authorized, and classify access per curve/product.
