---
type: ml-current-context
status: active
updated: 2026-09-29
active_goal: ML-G01
active_task: ML-G01-T02
---

# Current ML context

This is the compact mentor resumption note for `D:\ML-project`. The learner works from the self-contained [LEARNING_MANUAL.md](LEARNING_MANUAL.md); the mentor checks this note, [PROGRESS.md](PROGRESS.md), and the active task.

## Active position

- Project: AI Capital Cycle Quantamental Research Engine.
- Public repository: [Shreyash3007/ai-capital-cycle-quantamental-research](https://github.com/Shreyash3007/ai-capital-cycle-quantamental-research).
- Publication state: T02 teaching setup and prior session notes are on public `main`; the learner-authored T01 named-output and current T02 baseline code remain local and uncommitted. This checkpoint records observed runs without claiming mastery.
- Mentor Mode: active; follow [MENTOR_MODE.md](MENTOR_MODE.md).
- Phase: P00, C1W2 first-principles valuation engine.
- Goal: [ML-G01 - C1W2 Valuation Stretch Foundation](Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/GOAL.md).
- Active teaching task: [ML-G01-T02 - Cost and Residuals](Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/T02%20-%20Cost%20and%20Residuals.md). The learner's baseline six-row cost and named residuals have run; see [the T02 session](Journey/2026-09-29-ML-G01-T02.md). Changed-target and guard tests are next.
- Earlier open task: [ML-G01-T01 - Vectorized Prediction](Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/T01%20-%20Vectorized%20Prediction.md). The saved script produced six named predictions and `Methods agree: True`; independent explanation and transfer remain open. Details are in [the T01 session](Journey/2026-09-28-ML-G01-T01.md).
- Learner lesson and next-action page: [LEARNING_MANUAL.md](LEARNING_MANUAL.md). Keep its current step and diagram aligned with this note and the progress ledger.
- Progress: T01 0%, T02 0%, phase 0%, overall 0% because no full explained acceptance check is closed; canonical ledger: [PROGRESS.md](PROGRESS.md).
- Assistance debt: T01 functions and guard, and T02's baseline cost function, received exact first-pass teaching. Each needs independent transfer before closure.
- Course coverage: Machine Learning Specialization C1W1 and C1W2 completed, learner-reported. C1W3 has not been confirmed. P00 uses C1W1 prediction, cost, and gradient descent as well as C1W2 methods. Later methods may be introduced early with a first-principles explanation, a bounded task, and a learner understanding check; this does not mark a course week or project capability complete.
- Next action: ask for the AstraCompute hand explanation and a sentence on what cost `0.017894916666666653` measures. Teach `.copy()` on unrelated delivery-time data, then have the learner independently change only CobaltAI's synthetic observed value from `2.400` to `2.200` in a copied array, predict the residual/cost direction, run, and confirm the original array is intact. Teach slicing on unrelated data before a deliberately short observed-array call that should trigger the guard. A labeled residual plot and independent transfer follow. T03 gradients and a cost curve follow T02. Do not silently write assignment code.

## Current research target

Build a multiple linear regression model from first principles that estimates a log valuation multiple from comparable-scale company fundamentals. The gap between observed and model-estimated valuation becomes a **valuation-stretch signal**.

The first feature set is intentionally small:

- revenue growth;
- gross margin;
- operating margin;
- free-cash-flow margin;
- research-and-development intensity.

The first dataset is synthetic and frozen. It exists to expose the mathematics and Python behavior without API, accounting, or revision noise.

The cross-phase [software engineering path](ENGINEERING_LEARNING_PATH.md) now includes folder roles and Python execution in P00, SQL in P01, APIs later, and an analyst workbench and system design defense in P07. Teach each layer when the active research task needs it; T01 does not need a database or server.

## P00 required outputs

- learner-written loop and vectorized predictions;
- learner-written squared-error cost;
- learner-written gradients and batch gradient descent;
- learner-written feature scaling with a convergence comparison;
- a financially justified feature-engineering experiment;
- equality checks between loop and vectorized implementations;
- cost-history and actual-versus-predicted plots;
- residual-based valuation-stretch view;
- tests on changed input and failure cases;
- an oral or written explanation of shapes, formulas, updates, limitations, and finance meaning.

## Important boundaries

- Before every new request to write or revise code, SQL, analysis, or design, give one worked example of the same type from different data or a different domain. For a first-time concept, give exact assignment lines in chat with a line-by-line explanation and let the learner type and run them. Record that pass as assisted; require an independent variation before mastery. This supersedes the previous hint-only rule by the learner's explicit 2026-09-29 request; follow [Mentor Mode](MENTOR_MODE.md).
- No `scikit-learn` model training in ML-G01.
- T01's six rows are only a shape and prediction exercise. A larger frozen fixture is required before training and no predictive claim follows from six rows and five features.
- No live API, Jev integration, backtest, trading rule, or bubble composite is part of ML-G01.
- A positive residual does not prove a bubble.
- The learner writes, executes, explains, and defends every assignment-code line. The mentor guides through questions, hints, examples, and observed runs without providing the active task's completed solution.
- The public learning record links [knowledge](KNOWLEDGE_GRAPH.md), [sessions](JOURNEY.md), [evidence](Evidence/README.md), [progress](PROGRESS.md), and reviewed Git commits. Course PDFs remain local and excluded from publication.

## Canonical decisions

- Static first, frozen historical snapshots second, live adapters third.
- Live use initially means a live paper portfolio, not real-money execution.
- Numeric models calculate; TypeSafe/Jev later provides narrow typed semantic judgments; a generative model later explains already-computed evidence.
- Confidence is separated into data quality, statistical reliability, semantic confidence, and timing uncertainty.
- The finished product is for quant researchers, systematic equity analysts, finance ML engineers, AI evaluation engineers, and MFE-style academic review.
- The finished product is an output-oriented quantamental research engine, not a dashboard. Its valuable artifacts are versioned signals, model evidence, company and segment dossiers, event studies, fragility reports, and paper-portfolio attribution.
- The public universe is segmented by economic role in the AI capital cycle. OpenAI and Anthropic remain private ecosystem nodes unless and until they complete public listings.

## Evidence state

The learner's guarded loop and vectorized functions produced the same six named values in the saved script, including AstraCompute `2.6870000000000003` (ordinary floating-point rounding), and `Methods agree: True`. Changed-input and intentional shape-failure runs were also observed. This remains assisted T01 evidence with independent transfer and interpretation open. T02's saved arrays both have shape `(6,)`; the first error `-0.113`, squared error `0.012769`, residual `+0.113`, six-row cost `0.017894916666666653`, and six named residuals reran correctly. This is assisted baseline evidence. The learner has not yet supplied a hand explanation, changed-target run, guard failure, or plot. After each meaningful learner attempt, update the task and progress record, then refresh this note last.
