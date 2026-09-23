# Signal research program

## Purpose

The engine should produce repeatable research artifacts that can be inspected, falsified, and used in a disciplined paper-investment process. A signal is admitted only after its financial meaning, data lineage, statistical evidence, and failure behavior are documented.

## Signal contract

Every signal record should eventually contain:

```text
signal_id
entity_id
observation_date
available_from
signal_family
raw_value
normalized_value
direction
horizon
economic_mechanism
model_or_rule_version
data_snapshot_ids
confidence_vector
evidence_ids
known_failure_conditions
created_at
```

A bare score without this context is not a professional research output.

## Research sequence for every signal

1. **State the hypothesis.** Define the mechanism and expected direction before measuring performance.
2. **Define the observation.** Fix entity, timestamp, feature availability, target, and horizon.
3. **Build a naive baseline.** Use a mean, last value, simple multiple, or transparent rule.
4. **Implement the simplest model.** Start with interpretable statistics or ML.
5. **Design the test.** Use time-aware splits, costs, and an untouched period.
6. **Inspect failures.** Study regimes, segments, outliers, missing data, and counterexamples.
7. **Stress the result.** Change reasonable definitions, lags, weights, windows, and costs.
8. **Decide.** Promote, revise, quarantine, or reject the signal.
9. **Monitor.** Track drift, calibration, data quality, and realized paper outcomes.

Negative results remain in the research record.

## Priority research programs

### Program 1: valuation stretch

Estimate a conditional valuation anchor from point-in-time fundamentals. Study residual stability, omitted-variable explanations, and later returns without calling the residual mispricing by default.

### Program 2: fundamental delivery

Measure changes in revenue, margins, cash conversion, backlog, guidance, and capital intensity relative to prior expectations. Separate level, change, surprise, and acceleration.

### Program 3: AI capital efficiency

Relate incremental AI-oriented capex or investment to later revenue, gross profit, operating profit, and free cash flow. Account for long lags, depreciation, utilization, and segment disclosure limitations.

### Program 4: narrative-evidence divergence

Measure whether the strength and specificity of AI claims move with disclosed operating evidence. TypeSafe/Jev may create narrow semantic features after labeled evaluation; language models may extract source-linked claims under a strict schema.

### Program 5: event response

Study earnings, guidance, product launches, financing, capacity, customer, regulatory, and supply events. Estimate abnormal return, volatility, dispersion, and persistence using declared event windows and controls.

### Program 6: bubble and fragility

Combine valuation, price, fundamental, narrative, funding, crowding, and macro dimensions without erasing them. Report intensity, counter-evidence, triggers, and calibrated event horizons separately.

### Program 7: paper portfolio

Convert only promoted signals into versioned paper rules. Measure attribution, exposure, turnover, costs, liquidity, concentration, drawdown, and performance decay. Compare with equal-weight and factor-controlled baselines.

## Machine-readable outputs

- `universe_snapshot`: membership and segment at each date;
- `fundamentals_point_in_time`: normalized accounting data and availability;
- `features`: model-ready features with lineage;
- `semantic_judgments`: typed answers, probabilities, rubric, and evidence;
- `predictions`: target, horizon, estimate, and uncertainty;
- `signals`: versioned research signals;
- `events`: defined catalysts and event-study results;
- `paper_positions`: hypothetical positions and construction metadata;
- `attribution`: return, factor, cost, and risk contributions.

Parquet or another typed columnar format becomes the default when real data begins; small CSV files remain acceptable for transparent teaching fixtures.

## Human-readable outputs

- company quantamental dossier;
- segment and AI capital-cycle report;
- signal research memo;
- model card and evaluation report;
- earnings or catalyst event note;
- bubble and fragility report;
- paper-portfolio review;
- failure postmortem and rejected-signal log.

Every report links back to machine-readable records and source evidence.

## Promotion gates

A signal cannot enter the paper portfolio until it has:

- a stable definition and economic mechanism;
- point-in-time data lineage;
- a relevant baseline;
- walk-forward or otherwise valid out-of-sample evidence;
- sensitivity and failure analysis;
- multiple-testing disclosure;
- transaction-cost and exposure analysis where relevant;
- a versioned implementation;
- a written reason for promotion.

Promotion is reversible. A signal is quarantined when data changes, calibration deteriorates, the mechanism weakens, or implementation integrity is uncertain.
