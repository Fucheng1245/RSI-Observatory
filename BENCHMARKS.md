# RSI Benchmark Guide

“Recursive self-improvement” is too broad for one leaderboard. A useful benchmark must specify **what part of the improvement loop it measures** and whether the claimed gain persists outside the optimization episode.

## Self-improvement / RSI-oriented evaluations

| Benchmark / environment | Main question | Update target | Horizon | Evaluation style |
|---|---|---|---|---|
| [PAST-Bench](https://arxiv.org/abs/2608.04003) | Does retained experience improve future personal-agent behavior? | Memory, procedures, information state | Multi-episode | Matched retained-experience on/off conditions + pathway evidence |
| [AI4AI-Bench](https://arxiv.org/abs/2608.20318) | Can an agent improve the training algorithm itself? | Objective / update rule / learning algorithm | Hours per research task | Clean rerun from scratch + hidden fixed evaluator |
| [RSI-Exam](https://github.com/aiming-lab/RSI-Exam) | Can an agent improve executable research methods through experimentation? | Research method / artifact | Long-horizon fixed budget | Hidden evaluation set |
| [Scale RSI Bench](https://github.com/scaleapi/rsi-benchmark) | Can agents develop capabilities needed to advance AI R&D? | Research / engineering capability | Agentic task horizon | Benchmark suite |
| [OpenMLE / OpenRSI](https://github.com/FrontisAI/OpenRSI) | Can AI improve ML-engineering programs in executable environments? | MLE program / operator | Long-horizon search | Execution-grounded scoring |

## Capability proxies that matter for RSI

Not every useful evaluation is branded RSI. These capability families can provide evidence about prerequisites:

- **software engineering** — can the agent modify large codebases and validate changes?
- **long-horizon autonomy** — can it maintain goals and state over many tool calls?
- **ML engineering** — can it train, debug and compare models reproducibly?
- **scientific experimentation** — can it formulate hypotheses, run experiments and reject bad ideas?
- **verifier use** — can it exploit strong external feedback without gaming it?
- **memory transfer** — can experience from task A cause better performance on task B?
- **algorithm discovery** — can it produce genuinely new training/search procedures?

These should be labeled **proxies**, not direct demonstrations of RSI.

## Benchmark profiles

### PAST-Bench

Focuses on a prerequisite for persistent agents: **experience must improve future behavior, not merely be stored**. It is valuable because it asks for pathway evidence — save, retrieve, update — instead of treating any higher score as proof of memory-driven improvement.

Best for: memory systems, personal agents, procedural reuse, persistent state.

### AI4AI-Bench

Targets a higher recursive layer: **the learning algorithm itself**. A clean rerun from scratch helps separate real algorithmic improvement from accidental state, more data or evaluation leakage.

Best for: AI4AI, algorithm design, training-system improvement.

### RSI-Exam

Tests sustained experimentation on an executable research artifact under a fixed budget and hidden evaluation.

Best for: long-horizon research, method improvement, iterative experimentation.

### Scale RSI Bench

Tracks broader capabilities associated with advancing AI R&D. It is better interpreted as a capability signal than as proof of a complete recursive loop.

Best for: frontier research/engineering capability monitoring.

### OpenMLE / OpenRSI

An execution-grounded environment for ML engineering and program evolution rather than just a single score.

Best for: testing improvement operators, agentic MLE, end-to-end AI4AI loops.

## A strong RSI benchmark should test

### 1. Persistence
The improvement survives into future tasks or clean reruns.

### 2. Causal attribution
The benchmark can identify *what caused* the gain rather than merely observing a higher score.

### 3. Independent evaluation
The optimizer cannot trivially rewrite or influence the final judge.

### 4. Held-out generalization
The gain transfers to tasks not directly optimized during the loop.

### 5. Clean reruns
The improved artifact works from a fresh environment, not because of hidden caches or manual state.

### 6. Recursive depth
The benchmark distinguishes:

- better output;
- better task solver;
- better persistent agent;
- better updater;
- better research loop.

### 7. Compute normalization
The score should make clear whether improvement comes from a better system or simply more inference/search budget.

### 8. Reproducibility
Another team should be able to recreate the loop from public artifacts and documented settings.

### 9. Safety observability
For self-modifying systems, the benchmark should expose diffs, version history and failed modifications where possible.

## Common benchmark failure modes

- visible test overfitting;
- reward/evaluator hacking;
- hidden human intervention;
- calling more compute “self-improvement”;
- storing memory without showing causal reuse;
- comparing different base models or budgets;
- evaluation contamination;
- self-judging loops with no external ground truth;
- reporting best-of-many runs without failure rate.

## Observatory benchmark labels

Each tracked evaluation should eventually carry:

- **Direct / Proxy**;
- **Update target**;
- **Evaluator type**;
- **Hidden eval?**;
- **Clean rerun?**;
- **Persistent state?**;
- **Recursive depth**;
- **Public tasks / code / leaderboard?**.

This makes cross-benchmark comparisons possible without pretending all scores measure the same thing.
