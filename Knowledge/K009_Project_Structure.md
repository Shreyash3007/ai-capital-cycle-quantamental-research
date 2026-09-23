# K009: Project structure

**Learning status:** planned for P00. **Project evidence:** none yet.

`src` holds source code, `data` holds inputs, `outputs` holds generated results, and `tests` holds checks. The names are conventions; the reason for the separation is that each kind of file has a different job and change pattern. The learner should be able to trace a T01 result from input, through learner-written code, to output and a check.

**First small check:** explain why the prediction calculation belongs in `src` while a saved plot belongs in `outputs`. No extra package or server is needed for T01.

**Used by:** [T01](../Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/T01%20-%20Vectorized%20Prediction.md) and [the later engineering path](../ENGINEERING_LEARNING_PATH.md). **Progress:** [ledger](../PROGRESS.md).
