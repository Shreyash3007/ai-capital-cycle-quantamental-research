# Phase P00: C1W2 first-principles valuation engine

## Phase purpose

Build a complete multiple-linear-regression research kernel by hand and use it to produce a carefully limited valuation-stretch output. This phase turns completed C1W1-C1W2 course coverage into demonstrated Python, mathematics, ML, and finance capability.

## What this phase produces

- transparent loop and vectorized predictions;
- learner-written cost and gradient calculations;
- batch gradient descent with convergence diagnostics;
- feature scaling implemented and explained;
- financially reasoned feature engineering and nonlinear terms;
- actual-versus-predicted and residual research outputs;
- an independent final defense and transfer test.

The phase does not claim that the model predicts returns or proves a bubble.

## Task sequence

### ML-G01-T01: Loop and vectorized prediction

**Build:** prediction functions using explicit loops and `np.dot`.

**Why:** connect the multiple-regression formula to array shapes and Python execution.

**Output:** matching predictions on original and changed data plus a diagnosed shape failure.

### ML-G01-T02: Cost function and residual meaning

**Build:** squared-error cost from the formula and a residual table.

**Why:** understand exactly what the model minimizes and what an error means financially.

**Output:** hand-verified cost, learner implementation, changed target test, and residual interpretation.

### ML-G01-T03: Gradients and batch gradient descent

**Build:** parameter derivatives and simultaneous update logic.

**Why:** understand how optimization changes every weight and bias rather than treating training as a library call.

**Output:** hand-traced update, decreasing cost history, trained parameters, and one diagnosed bad learning rate. Use a larger frozen teaching fixture than T01's six rows so the training exercise does not imply that six observations support a five-feature valuation claim.

### ML-G01-T04: Feature scaling and convergence

**Build:** training-only mean normalization or z-score scaling, then compare convergence.

**Why:** show how feature scale changes the optimization path without changing the economic variable's meaning.

**Output:** scaler parameters, transformed features, before-and-after convergence evidence, and leakage explanation.

### ML-G01-T05: Feature engineering and nonlinear terms

**Build:** one financially justified transformed or interaction feature and one polynomial experiment.

**Why:** test whether the linear model can represent a plausible nonlinear financial relationship while controlling complexity.

**Output:** written hypothesis, engineered feature, baseline comparison, residual change, and overfitting warning.

### ML-G01-T06: Quantamental output and independent defense

**Build:** a reproducible valuation-stretch research artifact from a fresh frozen fixture.

**Why:** integrate Python, linear algebra, calculus, optimization, visualization, and finance interpretation without step-by-step rescue.

**Output:** signal table, diagnostic figures, short research note, failure analysis, and oral or written defense.

## Phase acceptance gate

P00 completes only when the learner can independently:

- define all variables, shapes, units, and transformations;
- derive prediction, cost, and gradient formulas;
- implement loop and vectorized forms;
- explain simultaneous gradient-descent updates;
- diagnose scaling and learning-rate behavior;
- justify engineered features economically;
- run original, changed, and failure cases;
- distinguish fit, valuation stretch, mispricing, and bubble claims;
- reproduce the integrated result on a fresh fixture;
- explain every learner-owned code block under questioning.

The six-row T01 fixture is only for checking array mechanics. With five features plus a bias, it cannot support a credible estimate of generalization. Later phase tasks need more observations, a baseline, and an honest train/test design before any predictive claim.

## Current boundary

P00 is designed around confirmed C1W2 coverage. A later method may be introduced early under [Mentor Mode](MENTOR_MODE.md), but it does not replace the current from-scratch regression gate or imply that the later course week is complete.

## Phase progress

See [PROGRESS.md](PROGRESS.md). Current phase completion is **0%** because the active task is ready but has not been attempted.
