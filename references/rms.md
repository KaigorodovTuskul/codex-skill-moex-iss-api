# RMS: risk-management datasets

## Why this family needs special handling

The live ISS reference exposes multiple entries with the same route template:

```text
/iss/rms/engines/{engine}/objects/[object]
```

but the actual object name is visible only in the response block/reference body. Never send literal `[object]` and never guess the schema from the generic title.

## Explicit documented routes

### `irr` — indicative risk rates

```text
/iss/rms/engines/{engine}/objects/irr
```

Arguments:

- `date`
- `q`
- `group` — exact-match list, up to 5
- `indicator` — exact-match list, up to 5
- `currencyid` — exact-match list, up to 5
- `instrument` — exact-match list, up to 5
- `isin` — exact-match list, up to 5
- `start` (default 0)
- `limit` (reference default `unlimited`)

Blocks include `irr`, `irr.cursor`, `irr.dates`.

### `settlementscalendar`

```text
/iss/rms/engines/{engine}/objects/settlementscalendar
```

Arguments: `year` (default today/current year semantics), `lang`.

## Generic-reference object map

The following mappings were resolved from the live reference pages reviewed on 2026-09-29:

| Official reference page | Actual object | Meaning |
|---|---|---|
| `/iss/reference/681` | `limits` | Minimum margin/risk-rate levels and concentration limits on derivatives. |
| `/iss/reference/729` | `rclimits` | `rclimits` dataset. Inspect metadata for exact current fields. |
| `/iss/reference/657` | `staticparams` | Static parameters. |
| `/iss/reference/691` | `staticparamskeyterm` | Static parameters by key terms. |
| `/iss/reference/651` | `percentfutures` | Interest-rate futures parameters. |

Concrete request form:

```text
/iss/rms/engines/{engine}/objects/limits
/iss/rms/engines/{engine}/objects/rclimits
/iss/rms/engines/{engine}/objects/staticparams
/iss/rms/engines/{engine}/objects/staticparamskeyterm
/iss/rms/engines/{engine}/objects/percentfutures
```

These five share a common documented argument pattern:

- `date` — works when no instrument code is supplied;
- `from`, `till` — documented for instrument-specific interval requests;
- `start=0`;
- `limit=1000`;
- `lang` on some objects;
- `<object>.cursor` and `<object>.dates`.

Do not assume the same fields across objects merely because their pagination parameters match.

## `cashflow`: official but underdocumented in the main catalog

MOEX published an ISS change notice on 2023-06-02 confirming:

```text
/iss/rms/engines/futures/objects/cashflow
```

and documented an updated structure including:

- `TRADEDATE`
- `ASSETCODE`
- `T`
- `CF`
- `CFRISK`
- `CFTYPE`
- `UPDATETIME`

The notice also said history would accumulate via `?date`. Older fields `BASE_CONTRACT_CODE`, `CORPORATE_ACTION_DATE`, `CASH_FLOW` were marked for later deletion.

**Rule:** treat this notice as evidence that the object exists, but inspect live metadata before coding field lists because the 2023 transition may already be complete.

Source: https://www.moex.com/n56498 (English) / https://www.moex.com/n56497 (Russian).

## `marketrates`: observed/underdocumented

The route supplied/observed in practice is:

```text
/iss/rms/engines/stock/objects/marketrates
```

It is **not** represented clearly in the reviewed public reference catalog and no sufficiently authoritative public schema was found in the reviewed MOEX/GitHub/Habr/Smart-Lab material.

Therefore:

1. Do not hardcode a field schema.
2. Probe it first:

```text
/iss/rms/engines/stock/objects/marketrates.json?iss.meta=on
```

3. Record all returned block names and metadata.
4. If history is needed, test `date` only after inspecting live behavior; do not assume it because other RMS objects use `date`.
5. Cross-check semantics against NCC risk-rate terminology only as secondary context, not as proof of ISS field identity.

Use the helper:

```bash
python scripts/moex_iss.py probe /iss/rms/engines/stock/objects/marketrates.json
```

## Version drift

MOEX has changed RMS fields over time. A 2023 MOEX notice updated derivatives `limits` fields to include `TRADEDATE`, `ASSETCODE`, `MR1`, `MR2`, `MR3`, `LK1`, `LK2`, `TITLE`, `GROUP_TITLE`, `UPDATETIME` and marked older `vcb/cl1/cl2/mr/mr_cl1/mr_cl2` fields for future deletion.

Never build critical risk logic on old field names without runtime verification.
