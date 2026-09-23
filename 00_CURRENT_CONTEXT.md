---
type: ml-current-context
status: active
updated: 2026-09-23
active_goal: ML-G01
active_task: ML-G01-T01
---

# Current ML context

This is the compact resumption note for `D:\ML-project`. Start with [HOME.md](HOME.md) for navigation, then read this note, [PROGRESS.md](PROGRESS.md), and the active task.

## Active position

- Project: AI Capital Cycle Quantamental Research Engine.
- Public repository: [Shreyash3007/ai-capital-cycle-quantamental-research](https://github.com/Shreyash3007/ai-capital-cycle-quantamental-research).
- Mentor Mode: active; follow [MENTOR_MODE.md](MENTOR_MODE.md).
- Phase: P00, C1W2 first-principles valuation engine.
- Goal: [ML-G01 - C1W2 Valuation Stretch Foundation](Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/GOAL.md).
- Task: [ML-G01-T01 - Vectorized Prediction](Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/T01%20-%20Vectorized%20Prediction.md).
- Task state: ready; no learner attempt has been observed.
- Progress: task 0%, phase 0%, overall 0%; canonical ledger: [PROGRESS.md](PROGRESS.md).
- Assistance debt: none.
- Course coverage: Machine Learning Specialization C1W2 completed, learner-reported. C1W3 has not been confirmed. Later methods may be introduced early with a first-principles explanation, a bounded task, and a learner understanding check; this does not mark a course week or project capability complete.
- Next action: run the task's short calibration, then make the learner's cold attempt in `Projects/AI Capital Cycle Quantamental Research Engine/src/01_vectorized_prediction.py`.

## Current research target

Build a multiple linear regression model from first principles that estimates a log valuation multiple from comparable-scale company fundamentals. The gap between observed and model-estimated valuation becomes a **valuation-stretch signal**.

The first feature set is intentionally small:

- revenue growth;
- gross margin;
- operating margin;
- free-cash-flow margin;
- research-and-development intensity.

The first dataset is synthetic and frozen. It exists to expose the mathematics and Python behavior without API, accounting, or revision noise.

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

All project capability is currently **planned**. Documentation, Mentor Mode, and the empty learner file exist, but no ML-G01 implementation or mastery has been demonstrated. After each task, record observed checks in `PROGRESS.md`, then refresh this note last.
