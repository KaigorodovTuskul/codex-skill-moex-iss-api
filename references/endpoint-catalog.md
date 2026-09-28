# Endpoint catalog — public/non-CCI snapshot

Snapshot date: **2026-09-29**. The reviewed live `/iss/reference/` reported **v0.14.1**.

This table covers every index entry **0–168** from the live reference. Entries **169+** are the commercial `/iss/cci/**` family and are intentionally excluded from this working catalog. The `Reference` column is the actual MOEX reference-page ID, not the list ordinal.

Generic system parameters such as `iss.meta`, `iss.data`, `iss.only` and block `.columns` are described in `protocol.md` and are not repeated on every row. For exact parameter descriptions/defaults, open the linked official reference page; the compact note here is a routing aid, not a replacement for runtime verification.

| # | Reference | Route | Key arguments / note |
|---:|---:|---|---|
| 0 | [/205](https://iss.moex.com/iss/reference/205) | `/iss/securities` | q, lang, engine, is_trading, market, group_by, group_by_filter, limit, start |
| 1 | [/193](https://iss.moex.com/iss/reference/193) | `/iss/securities/[security]` | description: lang; boards: lang, primary_board, start |
| 2 | [/199](https://iss.moex.com/iss/reference/199) | `/iss/securities/[security]/indices` | lang, only_actual |
| 3 | [/201](https://iss.moex.com/iss/reference/201) | `/iss/securities/[security]/aggregates` | lang, date |
| 4 | [/543](https://iss.moex.com/iss/reference/543) | `/iss/index` | global dictionaries; boardgroup/security-type/group filters; capability discovery |
| 5 | [/227](https://iss.moex.com/iss/reference/227) | `/iss/turnovers` | lang, is_tonight_session, date |
| 6 | [/225](https://iss.moex.com/iss/reference/225) | `/iss/turnovers/columns` | See the official reference page and relevant family note before constructing arguments. |
| 7 | [/403](https://iss.moex.com/iss/reference/403) | `/iss/engines/[engine]/markets/[market]/secstats` | tradingsession, securities<=10, boardid<=10 |
| 8 | [/413](https://iss.moex.com/iss/reference/413) | `/iss/engines/[engine]/turnovers` | lang, is_tonight_session, date |
| 9 | [/399](https://iss.moex.com/iss/reference/399) | `/iss/engines/[engine]/markets/[market]/turnovers` | See the official reference page and relevant family note before constructing arguments. |
| 10 | [/405](https://iss.moex.com/iss/reference/405) | `/iss/engines/[engine]/markets/zcyc` | legacy ZCYC; from, till, start; calculations marked stopped 2018-01-03 |
| 11 | [/417](https://iss.moex.com/iss/reference/417) | `/iss/engines/[engine]/zcyc` | date-oriented zcyc blocks; inspect specific block |
| 12 | [/499](https://iss.moex.com/iss/reference/499) | `/iss/history/otc/providers/nsd/markets` | See the official reference page and relevant family note before constructing arguments. |
| 13 | [/447](https://iss.moex.com/iss/reference/447) | `/iss/history/otc/providers/nsd/markets/[market]/daily` | date, lang |
| 14 | [/517](https://iss.moex.com/iss/reference/517) | `/iss/history/otc/providers/nsd/markets/[market]/monthly` | year + month required together; lang |
| 15 | [/391](https://iss.moex.com/iss/reference/391) | `/iss/engines` | discovery/schema route; mainly lang or no complex filters |
| 16 | [/397](https://iss.moex.com/iss/reference/397) | `/iss/engines/[engine]` | discovery/schema route; mainly lang or no complex filters |
| 17 | [/411](https://iss.moex.com/iss/reference/411) | `/iss/engines/[engine]/markets/[market]/.*?orderbook/columns` | discovery/schema route; mainly lang or no complex filters |
| 18 | [/381](https://iss.moex.com/iss/reference/381) | `/iss/engines/[engine]/markets/[market]/.*?securities/columns` | discovery/schema route; mainly lang or no complex filters |
| 19 | [/343](https://iss.moex.com/iss/reference/343) | `/iss/engines/[engine]/markets` | discovery/schema route; mainly lang or no complex filters |
| 20 | [/345](https://iss.moex.com/iss/reference/345) | `/iss/engines/[engine]/markets/[market]/.*?trades/columns` | discovery/schema route; mainly lang or no complex filters |
| 21 | [/351](https://iss.moex.com/iss/reference/351) | `/iss/engines/[engine]/markets/[market]` | discovery/schema route; mainly lang or no complex filters |
| 22 | [/419](https://iss.moex.com/iss/reference/419) | `/iss/engines/[engine]/markets/[market]/securities` | security/marketdata blocks; filters include primary/marketprice board, securities, assets, sectypes, seqnum |
| 23 | [/347](https://iss.moex.com/iss/reference/347) | `/iss/engines/[engine]/markets/[market]/securities/[security]` | security/marketdata blocks; filters include primary/marketprice board, securities, assets, sectypes, seqnum |
| 24 | [/425](https://iss.moex.com/iss/reference/425) | `/iss/engines/[engine]/markets/[market]/securities/[security]/trades` | live trades: tradeno, recno(FORTS/options), next_trade, limit, reversed, previous_session; start deprecated |
| 25 | [/357](https://iss.moex.com/iss/reference/357) | `/iss/engines/[engine]/markets/[market]/securities/[security]/orderbook` | orderbook; multi-security routes may accept securities; verify entitlement |
| 26 | [/317](https://iss.moex.com/iss/reference/317) | `/iss/engines/[engine]/markets/[market]/orderbook` | orderbook; multi-security routes may accept securities; verify entitlement |
| 27 | [/379](https://iss.moex.com/iss/reference/379) | `/iss/engines/[engine]/markets/[market]/trades` | live trades: tradeno, recno(FORTS/options), next_trade, limit, reversed, previous_session; start deprecated |
| 28 | [/723](https://iss.moex.com/iss/reference/723) | `/iss/engines/[engine]/markets/[market]/boards` | discovery/schema route; mainly lang or no complex filters |
| 29 | [/361](https://iss.moex.com/iss/reference/361) | `/iss/engines/[engine]/markets/[market]/boards/[board]` | discovery/schema route; mainly lang or no complex filters |
| 30 | [/353](https://iss.moex.com/iss/reference/353) | `/iss/engines/[engine]/markets/[market]/boards/[board]/securities` | security/marketdata blocks; filters include primary/marketprice board, securities, assets, sectypes, seqnum |
| 31 | [/359](https://iss.moex.com/iss/reference/359) | `/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]` | security/marketdata blocks; filters include primary/marketprice board, securities, assets, sectypes, seqnum |
| 32 | [/323](https://iss.moex.com/iss/reference/323) | `/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/trades` | live trades: tradeno, recno(FORTS/options), next_trade, limit, reversed, previous_session; start deprecated |
| 33 | [/371](https://iss.moex.com/iss/reference/371) | `/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/orderbook` | orderbook; multi-security routes may accept securities; verify entitlement |
| 34 | [/341](https://iss.moex.com/iss/reference/341) | `/iss/engines/[engine]/markets/[market]/securities/[security]/candles` | candles: from, till, interval, start |
| 35 | [/389](https://iss.moex.com/iss/reference/389) | `/iss/engines/[engine]/markets/[market]/securities/[security]/candleborders` | candle availability/borders |
| 36 | [/369](https://iss.moex.com/iss/reference/369) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/candleborders` | candle availability/borders |
| 37 | [/427](https://iss.moex.com/iss/reference/427) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/candles` | candles: from, till, interval, start |
| 38 | [/409](https://iss.moex.com/iss/reference/409) | `/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/candles` | candles: from, till, interval, start |
| 39 | [/333](https://iss.moex.com/iss/reference/333) | `/iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/candleborders` | candle availability/borders |
| 40 | [/325](https://iss.moex.com/iss/reference/325) | `/iss/engines/[engine]/markets/[market]/boards/[board]/trades` | live trades: tradeno, recno(FORTS/options), next_trade, limit, reversed, previous_session; start deprecated |
| 41 | [/395](https://iss.moex.com/iss/reference/395) | `/iss/engines/[engine]/markets/[market]/boards/[board]/orderbook` | orderbook; multi-security routes may accept securities; verify entitlement |
| 42 | [/393](https://iss.moex.com/iss/reference/393) | `/iss/engines/[engine]/markets/[market]/boardgroups` | discovery/schema route; mainly lang or no complex filters |
| 43 | [/367](https://iss.moex.com/iss/reference/367) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]` | discovery/schema route; mainly lang or no complex filters |
| 44 | [/385](https://iss.moex.com/iss/reference/385) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities` | security/marketdata blocks; filters include primary/marketprice board, securities, assets, sectypes, seqnum |
| 45 | [/387](https://iss.moex.com/iss/reference/387) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]` | security/marketdata blocks; filters include primary/marketprice board, securities, assets, sectypes, seqnum |
| 46 | [/329](https://iss.moex.com/iss/reference/329) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/trades` | live trades: tradeno, recno(FORTS/options), next_trade, limit, reversed, previous_session; start deprecated |
| 47 | [/315](https://iss.moex.com/iss/reference/315) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/orderbook` | orderbook; multi-security routes may accept securities; verify entitlement |
| 48 | [/355](https://iss.moex.com/iss/reference/355) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/trades` | live trades: tradeno, recno(FORTS/options), next_trade, limit, reversed, previous_session; start deprecated |
| 49 | [/313](https://iss.moex.com/iss/reference/313) | `/iss/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/orderbook` | orderbook; multi-security routes may accept securities; verify entitlement |
| 50 | [/461](https://iss.moex.com/iss/reference/461) | `/iss/history/engines/[engine]/markets/[market]/.*?listing/columns` | listing/schema history; use for historical board membership |
| 51 | [/489](https://iss.moex.com/iss/reference/489) | `/iss/history/engines/[engine]/markets/[market]/listing` | listing/schema history; use for historical board membership |
| 52 | [/459](https://iss.moex.com/iss/reference/459) | `/iss/history/engines/[engine]/markets/[market]/boards/[board]/listing` | listing/schema history; use for historical board membership |
| 53 | [/479](https://iss.moex.com/iss/reference/479) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/listing` | listing/schema history; use for historical board membership |
| 54 | [/519](https://iss.moex.com/iss/reference/519) | `/iss/history/engines/[engine]/markets/[market]/sessions` | stock sessions directory |
| 55 | [/467](https://iss.moex.com/iss/reference/467) | `/iss/history/engines/[engine]/markets/[market]/sessions/[session]/securities` | session-scoped history; date or from/till plus standard history filters/cursor |
| 56 | [/435](https://iss.moex.com/iss/reference/435) | `/iss/history/engines/[engine]/markets/[market]/sessions/[session]/securities/[security]` | session-scoped history; date or from/till plus standard history filters/cursor |
| 57 | [/521](https://iss.moex.com/iss/reference/521) | `/iss/history/engines/[engine]/markets/[market]/session/[session]/boardgroups/[boardgroup]/securities` | session-scoped history; date or from/till plus standard history filters/cursor |
| 58 | [/469](https://iss.moex.com/iss/reference/469) | `/iss/history/engines/[engine]/markets/[market]/sessions/[session]/boardgroups/[boardgroup]/securities/[security]` | session-scoped history; date or from/till plus standard history filters/cursor |
| 59 | [/529](https://iss.moex.com/iss/reference/529) | `/iss/history/engines/[engine]/markets/[market]/sessions/[session]/boards/[board]/securities` | session-scoped history; date or from/till plus standard history filters/cursor |
| 60 | [/445](https://iss.moex.com/iss/reference/445) | `/iss/history/engines/[engine]/markets/[market]/sessions/[session]/boards/[board]/securities/[security]` | session-scoped history; date or from/till plus standard history filters/cursor |
| 61 | [/441](https://iss.moex.com/iss/reference/441) | `/iss/history/engines/[engine]/markets/[market]/.*?[securities]/columns` | history columns/schema |
| 62 | [/477](https://iss.moex.com/iss/reference/477) | `/iss/history/engines/stock/markets/shares/securities/changeover` | stock code-change history |
| 63 | [/475](https://iss.moex.com/iss/reference/475) | `/iss/history/engines/stock/zcyc` | historical ZCYC |
| 64 | [/497](https://iss.moex.com/iss/reference/497) | `/iss/history/engines/[engine]/markets/[market]/securities` | collection history: date, session/interim/collection/asset filters, sort, start/limit, cursor |
| 65 | [/513](https://iss.moex.com/iss/reference/513) | `/iss/history/engines/[engine]/markets/[market]/yields` | yield collection history; date + standard history filters/start/limit |
| 66 | [/463](https://iss.moex.com/iss/reference/463) | `/iss/history/engines/[engine]/markets/[market]/dates` | date-range availability; session/interim where supported |
| 67 | [/439](https://iss.moex.com/iss/reference/439) | `/iss/history/engines/[engine]/markets/[market]/securities/[security]` | single-security history: from, till, sort, start/limit, session/marketprice filters; cursor |
| 68 | [/501](https://iss.moex.com/iss/reference/501) | `/iss/history/engines/[engine]/markets/[market]/yields/[security]` | single-security yield history: from, till, sort, start/limit, marketprice filters |
| 69 | [/433](https://iss.moex.com/iss/reference/433) | `/iss/history/engines/[engine]/markets/[market]/securities/[security]/dates` | date-range availability; session/interim where supported |
| 70 | [/503](https://iss.moex.com/iss/reference/503) | `/iss/history/engines/[engine]/markets/[market]/boards/[board]/dates` | date-range availability; session/interim where supported |
| 71 | [/491](https://iss.moex.com/iss/reference/491) | `/iss/history/engines/[engine]/markets/[market]/boards/[board]/securities` | collection history: date, session/interim/collection/asset filters, sort, start/limit, cursor |
| 72 | [/443](https://iss.moex.com/iss/reference/443) | `/iss/history/engines/[engine]/markets/[market]/boards/[board]/yields` | yield collection history; date + standard history filters/start/limit |
| 73 | [/531](https://iss.moex.com/iss/reference/531) | `/iss/history/engines/[engine]/markets/[market]/boards/[board]/securities/[security]` | single-security history: from, till, sort, start/limit, session/marketprice filters; cursor |
| 74 | [/495](https://iss.moex.com/iss/reference/495) | `/iss/history/engines/[engine]/markets/[market]/boards/[board]/yields/[security]` | single-security yield history: from, till, sort, start/limit, marketprice filters |
| 75 | [/457](https://iss.moex.com/iss/reference/457) | `/iss/history/engines/[engine]/markets/[market]/boards/[board]/securities/[security]/dates` | date-range availability; session/interim where supported |
| 76 | [/465](https://iss.moex.com/iss/reference/465) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/dates` | date-range availability; session/interim where supported |
| 77 | [/453](https://iss.moex.com/iss/reference/453) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities` | collection history: date, session/interim/collection/asset filters, sort, start/limit, cursor |
| 78 | [/487](https://iss.moex.com/iss/reference/487) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]` | single-security history: from, till, sort, start/limit, session/marketprice filters; cursor |
| 79 | [/493](https://iss.moex.com/iss/reference/493) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities` | collection history: date, session/interim/collection/asset filters, sort, start/limit, cursor |
| 80 | [/455](https://iss.moex.com/iss/reference/455) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/yields` | yield collection history; date + standard history filters/start/limit |
| 81 | [/483](https://iss.moex.com/iss/reference/483) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]` | single-security history: from, till, sort, start/limit, session/marketprice filters; cursor |
| 82 | [/473](https://iss.moex.com/iss/reference/473) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/yields/[security]` | single-security yield history: from, till, sort, start/limit, marketprice filters |
| 83 | [/451](https://iss.moex.com/iss/reference/451) | `/iss/history/engines/[engine]/markets/[market]/boardgroups/[boardgroup]/securities/[security]/dates` | date-range availability; session/interim where supported |
| 84 | [/247](https://iss.moex.com/iss/reference/247) | `/iss/archives/engines/[engine]/markets/[market]/[datatype]/years` | archive year/month directory; datatype=securities\|trades |
| 85 | [/249](https://iss.moex.com/iss/reference/249) | `/iss/archives/engines/[engine]/markets/[market]/[datatype]/[period]` | archive links; datatype=securities\|trades; period=yearly\|monthly\|daily |
| 86 | [/253](https://iss.moex.com/iss/reference/253) | `/iss/archives/engines/[engine]/markets/[market]/[datatype]/years/[year]/months` | archive year/month directory; datatype=securities\|trades |
| 87 | [/181](https://iss.moex.com/iss/reference/181) | `/iss/securitygroups` | security-group/collection directory; mostly lang/start depending route |
| 88 | [/189](https://iss.moex.com/iss/reference/189) | `/iss/securitygroups/[securitygroup]` | security-group/collection directory; mostly lang/start depending route |
| 89 | [/187](https://iss.moex.com/iss/reference/187) | `/iss/securitygroups/[securitygroup]/collections` | security-group/collection directory; mostly lang/start depending route |
| 90 | [/185](https://iss.moex.com/iss/reference/185) | `/iss/securitygroups/[securitygroup]/collections/[collection]` | security-group/collection directory; mostly lang/start depending route |
| 91 | [/183](https://iss.moex.com/iss/reference/183) | `/iss/securitygroups/[securitygroup]/collections/[collection]/securities` | security-group/collection directory; mostly lang/start depending route |
| 92 | [/763](https://iss.moex.com/iss/reference/763) | `/iss/statistics/engines/futures/promo` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 93 | [/111](https://iss.moex.com/iss/reference/111) | `/iss/statistics/engines/futures/markets/options/assets` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 94 | [/81](https://iss.moex.com/iss/reference/81) | `/iss/statistics/engines/futures/markets/options/assets/[asset]` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 95 | [/119](https://iss.moex.com/iss/reference/119) | `/iss/statistics/engines/futures/markets/options/assets/[asset]/volumes` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 96 | [/9](https://iss.moex.com/iss/reference/9) | `/iss/statistics/engines/futures/markets/options/assets/[asset]/optionboard` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 97 | [/145](https://iss.moex.com/iss/reference/145) | `/iss/statistics/engines/futures/markets/options/assets/[asset]/openpositions` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 98 | [/49](https://iss.moex.com/iss/reference/49) | `/iss/statistics/engines/futures/markets/options/assets/[asset]/turnovers` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 99 | [/151](https://iss.moex.com/iss/reference/151) | `/iss/statistics/engines/futures/markets/forts/series` | specialized futures/options statistics; inspect live reference for route-specific filters |
| 100 | [/173](https://iss.moex.com/iss/reference/173) | `/iss/statistics/engines/futures/markets/options/series` | asset_code, show_expired; unfiltered series max 500 |
| 101 | [/43](https://iss.moex.com/iss/reference/43) | `/iss/statistics/engines/futures/markets/options/series/[series_name]/securities` | option_type=P\|C |
| 102 | [/155](https://iss.moex.com/iss/reference/155) | `/iss/statistics/engines/futures/markets/[market]/openpositions` | date/from/till; option filters option_type, margin_style, exec_type, settle_type, option_on_spot |
| 103 | [/59](https://iss.moex.com/iss/reference/59) | `/iss/statistics/engines/futures/markets/[market]/openpositions/[asset]` | date/from/till; option filters option_type, margin_style, exec_type, settle_type, option_on_spot |
| 104 | [/95](https://iss.moex.com/iss/reference/95) | `/iss/statistics/complex/securities` | start |
| 105 | [/11](https://iss.moex.com/iss/reference/11) | `/iss/statistics/complex/securities/[security]` | See the official reference page and relevant family note before constructing arguments. |
| 106 | [/153](https://iss.moex.com/iss/reference/153) | `/iss/statistics/engines/stock/markets/shares/correlations` | date, start; cursor/dates |
| 107 | [/169](https://iss.moex.com/iss/reference/169) | `/iss/statistics/engines/currency/markets/selt/rates` | cbrf + wap_rates; date |
| 108 | [/17](https://iss.moex.com/iss/reference/17) | `/iss/statistics/engines/stock/splits` | split/consolidation directory/security detail |
| 109 | [/57](https://iss.moex.com/iss/reference/57) | `/iss/statistics/engines/stock/splits/[security]` | split/consolidation directory/security detail |
| 110 | [/45](https://iss.moex.com/iss/reference/45) | `/iss/statistics/engines/state/markets/repo/mirp` | date, lang, sort fields, start; cursor/dates |
| 111 | [/113](https://iss.moex.com/iss/reference/113) | `/iss/statistics/engines/state/markets/repo/dealers` | date, lang; dates |
| 112 | [/69](https://iss.moex.com/iss/reference/69) | `/iss/statistics/engines/state/markets/repo/cboper` | date, lang; dates |
| 113 | [/27](https://iss.moex.com/iss/reference/27) | `/iss/statistics/engines/stock/deviationcoeffs` | date, start; cursor/dates |
| 114 | [/165](https://iss.moex.com/iss/reference/165) | `/iss/statistics/engines/stock/quotedsecurities` | date; dates |
| 115 | [/53](https://iss.moex.com/iss/reference/53) | `/iss/statistics/engines/stock/currentprices` | date, start, tradingsession (0/1/2/5); dates |
| 116 | [/21](https://iss.moex.com/iss/reference/21) | `/iss/statistics/engines/stock/markets/bonds/monthendaccints` | date (default latest) |
| 117 | [/159](https://iss.moex.com/iss/reference/159) | `/iss/statistics/engines/stock/markets/index/analytics/columns` | index/RUSFAR schema or attributes; route-specific date/lang |
| 118 | [/93](https://iss.moex.com/iss/reference/93) | `/iss/statistics/engines/stock/markets/index/bulletins` | date, market EQ\|FI\|MX |
| 119 | [/35](https://iss.moex.com/iss/reference/35) | `/iss/statistics/engines/stock/markets/index/rusfar` | date; analytics/dates |
| 120 | [/761](https://iss.moex.com/iss/reference/761) | `/iss/statistics/engines/stock/markets/index/rusfar/attributes` | index/RUSFAR schema or attributes; route-specific date/lang |
| 121 | [/37](https://iss.moex.com/iss/reference/37) | `/iss/statistics/engines/[engine]/securitieslisting` | date, start, limit, lang, sectype, q, sort; cursor/dates/updated |
| 122 | [/231](https://iss.moex.com/iss/reference/231) | `/iss/sitenews` | start/lang as documented; cursor on collection route |
| 123 | [/229](https://iss.moex.com/iss/reference/229) | `/iss/sitenews/[news_id]` | single content item; no complex query arguments |
| 124 | [/553](https://iss.moex.com/iss/reference/553) | `/iss/events` | start/lang as documented; cursor on collection route |
| 125 | [/555](https://iss.moex.com/iss/reference/555) | `/iss/events/[event_id]` | single content item; no complex query arguments |
| 126 | [/13](https://iss.moex.com/iss/reference/13) | `/iss/statistics/engines/stock/markets/bonds/aggregates` | bond aggregate data/schema |
| 127 | [/19](https://iss.moex.com/iss/reference/19) | `/iss/statistics/engines/stock/markets/bonds/aggregates/columns` | bond aggregate data/schema |
| 128 | [/177](https://iss.moex.com/iss/reference/177) | `/iss/statistics/engines/stock/markets/index/analytics` | index analytics collection; inspect route reference for date/session filters |
| 129 | [/73](https://iss.moex.com/iss/reference/73) | `/iss/statistics/engines/stock/markets/index/analytics/[indexid]` | index/date analytics; inspect route-specific fields |
| 130 | [/141](https://iss.moex.com/iss/reference/141) | `/iss/statistics/engines/stock/markets/index/analytics/[indexid]/tickers` | date, tradingsession(1/2/3) |
| 131 | [/89](https://iss.moex.com/iss/reference/89) | `/iss/statistics/engines/stock/markets/index/analytics/[indexid]/tickers/[ticker]` | lang, from, till, tradingsession, start; cursor |
| 132 | [/105](https://iss.moex.com/iss/reference/105) | `/iss/statistics/engines/stock/capitalization` | type=daily\|monthly, date; online issuecapitalization block |
| 133 | [/527](https://iss.moex.com/iss/reference/527) | `/iss/history/engines/stock/totals/boards` | stock totals board directory |
| 134 | [/449](https://iss.moex.com/iss/reference/449) | `/iss/history/engines/stock/totals/securities` | date, start, tradingsession; cursor/dates |
| 135 | [/471](https://iss.moex.com/iss/reference/471) | `/iss/history/engines/stock/totals/boards/[board]/securities` | date, start, tradingsession; cursor/dates |
| 136 | [/509](https://iss.moex.com/iss/reference/509) | `/iss/history/engines/stock/totals/boards/[board]/securities/[security]` | from, till, start, tradingsession; cursor/dates |
| 137 | [/697](https://iss.moex.com/iss/reference/697) | `/iss/rms/engines/[engine]/objects/irr` | date, q, group/indicator/currencyid/instrument/isin<=5, start, limit; cursor/dates |
| 138 | [/621](https://iss.moex.com/iss/reference/621) | `/iss/rms/engines/[engine]/objects/settlementscalendar` | year, lang |
| 139 | [/681](https://iss.moex.com/iss/reference/681) | `/iss/rms/engines/[engine]/objects/[object] (limits)` | actual object hidden by generic route; date or instrument+from/till, start, limit=1000; cursor/dates |
| 140 | [/729](https://iss.moex.com/iss/reference/729) | `/iss/rms/engines/[engine]/objects/[object] (rclimits)` | actual object hidden by generic route; date or instrument+from/till, start, limit=1000; cursor/dates |
| 141 | [/657](https://iss.moex.com/iss/reference/657) | `/iss/rms/engines/[engine]/objects/[object] (staticparams)` | actual object hidden by generic route; date or instrument+from/till, start, limit=1000; cursor/dates |
| 142 | [/691](https://iss.moex.com/iss/reference/691) | `/iss/rms/engines/[engine]/objects/[object] (staticparamskeyterm)` | actual object hidden by generic route; date or instrument+from/till, start, limit=1000; cursor/dates |
| 143 | [/651](https://iss.moex.com/iss/reference/651) | `/iss/rms/engines/[engine]/objects/[object] (percentfutures)` | actual object hidden by generic route; date or instrument+from/till, start, limit=1000; cursor/dates |
| 144 | [/107](https://iss.moex.com/iss/reference/107) | `/iss/statistics/engines/state/rates` | state rates / column schema; inspect live metadata |
| 145 | [/97](https://iss.moex.com/iss/reference/97) | `/iss/statistics/engines/state/rates/columns` | state rates / column schema; inspect live metadata |
| 146 | [/71](https://iss.moex.com/iss/reference/71) | `/iss/statistics/engines/[engine]/derivatives/[report_name]` | report_name selects report; see statistics.md |
| 147 | [/91](https://iss.moex.com/iss/reference/91) | `/iss/statistics/engines/[engine]/monthly/[report_name]` | report_name selects report; see statistics.md |
| 148 | [/117](https://iss.moex.com/iss/reference/117) | `/iss/statistics/engines/currency/markets/fixing/[security]` | fixing/indicative-rate route; date or from/till depending route |
| 149 | [/25](https://iss.moex.com/iss/reference/25) | `/iss/statistics/engines/futures/markets/indicativerates/securities` | fixing/indicative-rate route; date or from/till depending route |
| 150 | [/63](https://iss.moex.com/iss/reference/63) | `/iss/statistics/engines/futures/markets/indicativerates/securities/[security]` | from, till, start/limit/sort as documented; history-style |
| 151 | [/5](https://iss.moex.com/iss/reference/5) | `/iss/statistics/engines/currency/markets/fixing` | fixing/indicative-rate route; date or from/till depending route |
| 152 | [/167](https://iss.moex.com/iss/reference/167) | `/iss/statistics/engines/[engine]/markets/[market]` | collateral repricing family; lang/date semantics by block |
| 153 | [/85](https://iss.moex.com/iss/reference/85) | `/iss/statistics/engines/[engine]/markets/[market]/securities` | collateral repricing securities by date |
| 154 | [/99](https://iss.moex.com/iss/reference/99) | `/iss/statistics/engines/[engine]/markets/[market]/securities/[security]` | collateral repricing single instrument: from, till, limit |
| 155 | [/559](https://iss.moex.com/iss/reference/559) | `/iss/referencedata/engines/[engine]/markets/all/securitieslisting` | date, start, limit, lang; cursor/dates |
| 156 | [/557](https://iss.moex.com/iss/reference/557) | `/iss/referencedata/engines/stock/markets/all/securities` | date, start, limit; cursor/dates (reference has limit-default inconsistency) |
| 157 | [/567](https://iss.moex.com/iss/reference/567) | `/iss/referencedata/engines/stock/markets/all/shorts` | date, start, limit; cursor/dates (reference has limit-default inconsistency) |
| 158 | [/569](https://iss.moex.com/iss/reference/569) | `/iss/referencedata/engines/futures/markets/[market]/risks` | date, start, limit<=1000; cursor/dates |
| 159 | [/563](https://iss.moex.com/iss/reference/563) | `/iss/referencedata/engines/futures/markets/[market]/params` | date, start, limit<=1000; cursor/dates |
| 160 | [/561](https://iss.moex.com/iss/reference/561) | `/iss/referencedata/engines/futures/markets/[market]/securities` | date, start, limit<=1000; cursor/dates |
| 161 | [/309](https://iss.moex.com/iss/reference/309) | `/iss/analyticalproducts/netflow2/securities` | entitlement-controlled; date |
| 162 | [/305](https://iss.moex.com/iss/reference/305) | `/iss/analyticalproducts/netflow2/securities/[security]` | entitlement-controlled; from,till; no normal pagination, max 1000 rows |
| 163 | [/307](https://iss.moex.com/iss/reference/307) | `/iss/analyticalproducts/futoi/securities` | entitlement-controlled; date, latest; dates |
| 164 | [/311](https://iss.moex.com/iss/reference/311) | `/iss/analyticalproducts/futoi/securities/[security]` | entitlement-controlled; from,till,latest; no normal pagination, max 1000 rows |
| 165 | [/299](https://iss.moex.com/iss/reference/299) | `/iss/history/statistics/markup/[markup_name]/[markup_type]` | from+till required, q, start, limit; cursor/columns; access may be product-controlled |
| 166 | [/297](https://iss.moex.com/iss/reference/297) | `/iss/statistics/markup/[markup_name]/[markup_type]/[markup_view]` | q, start, limit; cursor/columns; access may be product-controlled |
| 167 | [/237](https://iss.moex.com/iss/reference/237) | `/iss/sdfi/curves/[curveid]` | mixed SDFI entitlement; date |
| 168 | [/235](https://iss.moex.com/iss/reference/235) | `/iss/sdfi/curves` | SDFI curve directory; lang |

## Deliberately excluded CCI family

The live reference continues with `/iss/cci/**` corporate-information methods (companies, financial statements, ratings, affiliates, corporate information, actions and related datasets). MOEX describes CCI as a commercial information service with demo/contract/subscription access; unauthenticated information is unavailable. Because this skill is intended to route open/general ISS work, those methods are not copied here. If a user explicitly has CCI access, consult the current `/iss/cci/` reference and their entitlement list rather than relying on this skill snapshot.
