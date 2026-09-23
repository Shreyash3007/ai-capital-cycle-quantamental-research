# Master development roadmap

## How phases advance

The project advances through evidence-backed phases. Future methods are visible here and may be taught early when a task needs them. Mentor Mode first explains the prerequisite, checks understanding, and then assigns a bounded implementation. Course completion stays separate from project evidence. Every task begins with what we are building, why it matters, and what output it will produce. Every task ends with execution, changed-input testing, failure diagnosis, explanation, and progress updates.

**Learning sequence:** tiny synthetic calculation -> learner-written Python -> multi-feature model -> frozen real-world data -> tested signals -> AI evidence -> fragility research -> paper portfolio -> live paper research. Each phase starts with the smallest useful example and grows through working checkpoints. Professional depth is the end state, not the first exercise. [Mentor Mode](MENTOR_MODE.md) owns pace and help; [P00 plan](PHASE_00_C1W2_PLAN.md) owns the current difficulty ladder.

## P00: C1W2 first-principles valuation engine

**Weight:** 10%. **State:** active. **Known course coverage:** C1W2 completed, learner-reported.

Build prediction, cost, gradients, batch gradient descent, feature scaling, convergence diagnostics, feature engineering, and a limited valuation-stretch output from scratch.

Tasks: T01 loop and vectorized prediction; T02 cost and residual meaning; T03 gradients and gradient descent; T04 scaling and convergence; T05 feature engineering and nonlinear terms; T06 integrated output and independent defense.

Detailed plan: [PHASE_00_C1W2_PLAN.md](PHASE_00_C1W2_PLAN.md).

## P01: Point-in-time finance and data foundation

**Weight:** 12%. **State:** planned. **Gate:** P00 evidence plus the Python and data handling needed for reliable ingestion.

Build the accounting and data layer. The mentor writes each detailed brief when the preceding task reveals what the learner needs.

| Task | Build | Output |
|---|---|---|
| P01-T01 | Versioned company universe and segment rules | membership file with inclusion evidence and dates |
| P01-T02 | Frozen SEC filing and company-facts loader | immutable snapshot plus source manifest |
| P01-T03 | Accounting normalization and filing availability | reconciled company-quarter records |
| P01-T04 | Fundamental features with unit and missingness checks | point-in-time feature table |
| P01-T05 | Independent source-to-feature audit | data-quality report and defended sample rows |

**Output:** a reviewer can trace every important feature to its source and formula. This phase starts with frozen data and introduces any new technique through a first-principles lesson.

## P02: Quantitative market and econometric research

**Weight:** 14%. **State:** planned. **Gate:** P01 and the required statistics or time-series foundations taught from first principles.

Build the quantitative market research layer in this order:

| Task | Build | Output |
|---|---|---|
| P02-T01 | Adjusted-return and risk calculations | checked return, volatility, and drawdown series |
| P02-T02 | Market, sector, and segment baseline model | factor and residual-return report |
| P02-T03 | Event definitions and abnormal-return study | source-linked event study with declared windows |
| P02-T04 | Point-in-time panel and rolling evaluation | time-aware research dataset and split manifest |
| P02-T05 | Robustness and multiple-testing audit | sensitivity report with rejected findings |

**Output:** validated descriptive and econometric evidence with declared assumptions. A method beyond confirmed course coverage receives its own explanation and understanding check.

## P03: Supervised ML signal research

**Weight:** 16%. **State:** planned. **Teaching dependency:** C1W3 and relevant C2 concepts must be explained and demonstrated before use if their course weeks are not yet completed.

Develop supervised models in course order:

| Task | Build | Output |
|---|---|---|
| P03-T01 | Event label, horizon, base rate, and naive baseline | target specification and baseline report |
| P03-T02 | Logistic model and regularization | from-scratch and library-checked classification evidence |
| P03-T03 | Development diagnostics and error slices | learning curves and failure analysis |
| P03-T04 | Tree and ensemble comparison | walk-forward benchmark with ablations |
| P03-T05 | Probability calibration and signal promotion review | model card and promote/reject decision |

**Output:** promoted or rejected supervised signals with valid out-of-sample evidence.

## P04: AI evidence and deep-learning research

**Weight:** 12%. **State:** planned. **Teaching dependency:** appropriate C2/C3 and later deep-learning concepts must be explained and demonstrated before use if their course weeks are not yet completed.

Develop semantic evidence and later deep models in tested increments:

| Task | Build | Output |
|---|---|---|
| P04-T01 | Source-linked filing and transcript corpus | excerpt records with publication times |
| P04-T02 | Rubric and labeled semantic set | adjudicated examples and difficult counterexamples |
| P04-T03 | Deterministic text baseline and TypeSafe/Jev experiment | accuracy, calibration, and abstention report |
| P04-T04 | Structured LLM extraction and evidence-constrained explanation | audited claim records and unsupported-claim tests |
| P04-T05 | Retrieval and representation comparison | baseline versus embedding or deep-model evaluation |
| P04-T06 | Drift and operational failure audit | versioned semantic feature decision |

**Output:** evaluated semantic features and constrained explanations.

## P05: Bubble, catalyst, and fragility system

**Weight:** 12%. **State:** dependency-gated. **Gate:** reliable fundamental, market, and semantic evidence.

Build the fragility system from components before combining them:

| Task | Build | Output |
|---|---|---|
| P05-T01 | Reverse valuation and expectations gap | assumption and sensitivity tables |
| P05-T02 | Fundamental delivery and AI capital efficiency | segment-aware measures and counterexamples |
| P05-T03 | Price, crowding, funding, and macro dimensions | separate fragility records |
| P05-T04 | Narrative divergence and counter-evidence | source-linked competing thesis |
| P05-T05 | Catalyst paths and horizon event study | conditional trigger map and calibrated probabilities if supported |
| P05-T06 | Composite sensitivity and independent review | bubble and fragility research report |

**Output:** a report with dimensions, triggers, counter-thesis, and separate uncertainty components.

## P06: Portfolio construction and signal book

**Weight:** 14%. **State:** dependency-gated. **Gate:** at least one promoted signal with stable out-of-sample evidence.

Test research against portfolio constraints:

| Task | Build | Output |
|---|---|---|
| P06-T01 | Signal promotion and append-only signal book | dated signals with evidence and version |
| P06-T02 | Paper mapping, constraints, and exposure controls | dated hypothetical positions |
| P06-T03 | Cost, liquidity, slippage, and borrow assumptions | gross-to-net return bridge |
| P06-T04 | Risk and performance attribution | company, segment, factor, and cost decomposition |
| P06-T05 | Stress, alternative rules, and signal retirement | portfolio research memo and postmortem |

**Output:** reproducible paper positions and performance attribution.

## P07: Live paper research and final defense

**Weight:** 10%. **State:** dependency-gated. **Gate:** P01-P06 acceptance and operational readiness.

Operate and defend the full loop:

| Task | Build | Output |
|---|---|---|
| P07-T01 | Provider adapters and immutable snapshots | versioned live data with health checks |
| P07-T02 | Scheduled validation, features, inference, and reports | repeatable research run with failure recovery |
| P07-T03 | Live paper portfolio and monitoring | dated positions, attribution, staleness, and drift alerts |
| P07-T04 | Company and segment research publication | reproducible dossiers with counter-theses |
| P07-T05 | Final technical paper and professional defense | source-to-signal reproduction and oral review record |

**Output:** a reproducible live paper-research record and defensible final body of work.

## Progress accounting

Phase weights and evidence-backed completion live in [PROGRESS.md](PROGRESS.md). Course speed, hours worked, document count, and visual polish do not add completion credit.
