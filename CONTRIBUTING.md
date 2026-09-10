# Contributing to RSI Observatory

Thanks for helping keep the Observatory useful and high-signal.

## Inclusion policy

A project is in scope if it does at least one of the following:

1. demonstrates persistent or recursive self-improvement;
2. modifies a model, harness, memory, skill set, tool policy, scaffold, codebase, or training mechanism in ways that can improve future performance;
3. automates meaningful parts of AI R&D and closes an experiment / evaluation loop;
4. directly evaluates self-improvement or AI R&D capability;
5. studies safety, oversight, rollback, containment, reward hacking, or governance of self-improving systems;
6. provides an important survey, taxonomy, or research map of the field.

Pure one-shot self-critique or output refinement without persistent system change is usually out of scope unless it is an enabling component in a larger persistent loop.

## Add a repository

Edit `data/repos.json` and add one object with:

```json
{
  "full_name": "owner/repository",
  "category": "Benchmark",
  "note": "One-sentence explanation of the RSI connection."
}
```

Then run:

```bash
python scripts/update.py
```

The script will refresh metadata and regenerate the dynamic README sections.

## Add or correct a paper

The curated research library is generated from `data/paper-index.json`. Add one record with:

```json
{
  "title": "Paper title",
  "url": "https://arxiv.org/abs/...",
  "year": 2026,
  "layer": "Harness",
  "relevance": "Core"
}
```

Then run:

```bash
make papers
make check
```

Use **Core** when persistent self-improvement, self-modification, or recursive/meta-improvement is central to the work. **Core does not automatically mean L4 RSI.** Otherwise prefer **Enabling**, **Adjacent**, or **Foundational**. Classification corrections should cite the paper or another primary source.

## Categories

Prefer one primary category. If a project spans several categories, choose the category that best explains why someone would track it.

## Quality bar

Please avoid duplicate mirrors, obvious spam, abandoned empty repositories, trading-indicator RSI repositories, and projects whose relationship to recursive self-improvement is only keyword-level.


## Scorecard changes

Scorecard edits need stronger evidence than ordinary catalog additions. A proposed change should include a primary source showing the self-modification path, persistence, evaluation loop, or recursive-depth claim being changed. Prefer conservative labels when evidence is ambiguous.

Do not use total GitHub Stars as evidence of RSI capability.
