---
type: project
id: AI-EQUITY-LAB
status: active
phase: P00
gate_status: not-demonstrated
updated: 2026-09-23
---

# AI Capital Cycle Quantamental Research Engine project hub

## Current build

The active build is the C1W2 valuation-stretch foundation. Start with:

- [Current context](../../00_CURRENT_CONTEXT.md)
- [Active goal](../../Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/GOAL.md)
- [Ready task](../../Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/T01%20-%20Vectorized%20Prediction.md)
- [Mentor Mode](../../MENTOR_MODE.md) and [progress](../../PROGRESS.md)
- learner file: `src/01_vectorized_prediction.py`

## Directory contract

| Path | Purpose |
|---|---|
| `src/` | learner-authored numbered implementation files |
| `data/` | immutable fixtures and later versioned snapshots |
| `outputs/` | reproducible plots, tables, and reports |
| `tests/` | tutor-provided and later learner-written verification |

Read the README in each directory before placing files there.

## Current state

- Documentation: established.
- Learner code: not started.
- Data: initial fixture not yet committed; T01 begins with a small in-script NumPy matrix.
- Outputs: none.
- Tests: none.
- Live services: none required.
- Learner-reported course coverage: C1W1 and C1W2 complete; C1W3 not yet confirmed. Later concepts can be taught early under Mentor Mode without changing course status.

## Long-term output contract

The project exists to produce point-in-time datasets, promoted or rejected signal research, model cards, company and segment dossiers, event studies, bubble and fragility analysis, and paper-portfolio attribution. A dashboard is not a completion requirement.

## Run convention

From this project directory, numbered scripts will be run with commands such as:

```powershell
python .\src\01_vectorized_prediction.py
```

The exact successful command and important output must be recorded in task evidence.

## Project-wide rules

- No secret keys or downloaded provider payloads are committed without review.
- Outputs must identify the input snapshot and code version once real data begins.
- Learner solution files are never silently overwritten by the tutor.
- Results are research evidence, not investment advice or real-money execution instructions.
