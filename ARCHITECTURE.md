# Architecture

## Design principle

The system is a research pipeline with inspectable boundaries. Each module should hide internal complexity behind a small interface and return data rather than directly controlling the next module.

The architecture grows in stages. We do not create provider, model, or deployment abstractions before there are at least two real implementations that need them.

## Target data flow

```text
source adapters
    -> immutable raw snapshots
    -> point-in-time normalization
    -> feature tables
    -> numeric models + semantic judgments
    -> calibrated research signals
    -> bubble/fragility scenarios
    -> paper portfolio and monitoring
    -> evidence-linked research artifacts and paper attribution
    -> read-only research API and analyst workbench
```

## Modules

### 1. Source adapters

Fetch or load prices, filings, company facts, macro series, and later textual evidence. The adapter returns raw source records plus metadata. It does not calculate investment signals.

### 2. Snapshot store

Persists exactly what was known at fetch time. A snapshot records source, request, `as_of`, `fetched_at`, version, and revision information when available.

### 3. Normalization

Converts provider-specific names and units into a stable schema. It records transformations and rejects ambiguous values instead of guessing.

### 4. Point-in-time feature engine

Creates numeric features using only information available on the observation date. Finance formulas live here as deterministic code with unit tests.

### 5. Numeric model lab

Trains, evaluates, and compares transparent and complex models. It returns predictions, parameters, diagnostics, and metadata. It does not write narrative explanations.

### 6. Semantic judgment adapter

Later sends source-linked text states to TypeSafe/Jev for narrow typed judgments. It returns primitive answers, probability distributions, model version, and request metadata.

### 7. Signal and confidence engine

Combines evaluated inputs using versioned rules. Numeric calculations stay in code. Separate confidence components remain separate.

### 8. Bubble and fragility engine

Builds dimension scores, pro-bubble evidence, counter-evidence, and conditional scenarios. It never emits an unsupported exact burst date.

### 9. Research explanation

Creates a readable explanation from already-calculated, source-linked evidence. Generated text may summarize; it may not silently invent a number, source, or conclusion.

### 10. Paper portfolio and monitoring

Evaluates hypothetical decisions, costs, turnover, exposure, drawdown, and drift. It does not place real orders.

### 11. Research artifact publisher

Writes versioned signal tables, model cards, company dossiers, segment reports, event studies, fragility reports, and paper-portfolio attribution. Each important claim links to its source and calculation.

### 12. Research delivery

A later read-only API serves versioned artifacts to a small analyst workbench. The interface lets a reviewer trace a signal to its data, model, counter-evidence, and paper consequence. It does not calculate a signal or replace the saved research artifact. The learner builds and tests this layer in P06-P07 after the research contracts exist.

## Current Stage 0 architecture

Only four pieces exist conceptually in ML-G01:

```text
small frozen NumPy fixture
    -> vectorized prediction
    -> cost and gradient descent
    -> saved diagnostic plots
```

The learner will initially keep this in a small number of numbered scripts so every line is visible. Modules will be extracted only after repetition reveals a real shared responsibility.

The staged software structure and full-stack learning path are in [ENGINEERING_LEARNING_PATH.md](ENGINEERING_LEARNING_PATH.md). No database, API, or frontend belongs in T01.

## Stable interfaces to aim for later

Examples below describe contracts, not current implementation:

```text
load_snapshot(snapshot_id) -> RawSnapshot
build_features(raw_snapshot, observation_date) -> FeatureTable
fit(model_spec, train_table) -> FittedModel
predict(fitted_model, feature_table) -> PredictionTable
judge_semantics(evidence_bundle) -> SemanticJudgmentSet
build_bubble_profile(signal_set) -> BubbleProfile
render_report(research_state) -> ResearchReport
```

## Dependency rules

- Source and model code do not depend on optional presentation code.
- Finance calculations do not call an LLM.
- Model training does not fetch live endpoints.
- Explanations consume recorded results; they do not recompute them.
- Paper portfolio logic consumes versioned signals; it does not access future data.
- Credentials never enter notebooks, data snapshots, prompts, or committed files.
