# Sources and documentation status

Research snapshot: **2026-09-29**.

## Primary sources

1. Live ISS query reference: https://iss.moex.com/iss/reference/
   - reported version at review time: `v.0.14.1`;
   - every non-CCI entry numbered 0–168 in the index was opened and reviewed for its description/arguments;
   - exact reference-page IDs are preserved in `endpoint-catalog.md`.

2. Global ISS dictionary: https://iss.moex.com/iss/index
   - used for current engine/market/board/boardgroup/capability routing.

3. User-provided MOEX ISS developer guide v1.4 (2016), `iss-api-rus-v14.pdf`.
   - used for protocol mechanics: global ISS parameters, response blocks/metadata, precision, `SEQNUM`, pagination/cursors, authentication model, retries and dynamic-schema guidance;
   - not treated as the current endpoint catalog because it predates many current families.

4. MOEX RMS change notice (2023-06-02):
   - EN: https://www.moex.com/n56498
   - RU: https://www.moex.com/n56497
   - confirms futures `staticparams`, revised `limits` fields and `cashflow` fields/history.

5. MOEX Corporate Information Center product page:
   - https://www.moex.com/tsentr-korporativnoj-informatsii
   - confirms CCI is an access-controlled commercial information service with demo/contract workflow.

6. MOEX CCI user instruction:
   - https://www.moex.com/media/instruktsiya-po-ispolzovaniyu-servisov-tski.pdf
   - confirms authentication and that unauthenticated CCI information is unavailable.

7. MOEX information-services page:
   - https://www.moex.com/a2836
   - used for current product/access context, including SDFI curve access distinctions.

## Secondary sources

GitHub repositories were used only to cross-check route coverage/implementation patterns where official material is incomplete:

- https://github.com/uqee/moex-api — broad historical ISS route map; archived, therefore not authoritative for current behavior.
- https://github.com/Ruvad39/go-moex-iss — current community client; useful for implementation observations such as analytical-product handling, but secondary to MOEX docs/runtime responses.

Targeted searches on Habr and Smart-Lab for exact `marketrates`/RMS route documentation did not yield a sufficiently authoritative public schema in this review.

## Confidence labels used in this skill

- **documented** — current live `/iss/reference/` describes the route/arguments.
- **official-but-underdocumented** — MOEX itself confirms the route/fields outside the main reference (example: RMS `cashflow`).
- **observed/underdocumented** — route is known/observed but no adequate official public schema was located (example: RMS `marketrates`); inspect live metadata and do not hardcode.
- **entitlement-controlled** — route family exists but access depends on authentication/subscription/product terms.
- **excluded** — `/iss/cci/**` by default; intentionally not copied into the working route catalog because the user asked to omit closed subscription methods.

## Maintenance rule

ISS changes. When using this skill months later, compare the target route against the current `/iss/reference/`, inspect `/iss/index`, and probe metadata before changing production parsing logic. If the live reference and this snapshot conflict, prefer the live MOEX source and update the skill.
