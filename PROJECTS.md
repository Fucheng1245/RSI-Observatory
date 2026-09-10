# Projects & Systems

> **Browse broadly; classify conservatively.** Project names and self-descriptions are discovery signals, not capability grades.

[← Observatory](README.md) · [Methodology](METHODOLOGY.md) · [Scorecard](SCORECARD.md) · [Trends](TRENDS.md)

## Role vocabulary

- **Direct RSI** — L4-like public evidence: the improvement mechanism itself is modifiable in a bounded loop.
- **RSI-directed meta-evolution** — explicitly targets meta/recursive improvement with bounded evidence, while broader RSI remains unclaimed or unproven.
- **Self-improving system** — persistent autonomous improvement is central (typically L3/L3-like) without demonstrated mutable improver.
- **RSI substrate** — runtime/harness/environment for building RSI loops; the instantiated loop must be scored.
- **Enabling** — component-level work useful to RSI.
- **Adjacent AI R&D** — important research automation or AI-for-AI work that is relevant without being mislabeled as RSI.

See [METHODOLOGY.md](METHODOLOGY.md) for the formal rules.

## Self-modifying and RSI-directed systems

| System | Role | Update target | Notes |
|---|---|---|---|
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) | Direct RSI | Agent source code / archive | Open-ended evolution of coding agents; validated improvements are retained in an evolving archive. |
| [OpenRSI](https://github.com/FrontisAI/OpenRSI) | RSI-directed meta-evolution | ML engineering / AI4AI stack | Executable and measurable AI4AI stack; includes OpenMLE and Frontis-MA1. |
| [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) | Direct RSI | Agent implementation | Self-referential agent framework explicitly framed around RSI. |
| [LightRSI](https://github.com/zjunlp/LightRSI) | RSI substrate | Agent runtime / memory / skills | Runtime for lightweight recursive improvement loops in long-horizon agents. |
| [KnowAct](https://github.com/HITsz-TMG/KnowAct) | Self-improving system | Personal-agent capabilities | Persistent personal-agent setting for recursive capability growth. |
| [RSI-Harness](https://github.com/CosmosMind-ai/RSI-Harness) | RSI substrate / experiment | Agent harness / configuration | Versionable harness and genome-style configuration surface for iterative evolution. |
| [VideoHarness-RSI](https://github.com/Tencent/VideoHarness-RSI) | RSI-directed / domain experiment | Video-agent harness | Domain-specific harness self-improvement work. |
| [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | Self-improving system | Coding-agent implementation | Agent edits its own implementation and evaluates changes empirically. |
| [MetaSkill-Evolve](https://arxiv.org/abs/2607.05297) | RSI-directed meta-evolution | Skills + meta-skill updater | Two-timescale design where task skills and the improvement controller both evolve. |
| [AREX](https://arxiv.org/abs/2607.21461) | Self-improving system | Deep-research improvement state | Outer verification loop recursively improves long-horizon research behavior. |

## Self-improving coding and long-running agents

| System | Role | Focus |
|---|---|---|
| [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) | Self-improving system | Self-improving RLM agent for coding workflows and long-running autonomous tasks. |
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) | Direct RSI | Open-ended code-level evolution of agents. |
| [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | Self-improving system | Self-editing coding agent evaluated on software-engineering tasks. |
| [SWE-Gym](https://arxiv.org/abs/2412.21139) | Enabling | Executable software tasks and trajectories for training agents and verifiers. |
| [Teaching LLMs to Self-Debug](https://arxiv.org/abs/2304.05128) | Enabling | Execution-feedback loops for diagnosing and repairing code. |
| [AgentCoder](https://arxiv.org/abs/2312.13010) | Enabling | Multi-agent iterative code generation, test design and repair. |
| [STOP](https://arxiv.org/abs/2310.02304) | Enabling / recursive | LLM-written scaffolding improves the program responsible for further improvements. |

## Automated AI R&D and scientific discovery

| System | Role | Focus |
|---|---|---|
| [The AI Scientist](https://github.com/SakanaAI/AI-Scientist) | Adjacent AI R&D | Idea generation, experimentation, analysis, paper writing and review. |
| [The AI Scientist-v2](https://doi.org/10.1038/s41586-026-10265-5) | Adjacent AI R&D | More end-to-end, template-free automated research with agentic tree search. |
| [OpenRSI / OpenMLE](https://github.com/FrontisAI/OpenRSI) | RSI-directed / AI4AI | Execution-grounded ML engineering and program evolution. |
| [Frontis-MA1](https://arxiv.org/abs/2607.28568) | RSI-directed / AI4AI | Training an AI4AI model toward recursive improvement in ML engineering. |
| [AutoResearch](https://arxiv.org/abs/2608.17906) | Adjacent AI R&D | Grounded idea generation, coordinated experiments, diagnosis and independent review. |
| [FT-Dojo](https://arxiv.org/abs/2603.01712) | Adjacent AI R&D | Autonomous LLM fine-tuning environment spanning data, training, evaluation and strategy revision. |
| [MLEvolve](https://arxiv.org/abs/2606.06473) | Self-improving system | Long-horizon machine-learning algorithm discovery with search and retrospective memory. |
| [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525) | Adjacent AI R&D | Turns training and post-training into executable research environments. |
| [AlphaEvolve](https://arxiv.org/abs/2506.13131) | Enabling / AI R&D | LLM code generation plus automated evaluation and evolutionary search for algorithms. |
| [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) | Enabling | Evolutionary program search with a frozen language model and evaluators. |

## Model and training self-improvement

### Self-training, self-reward and self-distillation

- [EvoLM](https://arxiv.org/abs/2605.03871) — co-evolves discriminative rubrics and policy updates without human annotation.
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — model produces and judges its own alignment data across rounds.
- [Self-Play Fine-Tuning](https://arxiv.org/abs/2401.01335) — preference learning through self-play.
- [Meta-Rewarding Language Models](https://arxiv.org/abs/2407.19594) — improves both judgments and responses using a meta-judge loop.
- [SELF](https://arxiv.org/abs/2310.00533) — repeated self-feedback, refinement, filtering and fine-tuning.
- [Self-Instruct](https://arxiv.org/abs/2212.10560) — bootstraps instruction data from model generations.
- [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610) — pseudo-labeling with high-confidence self-generated answers.
- [Beyond Human Data](https://arxiv.org/abs/2312.06585) — iterative model-generated problem-solving data and filtering.

### Test-time and self-evolving optimization

- [SERPO](https://arxiv.org/abs/2607.26873) — co-evolves evidence, rubrics and policy parameters in open-ended test-time RL.
- [Teaching LLMs to Self-Evolve / MetaEvolve](https://arxiv.org/abs/2607.21971) — trains meta-skills for feedback-driven evolutionary refinement.
- [TEMPO](https://arxiv.org/abs/2604.19295) — sustained test-time parameter updates with critic recalibration.
- [Self-Adapting Language Models / SEAL](https://arxiv.org/abs/2506.10943) — models generate their own update data and fine-tuning directives.
- [Self-Improvement in Language Models: The Sharpening Mechanism](https://arxiv.org/abs/2412.01951) — formalizes verifier-guided improvement amortized into a stronger policy.
- [rStar-Math](https://arxiv.org/abs/2501.04519) — self-evolved deep-thinking data and preference modeling for math reasoning.
- [Quiet-STaR](https://arxiv.org/abs/2403.09629) — learns useful internal rationales throughout text.
- [STaR](https://arxiv.org/abs/2203.14465) — bootstraps reasoning from generated rationales and filtering.

## Harness, scaffold and program optimization

- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) — meta-agent invents and improves executable agent architectures.
- [TextGrad](https://arxiv.org/abs/2406.07496) — textual gradients optimize prompts, code and compound AI-system variables.
- [OPRO](https://arxiv.org/abs/2309.03409) — language models iteratively optimize natural-language solutions and prompts.
- [Promptbreeder](https://arxiv.org/abs/2309.16797) — evolves both task prompts and the mutation prompts that generate improvements.
- [DSPy](https://arxiv.org/abs/2310.03714) — compiles declarative LM programs by optimizing prompts/demonstrations against metrics.
- [Language Agent Tree Search](https://arxiv.org/abs/2310.04406) — combines search, value estimates, environment feedback and self-reflection.
- [STOP](https://arxiv.org/abs/2310.02304) — self-referential scaffolding optimization.

## Memory, context and skill evolution

- [Recuris](https://github.com/Gen-Verse/Recuris) — recursive experiential/working-memory evolution for long-horizon harnesses.
- [Agentic Context Engineering](https://arxiv.org/abs/2510.04618) — evolves context as a structured playbook.
- [EvolveR](https://arxiv.org/abs/2510.16079) — distills trajectories into reusable strategies and closes the loop with policy reinforcement.
- [Strategy Genes](https://arxiv.org/abs/2604.15097) — compact editable experience representations for test-time evolution.
- [MetaSkill-Evolve](https://arxiv.org/abs/2607.05297) — fast skill evolution plus slower meta-skill evolution.
- [PAST-Bench](https://arxiv.org/abs/2608.04003) — evaluation framework for whether retained experience actually improves later behavior.

## Multi-agent and co-evolution

Multi-agent systems become RSI-relevant when agents improve each other, improve the coordination protocol, or participate in population-level search rather than merely debate once.

- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) — searches agent-system designs rather than one fixed agent.
- [POET](https://arxiv.org/abs/1901.01753) — co-evolves environments and agents with transfer between emerging challenges.
- [PACEvolve](https://arxiv.org/abs/2601.10657) — progress-aware collaborative long-horizon evolutionary search.

## Embodied and physical self-improvement

- [ASPIRE](https://arxiv.org/abs/2607.00272) — failure diagnosis, code-as-policy editing and validated reusable skill libraries for robotics.
- [ENPIRE](https://arxiv.org/abs/2606.19980) — real-robot autoresearch loop that can edit policy, infrastructure or algorithm code and rerun experiments.
- [MineEvolve](https://arxiv.org/abs/2603.13131) — converts success into reusable skills and failures into executable guardrails.
- [RISE](https://arxiv.org/abs/2602.11075) — imagined rollouts from a world model drive continuing robot-policy updates.
- [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) — frozen model evolves reusable skills and context-code harness from environment rollouts.
- [Self-Improving VLA Models via Residual RL](https://iclr.cc/virtual/2026/poster/10008318) — generates recovery trajectories in failure regions and distills them back into a generalist policy.

## Evolutionary and open-ended systems

- [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) — open-ended archive of self-modified agents.
- [PACEvolve](https://arxiv.org/abs/2601.10657) — long-horizon progress-aware evolutionary search.
- [AlphaEvolve](https://arxiv.org/abs/2506.13131) — coding-agent evolutionary search for scientific and algorithmic discovery.
- [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) — program evolution with LM generation and automated evaluators.
- [AutoML-Zero](https://arxiv.org/abs/2003.03384) — evolves ML algorithms from elementary operations.
- [AI-GAs](https://arxiv.org/abs/1905.10985) — proposes algorithms that generate environments, architectures and learning algorithms.
- [POET](https://arxiv.org/abs/1901.01753) — open-ended co-evolution of environments and solutions.
- [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474) — meta-learns an optimizer.
- [MAP-Elites](https://arxiv.org/abs/1504.04909) — quality-diversity archive that illuminates high-performing niches.
- [POWERPLAY](https://arxiv.org/abs/1112.5309) — continually invents tasks and modifies a solver so its verified skill set expands.

## Introspection and self-modeling

- [Emergent Introspective Awareness in Large Language Models](https://arxiv.org/abs/2601.01828)
- [Self-Reference in Large Language Models: The Introspection Threshold for RSI](https://arxiv.org/abs/2607.04277)
- [Structure Enables Effective Self-Localization of Errors in LLMs](https://arxiv.org/abs/2602.02416)
- [Looking Inward](https://arxiv.org/abs/2410.13787)
- [Recursive Introspection](https://arxiv.org/abs/2407.18219)
- [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221)

## Benchmarks and maps

- [RSI-Exam](https://github.com/aiming-lab/RSI-Exam) — executable research improvement.
- [PAST-Bench](https://github.com/Gen-Verse/PAST-Bench) — persistent experience and future-agent improvement.
- [Scale RSI Bench](https://github.com/scaleapi/rsi-benchmark) — AI-R&D capability.
- [OpenRSI / OpenMLE](https://github.com/FrontisAI/OpenRSI) — execution-grounded MLE environment and search loop.
- [Awesome RSI](https://github.com/lobehub/awesome-rsi) — broad curated research map.
- [Awesome Self-Improving Agents](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents) — survey-oriented self-improving-agent map.
- [Recursive Self-Improving Agents survey resources](https://github.com/D2I-ai/awesome-recursive-self-improving-agents) — framework-oriented survey map.

## Inclusion boundary

The catalog is intentionally wider than “strict RSI,” because the practical path to RSI is being built from adjacent components. Every entry should nevertheless connect to at least one of these:

- persistent learning or adaptation;
- self-modification of model/harness/code;
- improvement of an updater, evaluator or learning algorithm;
- automated research that changes future AI systems;
- open-ended evolutionary improvement;
- direct evaluation of self-improvement;
- safety mechanisms for systems that change themselves.
