# Data and live-system design

## Why static comes first

Live data adds authentication, rate limits, revisions, missing fields, schema changes, and timing ambiguity. Those problems can hide whether the learner actually understands the model.

The project therefore uses this order:

1. **Synthetic frozen data:** expose shapes, formulas, and Python behavior.
2. **Frozen historical snapshot:** introduce real accounting and market meaning while preserving reproducibility.
3. **Provider adapters:** fetch data and immediately store an immutable snapshot.
4. **Scheduled live research:** calculate features from snapshots, run models, and monitor a paper portfolio.

Models never train directly against a moving API response.

## Planned data domains

| Domain | Examples | Main risks |
|---|---|---|
| Prices and volume | adjusted close, returns, volatility, turnover | corporate actions, missing sessions, vendor adjustments |
| Fundamentals | revenue, margins, cash flow, R&D, shares, debt | filing dates, restatements, units, quarterly versus trailing values |
| Valuation | enterprise value, sales, earnings, free-cash-flow multiples | negative denominators, stale market cap, peer definition |
| Filings and calls | 10-K, 10-Q, 8-K, earnings-call text | publication timestamp, amendments, source linking |
| Macro and funding | rates, spreads, liquidity proxies | release lags, revisions, frequency mismatch |
| Universe | AI exposure, sector, geography, listing status | survivorship bias, changing classification |

## Likely public sources

- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) for company submissions and XBRL company facts.
- [FRED API](https://fred.stlouisfed.org/docs/api/fred/series_observations.html) for macroeconomic series; an API key is required.
- [Alpha Vantage documentation](https://www.alphavantage.co/documentation/) as one possible market-data adapter, subject to current free-tier limits and licensing.

These are candidates, not a promise that every required field is free. Provider terms, rate limits, coverage, timestamps, and redistribution rights must be checked before integration.

## Snapshot contract

Every raw snapshot should eventually record:

```text
snapshot_id
source_name
source_url_or_request
entity_id
as_of
fetched_at
available_from
revision_or_filing_id
schema_version
content_hash
raw_payload_path
```

`as_of` means the period or market date described by the data. `available_from` means the earliest time the research system was allowed to know it. These are not interchangeable.

## Point-in-time rules

- Join features using `available_from`, not only fiscal-period end.
- Preserve amended filings instead of overwriting earlier knowledge.
- Use universe membership known at the observation date.
- Adjust price history consistently and document the adjustment source.
- Fit scalers and model parameters on training periods only.
- Never use a future label, future filing, or revised future value in a historical feature.
- Keep raw, normalized, feature, prediction, and report layers separately versioned.

## Live operating loop

The first live system will:

1. fetch permitted sources;
2. save immutable raw snapshots;
3. validate freshness, schema, units, and missingness;
4. build point-in-time features;
5. run versioned models and semantic judgments;
6. write prediction and confidence records;
7. update the live paper portfolio;
8. render monitoring and research reports;
9. alert on stale data, failed checks, drift, or uncertain judgments.

## Failure policy

Stale, missing, ambiguous, or low-confidence data should lower data confidence or block a downstream action. The system must never silently replace missing evidence with an apparently precise value.

## Stage 0 data

ML-G01 uses a hand-readable frozen matrix of ratio features and a target representing a log valuation multiple. Feature names, units, shapes, and target meaning must be printed and explained before model training begins.
