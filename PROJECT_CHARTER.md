# Project charter

## Working name

**AI Capital Cycle Quantamental Research Engine**

## Mission

Build an institutional-style quantamental research engine that measures value creation, embedded expectations, market behavior, financing conditions, and narrative evidence across the public AI capital cycle. The system should help a skilled analyst distinguish:

- expensive but fundamentally supported growth;
- temporary valuation stretch;
- speculative price behavior;
- financing or liquidity fragility;
- narrative claims that are weakly supported by disclosed evidence;
- conditions under which the current state could improve or break.

The project is both a learning vehicle and a serious research artifact. Every added technique must have a financial reason, a measurable evaluation, a professional output, and an honest limitation.

## Intended audience

- quantitative researchers;
- systematic equity analysts;
- finance-focused ML engineers;
- AI evaluation engineers;
- technically strong investment researchers.

It is not designed as a beginner stock picker, a generic consumer dashboard, an AI chat wrapper, or an automatic buy/sell oracle.

## Core outputs

For each company, universe, and observation date, the mature platform should produce:

1. **Fundamental state:** growth, margins, cash generation, investment intensity, and balance-sheet condition.
2. **Valuation state:** absolute valuation, peer-relative valuation, and model-estimated valuation stretch.
3. **Market state:** momentum, volatility, liquidity, turnover, concentration, and price explosiveness.
4. **Narrative state:** typed, source-linked judgments about disclosed AI demand, monetization, capacity constraints, competitive risk, and management claims.
5. **Bubble and fragility profile:** dimension scores, pro-bubble evidence, counter-evidence, triggers, and scenario horizons.
6. **Confidence profile:** data, statistical, semantic, and timing uncertainty shown separately.
7. **Portfolio research:** paper-only signals, costs, turnover, drawdowns, exposures, and failure analysis.
8. **Research explanation:** a concise evidence-backed narrative that never invents calculations or sources.
9. **Machine-readable signal book:** versioned observations, horizons, mechanisms, confidence, evidence, and failure conditions.
10. **Professional research artifacts:** company dossiers, segment reports, model cards, event studies, rejected-signal memos, and portfolio postmortems.

## Research universe

The first serious universe will contain public companies segmented by role in the AI capital cycle: compute, foundry and equipment, networking and power, specialized cloud, hyperscalers, and enterprise applications. Private labs such as OpenAI and Anthropic are ecosystem nodes, not listed securities. Membership and segmentation must be versioned through time to reduce survivorship bias. See [UNIVERSE_AND_SEGMENTATION.md](UNIVERSE_AND_SEGMENTATION.md).

## What excellence means

The project should demonstrate that its author can:

- implement core algorithms from first principles and explain their mathematics;
- write clear Python with explicit shapes, contracts, tests, and failure handling;
- understand company filings, valuation multiples, cash flow, capital intensity, and market microstructure limitations;
- construct point-in-time features without look-ahead leakage;
- compare simple baselines with more complex models;
- evaluate with walk-forward and out-of-sample procedures;
- distinguish model fit from economic usefulness;
- calibrate uncertainty instead of hiding it inside one score;
- use AI as a controlled research component rather than a source of untraceable authority;
- operate a reproducible live paper-research loop.
- formulate and reject hypotheses without hiding negative results;
- defend the full chain from accounting source to signal and portfolio consequence under professional questioning.

## Non-goals

- predicting an exact crash date;
- claiming causation from correlation or a model residual;
- maximizing a backtest by trying many hidden variations;
- using an LLM to perform deterministic finance arithmetic;
- treating model confidence as truth;
- adding deep learning merely to make the system look advanced;
- real-money execution without a new explicit authorization and separate risk design;
- completing the entire platform in one week.

## One-week commitment

The first phase targets a narrow but deep research kernel using the full C1W2 boundary. It will calculate a valuation-stretch signal from learner-written multiple linear regression, cost, gradient descent, vectorization, scaling, and feature engineering, then visualize and explain the result. The original one-week schedule remains a target; the evidence gate determines completion.

The long-term charter remains ambitious. The first delivery remains honest.

Mentor Mode and progress accounting live in [MENTOR_MODE.md](MENTOR_MODE.md) and [PROGRESS.md](PROGRESS.md). The learner reports completing C1W1 and C1W2, while project implementation remains at 0% until demonstrated.

## Final acceptance standard

The long-term platform is portfolio-ready only when it includes:

- versioned price, fundamental, macro, filing, and semantic datasets;
- transparent naive and statistical baselines;
- at least three justified model families, each compared against simpler baselines;
- point-in-time walk-forward evaluation;
- bubble, fragility, and counter-evidence analysis;
- evaluated TypeSafe semantic features on a labeled set;
- paper strategies with transaction costs, turnover, concentration, and drawdown controls;
- a live paper portfolio with monitoring and immutable snapshots;
- model cards, data documentation, evaluation reports, and failure postmortems;
- machine-readable signal and attribution products;
- professional company, segment, model, event, fragility, and portfolio reports;
- optional inspection tooling that never owns the research logic.
