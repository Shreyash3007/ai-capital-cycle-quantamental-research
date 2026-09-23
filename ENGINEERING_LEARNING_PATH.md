# Software engineering learning path

The research engine is also a software engineering project. The learner will understand and write the code that moves data from source to model to research output. Software structure, SQL, APIs, frontend work, and system design enter when the next research problem needs them. This is a learning sequence, not a list of tools to install now.

## What full stack means here

The eventual stack has five layers: source data and storage, research calculations, a backend that serves versioned results, a small analyst-facing interface, and operations that keep runs reliable. The interface lets a reviewer inspect a signal, its evidence, its counter-thesis, and its paper consequence. It does not replace the research outputs with a dashboard.

The learner writes the learning-owned Python, SQL, backend, and frontend code. The mentor may prepare fixtures, checks, and setup, but must label those contributions and must not supply the active task's finished solution. Each new layer follows the same short loop: problem -> logic -> language or tool -> learner implementation -> run -> changed case -> tradeoff.

## Why the current folders exist

| Path | Job now | Question the learner should be able to answer |
|---|---|---|
| `Projects/AI Capital Cycle Quantamental Research Engine/src/` | Python source: instructions that create predictions and later research results | Where does the calculation live, and why is it separate from its inputs? |
| `Projects/AI Capital Cycle Quantamental Research Engine/data/` | Frozen teaching inputs and later dated source snapshots | Which data did a result use? |
| `Projects/AI Capital Cycle Quantamental Research Engine/outputs/` | Generated plots, tables, and reports | Can this result be recreated from code and input? |
| `Projects/AI Capital Cycle Quantamental Research Engine/tests/` | Checks that compare actual behavior with expected behavior | What change would reveal a bug? |
| `Goals/`, `Journey/`, `Evidence/`, `Knowledge/` | Tasks, attempts, observed proof, and concept links | What was planned, tried, demonstrated, and learned? |

`src` is a common name for source code, not a Python rule. We keep these boundaries because code, input data, generated results, and checks change for different reasons. T01 needs only one small learner-written script; a package, database, server, and frontend would add work without helping its prediction exercise. Learn the folder roles now; restructure only when a real repeated responsibility appears.

## Ordered build and learning checkpoints

| Phase | Engineering lesson | Learner-built evidence | Why at this point |
|---|---|---|---|
| P00 | Files and paths, Python values and arrays, functions, imports, command-line runs, simple tests, Git and reproducible outputs | Explain the current folders; run learner scripts; show one changed-input test and a saved plot | Understand the program before splitting it into services. |
| P01 | File formats, relational tables, keys, constraints, SQL queries and joins, transactions, parameterized queries | Load a frozen source snapshot into local SQLite; query a point-in-time company record back to its source | Real finance data needs traceable storage and time-aware joins. |
| P02 | Module boundaries, data contracts, query checks, indexes, logging, integration tests | Reproduce a market calculation from stored data and test a missing or late record | More data and joins make silent errors costly. |
| P03 | Reproducible model runs, configuration, typed result records, test automation | Rerun a model from a saved config and data snapshot; compare versions | Model evidence must survive code changes. |
| P04 | HTTP and JSON, external API clients, timeouts, retries, secrets, typed AI responses, test doubles | Evaluate a source-linked AI judgment from a recorded request and response | AI services are external dependencies that can fail or change. |
| P05 | Report schemas and versioned research artifacts | Trace one fragility claim from report to inputs and calculation | A research output needs a stable contract before it is served. |
| P06 | Read-only backend endpoints and API contracts | Serve a versioned signal or dossier through a tested local API | Other tools can consume research without owning its logic. |
| P07 | HTML/CSS/JavaScript basics, then TypeScript and React if the interaction warrants them; end-to-end system design and operations | Build a small evidence-linked analyst workbench; test browser, API, data lineage, stale-data behavior, and recovery | Full-stack skill is demonstrated on the finished research workflow. |

The phase IDs and finance/ML gates remain in [ROADMAP.md](ROADMAP.md). These engineering checkpoints are part of the relevant phase's acceptance evidence, not a separate percentage that inflates progress. A later phase cannot claim its engineering capability from a diagram alone.

## Stack decisions and gates

| Layer | Current or candidate choice | Decision gate |
|---|---|---|
| Current scripts | Python, NumPy, Matplotlib, PowerShell, Git | Already present; no database or server needed for T01. |
| First local database | Python `sqlite3` and SQLite | Add in P01 when frozen company records require keyed, time-aware queries. |
| Larger database | PostgreSQL candidate | Consider only if concurrency, data volume, or operating needs exceed the local database. |
| Backend API | FastAPI candidate | Choose in P06 after there is a versioned research artifact to serve. |
| Browser interface | Start with HTML/CSS/JavaScript; TypeScript and React are candidates for richer interaction | Choose in P07 after defining the reviewer workflow and the API contract. |

These are staged choices, not installed dependencies or claims of proficiency. Recheck official documentation and project needs at each gate. The current sources for later study are the [Python modules tutorial](https://docs.python.org/3/tutorial/modules.html), [Python SQLite interface](https://docs.python.org/3/library/sqlite3.html), [FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/), [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro), and [React learning guide](https://react.dev/learn).

## System design questions, in order

1. What does one function own, and what should it receive and return? Start in P00.
2. Which stored record existed at the decision time? Start in P01.
3. How do we detect a bad input, failed join, or changed source? Start in P02.
4. Can another person reproduce a model or report version? Start in P03-P05.
5. How does an API or AI dependency fail without corrupting the research record? Start in P04-P06.
6. Can a reviewer inspect the conclusion and its evidence, and can the live paper system recover after a failed run? Finish in P07.

At each gate the learner explains the design choice, writes the task code, runs a normal and changed case, and names a tradeoff. Record that evidence in [PROGRESS.md](PROGRESS.md) and [JOURNEY.md](JOURNEY.md). The next engineering lesson must not delay the current ML checkpoint.
