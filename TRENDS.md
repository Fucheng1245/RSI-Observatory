# RSI Trends

This page separates **field-level trends** from individual project rankings. The live repository table in README provides the raw momentum signal; this file explains what to watch and why.

## Current themes to watch (2026)

### 1. Self-improving coding agents are becoming a distinct product/research category

The combination of executable code, exact tests and editable agent source makes software engineering a natural RSI testbed. Public systems now range from experimental self-editing agents to large coding-agent projects explicitly marketed as self-improving.

Watch: Prime Agent, Darwin Gödel Machine, Gödel Agent, self-improving coding-agent research, SWE-Gym-style verifier infrastructure.

### 2. Automated AI R&D is converging with RSI

Automated research used to mean “generate a paper.” Newer systems increasingly operate over code, training, experiments, diagnosis and algorithm design. The remaining bottleneck is often **what to research and how to validate true progress**.

Watch: AI Scientist, OpenRSI/OpenMLE, Frontis-MA1, AI4AI-Bench, AutoResearch, FT-Dojo, MLEvolve, AlphaEvolve.

### 3. Evaluation is becoming its own RSI subfield

As claims become stronger, the evaluator becomes the center of the problem. PAST-Bench, AI4AI-Bench and RSI-Exam isolate different parts of the loop rather than using one generic agent score.

Watch for: clean reruns, hidden evaluators, causal attribution, generalization, compute normalization.

### 4. Memory is moving from storage to improvement

Long-term memory projects are increasingly evaluated by whether saved experience *causes future gains*. This is a major shift from “has memory” to “learns persistently.”

Watch: Recuris, PAST-Bench, Agentic Context Engineering, EvolveR, strategy/skill representations.

### 5. Recursive depth is becoming explicit

The important distinction is no longer only “does the agent improve?” but “does the mechanism that performs improvement also improve?” Meta-skill evolution and self-referential code search make this measurable.

Watch: MetaSkill-Evolve, STOP, Darwin Gödel Machine, evaluator/rubric evolution.

### 6. Embodied RSI is emerging

Robotics adds real execution cost, resets, physical uncertainty and persistent skill libraries. It is a useful stress test for whether self-improvement survives outside text-only benchmarks.

Watch: ASPIRE, ENPIRE, RISE, MineEvolve, skill-harness evolution.

### 7. Safety concerns are shifting from static alignment to modification governance

Repeated persistent updates introduce versioning, evaluator integrity, rollback and goal-drift problems that do not appear in the same way for static chat models.

Watch: TamperBench, misevolution, goal-drift evaluation, safeguarded high-order objectives.

## Repository signals

Total Stars answer “what has accumulated attention?” Momentum answers “what is moving now?” The Observatory should compute:

- **7d Star delta**;
- **30d Star delta**;
- **Star velocity** = delta / days observed;
- **recent push age**;
- **fork growth**;
- **new contributors**;
- **new releases/tags**;
- **issue/PR activity**;
- **new repo creation rate by subfield**.

## Research signals

- papers/month containing `recursive self-improvement`;
- papers/month containing `self-improving agent` or `self-evolving agent`;
- number of new direct RSI benchmarks;
- number of systems with hidden/independent evaluation;
- number of systems modifying code vs memory vs weights vs algorithms;
- shift from static datasets toward executable environments;
- open-source vs closed evaluation artifacts.

## A useful “field maturity” dashboard

| Dimension | Early field | Maturing field |
|---|---|---|
| Claims | qualitative demos | controlled causal evaluations |
| Updates | prompt/output | persistent code/weights/algorithms |
| Evaluation | visible benchmark | hidden / independent / clean rerun |
| Loops | one-step | multi-generation |
| Reproducibility | screenshots / anecdotes | public environments and configs |
| Safety | general discussion | versioning, rollback, evaluator integrity |
| Research ecosystem | isolated papers | shared benchmarks, runtimes and leaderboards |

## Snapshot caveat

Popularity is not capability. A large adjacent automated-research project can have more Stars than a direct RSI benchmark because the user base is broader. The Observatory therefore keeps **role/category labels** alongside momentum metrics.

## Planned trend features

- 7/30/90-day sparklines;
- “new this week” project feed;
- subfield momentum index;
- benchmark-release timeline;
- paper velocity by taxonomy branch;
- direct-RSI vs adjacent-R&D filters;
- lab/team activity view;
- historical snapshots downloadable as CSV/JSON.
