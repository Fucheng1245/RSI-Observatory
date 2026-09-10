# Safety & Oversight

[← Observatory](README.md) · [Methodology](METHODOLOGY.md) · [Benchmarks](BENCHMARKS.md)

Self-modification changes the system being evaluated. A higher task score alone does not establish that its objectives, permissions, or evaluation process remain intact. This page is an editorial guide to assessing those questions; it is not a certification of any listed system.

## What to look for in an experiment

| Question | Evidence to request |
|---|---|
| Did the system improve the task or manipulate the test? | A frozen external evaluator, held-out tasks, and a record of which evaluation files the agent could access. |
| Did the objective change across generations? | Repeated behavioral checks against the original objective, including failures and regressions. |
| Can a modification be inspected and reversed? | Versioned changes, parent checkpoints, selection logs, and a tested rollback path. |
| Are gains due to a better method or more compute? | Matched budgets, multiple seeds, and cost per accepted improvement. |
| What can generated code affect? | Explicit execution boundaries, resource limits, and documented network and credential access. |
| Does the reported result reproduce? | A clean-run recipe with versions, tasks, seeds, traces, and independent replication status. |

These are Observatory review criteria. Missing evidence should be recorded as **not demonstrated**, rather than assumed to be either safe or unsafe.

## Starting points

- [Darwin Gödel Machine: safety consideration](https://github.com/jennyzzt/dgm#safety-consideration). The authors flag the risks of executing generated code. Review the execution boundary alongside capability results.
- [Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142). A formal starting point for reasoning about self-modification and goal preservation; its assumptions should not be treated as deployment guarantees.
- [OpenRSI](https://github.com/FrontisAI/OpenRSI). Inspect the executable evaluation and stated scope of the improvement loop when interpreting claims.
- [Research library](PAPERS.md). The Safety category provides additional candidates for investigation; inclusion is distinct from replication.

## Reporting a concern

For a classification dispute, use the classification-correction issue template with the source, exact field, proposed correction, and supporting evidence. Report vulnerabilities in a listed implementation through that project's own reporting process.

Review date: 2026-09-10.
