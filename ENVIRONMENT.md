# Environment and nominal operations

## Current local baseline

The initial environment has been observed with:

- Windows and PowerShell;
- Python 3.14.5;
- NumPy 2.4.4;
- Matplotlib 3.10.9;
- pandas available;
- Jupyter not currently required.

Versions must be rechecked before relying on this note in a future environment.

## Stage 0 run model

The first phase uses ordinary Python scripts so execution order and state remain visible. From the project hub:

```powershell
python .\src\01_vectorized_prediction.py
```

No Docker, database, web server, TypeSafe API, or background service is needed for ML-G01.

The standalone Git repository was initialized on 2026-09-22. No baseline commit has been created.

## Dependency policy

- Add a library only for a defined capability.
- Pin dependencies when the first reproducible environment file is created.
- Do not install a training framework to avoid implementing the current learning objective.
- Keep secrets outside the repository.
- Record the exact environment with every serious experiment.

## Repository operations

- Add a Python environment file when the first executable task begins.
- Add formatting and tests only when the learner understands the underlying commands.
- Keep generated outputs separate from source.
- Add large raw datasets to ignored, versioned storage rather than normal Git history.

## Health checks by stage

| Stage | Required readiness |
|---|---|
| C1W2 scripts | Python imports and a successful small NumPy operation |
| static plots | Matplotlib can save and reopen a PNG |
| live data | provider credential, rate-limit, schema, and snapshot-write checks |
| TypeSafe/Jev | SDK/API authentication plus a recorded low-risk test request |
| optional research viewer | local server health plus browser rendering checks |
| scheduled paper system | scheduler, snapshot, inference, and alert health checks |

Heavy runtimes should be started only when a real stage requires them.
