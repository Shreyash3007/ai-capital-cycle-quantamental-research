---
type: task
id: ML-G01-T01
goal: ML-G01
status: ready
challenge_level: foundation-to-stretch
evidence_status: planned
updated: 2026-09-23
---

# ML-G01-T01: Vectorized prediction

## Central difficulty

Start with one feature and two company rows. Grow that working calculation into loop and vectorized predictions for a five-feature table, keeping the meaning and shape of every value clear.

This task does not implement cost or gradient descent. Those remain separate tasks so the tutor can see whether vectorization itself is understood.

## Before you build

**What:** calculate two predictions by hand, write them in Python, and then extend the same logic to more features and companies.

**Why:** the same calculation must make sense as a finance row, a mathematical dot product, and executing Python code.

**What you get:** several small working runs, a checked five-feature prediction table, and one explained shape error. This becomes the base for cost and gradient descent.

## Working file

`../../Projects/AI Capital Cycle Quantamental Research Engine/src/01_vectorized_prediction.py`

The file is intentionally empty. The learner writes every implementation line.

## Finance setup

First checkpoint: use only **revenue growth** for two fictional companies. The trial weight is `2.0` and the bias is `1.0`. These are supplied numbers, not learned parameters.

| Company | Revenue growth |
|---|---:|
| AstraCompute | 0.20 |
| NexaCloud | 0.40 |

Work out each prediction on paper before coding. Represent this as a two-row, one-feature matrix when you reach NumPy. First make one prediction work, then both rows, then compare loop and vectorized results.

Second checkpoint: add **gross margin** as a second feature for those two rows, using values `0.72` and `0.68` and trial weights `[2.0, 0.5]`. Keep the bias at `1.0`. Explain what changed in the shapes and in each row's calculation.

Final checkpoint: use this five-feature synthetic universe. Each row represents a company observation. The comparable-scale ratio features are, in order:

1. revenue growth;
2. gross margin;
3. operating margin;
4. free-cash-flow margin;
5. R&D intensity.

The target used later is a log valuation multiple. This task only predicts from supplied trial weights and a bias.

Use this frozen synthetic fixture only after the small checkpoints work. The names do not represent real companies.

| Company | Revenue growth | Gross margin | Operating margin | FCF margin | R&D intensity |
|---|---:|---:|---:|---:|---:|
| AstraCompute | 0.55 | 0.72 | 0.28 | 0.25 | 0.18 |
| NexaCloud | 0.40 | 0.68 | 0.22 | 0.20 | 0.16 |
| VertexChips | 0.65 | 0.75 | 0.35 | 0.32 | 0.21 |
| ModelWorks | 0.30 | 0.62 | 0.12 | 0.08 | 0.25 |
| DataForge | 0.25 | 0.58 | 0.15 | 0.14 | 0.12 |
| CobaltAI | 0.50 | 0.65 | 0.05 | -0.02 | 0.40 |

For the five-feature fixture, use trial parameters `w = [1.2, 0.8, 1.0, 0.9, -0.3]` and `b = 1.0`. These are supplied inputs, not learned parameters. Their economic signs are not a validated valuation claim.

Read [DATA_DICTIONARY.md](../../DATA_DICTIONARY.md) for the feature and shape contracts.

## Calibration before coding

For the first two-row, one-feature checkpoint, answer briefly without searching:

1. If each row is a company and the only feature is revenue growth, what should one predicted number represent?
2. What are the shapes of `X`, `w`, and the two predictions?

The answers diagnose readiness; they are not graded as the task itself. The mentor explains any gap quickly, then you write and run the first small step.

## Learner challenge

Write the implementation yourself, one checkpoint at a time. Start with the two-row, one-feature calculation. Add the loop, then the vectorized form, checking the output after each step. Extend to two features, then the full fixture. Show shapes and per-company results and check loop/vectorized agreement within a stated floating-point tolerance. Change one input and repeat the check.

Choose names that express finance meaning. Avoid shadowing Python built-ins such as `sum` and `list`.

## Required prediction before run

Before each new checkpoint's first run, write down:

- the expected output shape;
- one hand-calculated row prediction for that checkpoint;
- once both versions exist, whether they should match exactly or within floating-point tolerance.

## Required failure experiment

After the correct five-feature run, intentionally create one incompatible weight shape, run it, and read the error. Then restore the correct shape and explain what dimension failed to align.

## Acceptance and task progress

Each passed and explained check contributes 20 percentage points to T01. The mentor records evidence for each check in `PROGRESS.md`. A result that runs but cannot be explained remains open.

1. The two-row, one-feature shapes and hand predictions are correct and explained.
2. A learner-written loop returns both starter predictions.
3. A learner-written vectorized version agrees with the loop on the starter data.
4. Both versions agree after the move to two features, then five features, and after a changed row or weight.
5. The incompatible-shape failure is diagnosed and repaired; the learner explains what the predictions mean and why they are not yet a valuation conclusion.

## Tutor behavior

Start with the calibration and cold attempt. Follow [Mentor Mode](../../MENTOR_MODE.md) for explanation, help, code review, and the solution boundary.

## Completion evidence

Record the exact command, outputs, changed input, shape error, learner explanation, and assistance level. Passing T01 unlocks a detailed T02 cost-function brief.
