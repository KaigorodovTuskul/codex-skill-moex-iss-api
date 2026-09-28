# MOEX ISS API

A Codex skill for reliable work with the Moscow Exchange Information & Statistical Server (ISS).

It combines the current online ISS reference, `/iss/index`, the MOEX ISS developer guide v1.4, current MOEX notices/manuals, and secondary implementation evidence for underdocumented behavior.

## What it covers

- discovery of `engine`, `market`, `boardgroup`, `board`, security groups/types/collections;
- instrument search and board resolution;
- current securities and market data;
- trades, order books and candles;
- historical trading results, yields, sessions and listing;
- downloadable history archives;
- statistics and specialized datasets;
- Reference Data 2.0;
- RMS risk datasets, including explicit resolution of generic `[object]` reference pages;
- pagination, cursors, `SEQNUM`/`dataversion`, precision and response parsing;
- access/entitlement handling;
- a small dependency-free Python ISS helper.

Commercial `/iss/cci/**` methods are deliberately excluded from the working catalog unless the user explicitly has CCI access and asks to use them.

## Structure

```text
.
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── protocol.md
│   ├── routing.md
│   ├── current-market.md
│   ├── history.md
│   ├── statistics.md
│   ├── rms.md
│   ├── reference-data.md
│   ├── endpoint-catalog.md
│   ├── recipes.md
│   └── source-notes.md
└── scripts/
    └── moex_iss.py
```

## Installation

Windows PowerShell:

```powershell
git clone <YOUR_REPOSITORY_URL> "$env:USERPROFILE\.agents\skills\moex-iss-api"
```

macOS/Linux:

```bash
git clone <YOUR_REPOSITORY_URL> ~/.agents/skills/moex-iss-api
```

Explicit invocation:

```text
$moex-iss-api
```

## Documentation snapshot

Research snapshot: **2026-09-29**.

The live MOEX reference identified itself as **v0.14.1** at the time of review. Because ISS is a live service, the skill instructs Codex to prefer current `/iss/reference/`, runtime metadata and `/iss/index` over stale hardcoded assumptions.
