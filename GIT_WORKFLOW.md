# Public Git and learning workflow

## Purpose

The public repository should make the learning process inspectable. It should show what the learner wrote, what ran, what failed, what changed, and which claims were actually demonstrated. Git history is one part of that proof; [session notes](JOURNEY.md), [evidence records](Evidence/README.md), and [progress](PROGRESS.md) explain the meaning of each milestone.

## Ownership and publication

- GitHub owner: `Shreyash3007`.
- Repository: `ai-capital-cycle-quantamental-research`.
- Visibility: public.
- Remote: https://github.com/Shreyash3007/ai-capital-cycle-quantamental-research
- Local root: `D:\ML-project`.
- The project plans and infrastructure documents were mentor-assisted. Learner code is labeled and remains learner-authored.
- The ten course PDFs remain local under `MLS Slides/` and are excluded from Git. Public notes can cite their topics but do not redistribute the files.

The public repository was created on 2026-09-23. The [baseline commit `d9d9db6`](https://github.com/Shreyash3007/ai-capital-cycle-quantamental-research/commit/d9d9db648c842648951a0f5c59c83b23778027e8) was pushed to `main`; the local and remote hashes matched. This establishes the documentation baseline, not a demonstrated model.

## Milestone commit cycle

After each meaningful task or research milestone:

1. Run the learner's code and inspect the outputs together.
2. Save a dated [session note](Journey/SESSION_TEMPLATE.md) with the exact command, failures, corrections, and assistance.
3. Add an [evidence record](Evidence/EVIDENCE_TEMPLATE.md) only for checks actually demonstrated.
4. Update [PROGRESS.md](PROGRESS.md), affected [knowledge nodes](Knowledge/INDEX.md), and [KNOWLEDGE_GRAPH.md](KNOWLEDGE_GRAPH.md). Refresh [START_HERE.md](START_HERE.md) when the learner's next step changes.
5. Review the staged file list for slides, secrets, private data, generated bulk outputs, and unrelated work.
6. Commit the coherent milestone, then push to the public remote.
7. Verify the remote commit and public README after pushing.

Small code attempts may be committed before task completion. Label the commit as an attempt; do not imply it passed the gate. Save failures that explain a later correction.

## Commit messages

Use specific subjects that reflect evidence:

```text
docs: establish mentor and research roadmap
learn(T01): add first loop prediction attempt
fix(T01): correct vector shape after changed-input test
evidence(T01): record independent prediction demonstration
research(P05): reject unstable fragility signal
```

These are examples, not a claim that those events have happened.

## Public preflight

Before every push:

- `git status --short` shows only intended changes.
- `git diff --cached --name-only` contains no course PDF, secret, credential, or unlicensed provider dataset.
- New Markdown links resolve locally.
- The task, progress, graph, and journey states agree.
- A research claim cites its source, code version, data snapshot, and evaluation when relevant.

The mentor may prepare and run these checks. The learner should understand the resulting commit and be able to explain any learner-owned code in it.

## Synchronization limit

Commits and pushes happen when work is completed in a session and a mentor or the learner performs the cycle. This repository does not claim automatic background synchronization. The public history is current through the latest verified push, and [JOURNEY.md](JOURNEY.md) records what that push represents.
