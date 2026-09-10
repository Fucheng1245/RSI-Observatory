# RSI Research Library

> **213 papers and research works, structured by how they relate to Recursive Self-Improvement.**

Not everything that improves an AI system is RSI. This library separates **Core self-improvement**, **Enabling mechanisms**, **Adjacent AI R&D/evaluation**, and **Foundational work** so breadth does not come at the cost of precision.

**Coverage:** 213 research works · 100 Core · 57 Enabling · 39 Adjacent · 17 Foundational · 95 from 2026

[← Observatory](README.md) · [Landscape](LANDSCAPE.md) · [Scorecard](SCORECARD.md) · [Benchmarks](BENCHMARKS.md) · [Safety](SAFETY.md)

---

## If you only read 20

| Work | Track | Why it matters |
|---|---|---|
| [Gödel Machines](https://arxiv.org/abs/cs/0309048) | **Foundations** | The classic self-referential improvement formalism. |
| [STOP](https://arxiv.org/abs/2310.02304) | **Harness** | A concrete modern bridge from code-generation to recursive scaffold improvement. |
| [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) | **Agent** | Lets an agent inspect and rewrite its own logic. |
| [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) | **Code** | Empirical self-modification with an archive of validated improvements. |
| [MetaSkill-Evolve](https://arxiv.org/abs/2607.05297) | **Skills** | Makes the skill-improvement machinery itself part of the evolving system. |
| [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | **Harness** | A clean self-improving-harness loop with held-out validation. |
| [Recursive Experiential-Working Memory Evolution / Recuris](https://arxiv.org/abs/2608.24876) | **Memory** | Persistent experience/working-memory evolution for long-horizon agents. |
| [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) | **Cross-component** | Jointly updates the agent harness and model weights. |
| [Frontis-MA1](https://arxiv.org/abs/2607.28568) | **AI R&D** | Execution-grounded AI4AI training in ML engineering. |
| [AI4AI-Bench](https://arxiv.org/abs/2608.20318) | **Evaluation** | Tests whether agents can improve training algorithms under executable evaluation. |
| [PAST-Bench](https://arxiv.org/abs/2608.04003) | **Evaluation** | Tests whether retained experience actually improves later performance. |
| [PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640) | **Evaluation** | Measures autonomous post-training under a real compute/time budget. |
| [AutoScientists](https://arxiv.org/abs/2605.28655) | **AI R&D** | Studies decentralized research teams that share evidence and coordinate around hypotheses; recursive updater modification is not established here. |
| [Bilevel Autoresearch](https://arxiv.org/abs/2603.23420) | **Meta-loop** | Explicit bilevel optimization of the research/improvement process. |
| [AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461) | **Research agent** | Uses an outer audit/improvement loop to drive targeted follow-up research. |
| [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191) | **Reality check** | Useful negative evidence on current open-ended AI R&D limits. |
| [Your Agent May Misevolve](https://arxiv.org/abs/2509.26354) | **Safety** | Focuses directly on emergent risks from self-evolving agents. |
| [TamperBench](https://arxiv.org/abs/2602.06911) | **Safety** | Stress-tests whether safety survives fine-tuning and tampering. |
| [Evaluating Goal Drift in Language Model Agents](https://arxiv.org/abs/2505.02709) | **Safety** | Measures long-horizon objective drift. |
| [Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142) | **Theory** | Formal conditions for goal-preserving self-modification. |

---

## How the library is labeled

| Label | Meaning |
|---|---|
| **Core** | Persistent self-improvement, self-modification, or recursive/meta-improvement is central. **Core does not automatically mean L4 RSI.** |
| **Enabling** | Memory, verification, tooling, optimization, or another mechanism useful for RSI, but not itself a recursive loop. |
| **Adjacent** | AI R&D automation, open-ended search, or evaluation that materially informs the path to RSI. |
| **Foundational** | Historical, theoretical, or survey work used to frame the field. |

> These labels are **RSI Observatory judgments**, not author claims. They are deliberately conservative and can be challenged through a classification-correction issue.

### Research routes

- **Self-modifying agents:** STOP → Gödel Agent → Darwin Gödel Machine → Self-Harness → MetaSkill-Evolve
- **Memory & skills:** Reflexion → A-MEM → Recuris → SkillOpt → MetaSkill-Evolve
- **Automated AI R&D:** AI Scientist → Execution-Grounded AI Research → Frontis-MA1 → AutoScientists → AI4AI-Bench
- **Evaluation:** PAST-Bench → PostTrainBench → AI4AI-Bench → LongWoF-Bench → MLS-Bench
- **Safety:** Self-Modification of Policy/Utility → Goal Drift → TamperBench → Misevolution → SAHOO

---

## Full research index

The machine-readable source is [`data/paper-index.json`](data/paper-index.json).

<details>
<summary><strong>Foundations</strong> — 7 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [A Formulation of Recursive Self-Improvement and Its Possible Efficiency](https://arxiv.org/abs/1805.06610) | 2018 | **Foundational** |
| [From Seed AI to Technological Singularity via Recursively Self-Improving Software](https://arxiv.org/abs/1502.06512) | 2015 | **Foundational** |
| [Bounded Recursive Self-Improvement](https://arxiv.org/abs/1312.6764) | 2013 | **Foundational** |
| [Gödel Machines](https://arxiv.org/abs/cs/0309048) | 2003 | **Foundational** |
| [Optimal Ordered Problem Solver](https://arxiv.org/abs/cs/0207097) | 2002 | **Foundational** |
| [Evolutionary Principles in Self-Referential Learning](https://people.idsia.ch/~juergen/diploma1987ocr.pdf) | 1987 | **Foundational** |
| [Speculations Concerning the First Ultraintelligent Machine](https://www.sciencedirect.com/science/article/pii/S0065245808604180) | 1965 | **Foundational** |

</details>

<details>
<summary><strong>Field maps</strong> — 6 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) | 2026 | **Foundational** |
| [Self-evolving Embodied AI](https://arxiv.org/abs/2602.04411) | 2026 | **Foundational** |
| [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) | 2026 | **Foundational** |
| [A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/abs/2508.07407) | 2025 | **Foundational** |
| [A Survey of Self-Evolving Agents](https://arxiv.org/abs/2507.21046) | 2025 | **Foundational** |
| [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) | 2024 | **Foundational** |

</details>

<details>
<summary><strong>Memory / Skills</strong> — 28 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [CoEvoSkills](https://arxiv.org/abs/2604.01687) | 2026 | **Core** |
| [Decocted Experience](https://arxiv.org/abs/2604.04373) | 2026 | **Core** |
| [From Procedural Skills to Strategy Genes](https://arxiv.org/abs/2604.15097) | 2026 | **Core** |
| [Learning to Continually Learn via Meta-learning Agentic Memory Designs](https://arxiv.org/abs/2602.07755) | 2026 | **Core** |
| [Live-Evo](https://arxiv.org/abs/2602.02369) | 2026 | **Core** |
| [Memory Transfer Learning](https://arxiv.org/abs/2604.14004) | 2026 | **Core** |
| [MetaSkill-Evolve](https://arxiv.org/abs/2607.05297) | 2026 | **Core** |
| [PAST-Bench](https://arxiv.org/abs/2608.04003) | 2026 | **Core** |
| [Programmatic Skill Networks](https://arxiv.org/abs/2601.03509) | 2026 | **Core** |
| [Recursive Experiential-Working Memory Evolution / Recuris](https://arxiv.org/abs/2608.24876) | 2026 | **Core** |
| [SkillFoundry](https://arxiv.org/abs/2604.03964) | 2026 | **Core** |
| [SkillGen](https://arxiv.org/abs/2605.10999) | 2026 | **Core** |
| [SkillOS](https://arxiv.org/abs/2605.06614) | 2026 | **Core** |
| [SkillX](https://arxiv.org/abs/2604.04804) | 2026 | **Core** |
| [Agentic Context Engineering](https://arxiv.org/abs/2510.04618) | 2025 | **Core** |
| [Confucius Code Agent](https://arxiv.org/abs/2512.10398) | 2025 | **Core** |
| [EvolveR](https://arxiv.org/abs/2510.16079) | 2025 | **Core** |
| [FLEX](https://arxiv.org/abs/2511.06449) | 2025 | **Core** |
| [MemEvolve: Meta-Evolution of Agent Memory Systems](https://arxiv.org/abs/2512.18746) | 2025 | **Core** |
| [ReasoningBank](https://arxiv.org/abs/2509.25140) | 2025 | **Core** |
| [SkillWeaver](https://arxiv.org/abs/2504.07079) | 2025 | **Core** |
| [SWE-Exp](https://arxiv.org/abs/2507.23361) | 2025 | **Core** |
| [ToolCoder](https://arxiv.org/abs/2502.11404) | 2025 | **Core** |
| [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | 2025 | **Enabling** |
| [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | 2023 | **Enabling** |
| [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) | 2023 | **Enabling** |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | **Enabling** |
| [Tool Makers](https://arxiv.org/abs/2305.17126) | 2023 | **Enabling** |

</details>

<details>
<summary><strong>Harness</strong> — 21 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850) | 2026 | **Core** |
| [AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses](https://arxiv.org/abs/2608.12307) | 2026 | **Core** |
| [AutoHarness: Improving LLM Agents by Automatically Synthesizing a Code Harness](https://arxiv.org/abs/2603.03329) | 2026 | **Core** |
| [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) | 2026 | **Core** |
| [EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.05446) | 2026 | **Core** |
| [Learning to Self-Evolve](https://arxiv.org/abs/2603.18620) | 2026 | **Core** |
| [MEMO](https://arxiv.org/abs/2603.09022) | 2026 | **Core** |
| [MemoHarness: Agent Harnesses That Learn from Experience](https://arxiv.org/abs/2607.14159) | 2026 | **Core** |
| [Reflective Context Learning](https://arxiv.org/abs/2604.03189) | 2026 | **Core** |
| [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | 2026 | **Core** |
| [SePO: Self-Evolving Prompt Agent for System Prompt Optimization](https://arxiv.org/abs/2606.04465) | 2026 | **Core** |
| [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904) | 2026 | **Core** |
| [Dynamic Cheatsheet](https://arxiv.org/abs/2504.07952) | 2025 | **Core** |
| [SCOPE](https://arxiv.org/abs/2512.15374) | 2025 | **Core** |
| [STOP](https://arxiv.org/abs/2310.02304) | 2023 | **Core** |
| [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) | 2024 | **Enabling** |
| [TextGrad](https://arxiv.org/abs/2406.07496) | 2024 | **Enabling** |
| [DSPy](https://arxiv.org/abs/2310.03714) | 2023 | **Enabling** |
| [Language Agent Tree Search](https://arxiv.org/abs/2310.04406) | 2023 | **Enabling** |
| [Large Language Models as Optimizers / OPRO](https://arxiv.org/abs/2309.03409) | 2023 | **Enabling** |
| [Promptbreeder](https://arxiv.org/abs/2309.16797) | 2023 | **Enabling** |

</details>

<details>
<summary><strong>Verification</strong> — 6 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Chain-of-Verification Reduces Hallucination in Large Language Models](https://arxiv.org/abs/2309.11495) | 2023 | **Enabling** |
| [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) | 2023 | **Enabling** |
| [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) | 2023 | **Enabling** |
| [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | 2023 | **Enabling** |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | **Enabling** |
| [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) | 2022 | **Enabling** |

</details>

<details>
<summary><strong>Agent / Architecture</strong> — 27 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse](https://arxiv.org/abs/2603.18000) | 2026 | **Core** |
| [AgentGA](https://arxiv.org/abs/2604.14655) | 2026 | **Core** |
| [EvoAgent: An Evolvable Agent Framework with Skill Learning and Multi-Agent Delegation](https://arxiv.org/abs/2604.20133) | 2026 | **Core** |
| [EVOCHAMBER](https://arxiv.org/abs/2605.11136) | 2026 | **Core** |
| [EvoFSM](https://arxiv.org/abs/2601.09465) | 2026 | **Core** |
| [EvoRepair](https://arxiv.org/abs/2605.30105) | 2026 | **Core** |
| [FailureMem](https://arxiv.org/abs/2603.17826) | 2026 | **Core** |
| [HyEvo](https://arxiv.org/abs/2603.19639) | 2026 | **Core** |
| [Hyperagents](https://arxiv.org/abs/2603.19461) | 2026 | **Core** |
| [JudgeFlow](https://arxiv.org/abs/2601.07477) | 2026 | **Core** |
| [Learning to Compose](https://arxiv.org/abs/2602.11114) | 2026 | **Core** |
| [Learning to Hand Off](https://arxiv.org/abs/2605.19140) | 2026 | **Core** |
| [SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution](https://arxiv.org/abs/2607.26784) | 2026 | **Core** |
| [SWE-Replay](https://arxiv.org/abs/2601.22129) | 2026 | **Core** |
| [Workflow-R1](https://arxiv.org/abs/2602.01202) | 2026 | **Core** |
| [AdaptFlow](https://arxiv.org/abs/2508.08053) | 2025 | **Core** |
| [Alita-G: Self-Evolving Generative Agent for Agent Generation](https://arxiv.org/abs/2510.23601) | 2025 | **Core** |
| [EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616) | 2025 | **Core** |
| [EvoFlow](https://arxiv.org/abs/2502.07373) | 2025 | **Core** |
| [Log-Augmented Generation](https://arxiv.org/abs/2505.14398) | 2025 | **Core** |
| [MermaidFlow](https://arxiv.org/abs/2505.22967) | 2025 | **Core** |
| [ScoreFlow](https://arxiv.org/abs/2502.04306) | 2025 | **Core** |
| [SEW](https://arxiv.org/abs/2505.18646) | 2025 | **Core** |
| [Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization](https://arxiv.org/abs/2402.17574) | 2024 | **Core** |
| [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) | 2024 | **Core** |
| [Self-evolving Agents with Reflective and Memory-Augmented Abilities](https://arxiv.org/abs/2409.00872) | 2024 | **Core** |
| [AutoTTS](https://arxiv.org/abs/2605.08083) | 2026 | **Adjacent** |

</details>

<details>
<summary><strong>Cross-component</strong> — 7 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [ARISE](https://arxiv.org/abs/2603.16060) | 2026 | **Core** |
| [CODESKILL](https://arxiv.org/abs/2605.25430) | 2026 | **Core** |
| [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) | 2026 | **Core** |
| [SkillRL](https://arxiv.org/abs/2602.08234) | 2026 | **Core** |
| [VLAW](https://arxiv.org/abs/2602.12063) | 2026 | **Core** |
| [Live-SWE-agent](https://arxiv.org/abs/2511.13646) | 2025 | **Core** |
| [WebEvolver](https://arxiv.org/abs/2504.21024) | 2025 | **Core** |

</details>

<details>
<summary><strong>Code / Agent</strong> — 5 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | 2025 | **Core** |
| [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) | 2025 | **Core** |
| [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139) | 2024 | **Core** |
| [AgentCoder](https://arxiv.org/abs/2312.13010) | 2023 | **Core** |
| [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128) | 2023 | **Core** |

</details>

<details>
<summary><strong>Model / Trainer</strong> — 18 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [EvoLM](https://arxiv.org/abs/2605.03871) | 2026 | **Enabling** |
| [SERPO](https://arxiv.org/abs/2607.26873) | 2026 | **Enabling** |
| [Teaching LLMs to Self-Evolve / MetaEvolve](https://arxiv.org/abs/2607.21971) | 2026 | **Enabling** |
| [TEMPO](https://arxiv.org/abs/2604.19295) | 2026 | **Enabling** |
| [rStar-Math](https://arxiv.org/abs/2501.04519) | 2025 | **Enabling** |
| [Self-Adapting Language Models / SEAL](https://arxiv.org/abs/2506.10943) | 2025 | **Enabling** |
| [Meta-Rewarding Language Models](https://arxiv.org/abs/2407.19594) | 2024 | **Enabling** |
| [Quiet-STaR](https://arxiv.org/abs/2403.09629) | 2024 | **Enabling** |
| [Self-Play Fine-Tuning](https://arxiv.org/abs/2401.01335) | 2024 | **Enabling** |
| [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) | 2024 | **Enabling** |
| [The Sharpening Mechanism](https://arxiv.org/abs/2412.01951) | 2024 | **Enabling** |
| [Beyond Human Data](https://arxiv.org/abs/2312.06585) | 2023 | **Enabling** |
| [RLAIF vs. RLHF](https://arxiv.org/abs/2309.00267) | 2023 | **Enabling** |
| [SELF](https://arxiv.org/abs/2310.00533) | 2023 | **Enabling** |
| [Self-Alignment with Instruction Backtranslation](https://arxiv.org/abs/2308.06259) | 2023 | **Enabling** |
| [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610) | 2022 | **Enabling** |
| [Self-Instruct](https://arxiv.org/abs/2212.10560) | 2022 | **Enabling** |
| [STaR](https://arxiv.org/abs/2203.14465) | 2022 | **Enabling** |

</details>

<details>
<summary><strong>Improvement mechanism</strong> — 3 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Bilevel Autoresearch](https://arxiv.org/abs/2603.23420) | 2026 | **Core** |
| [EvoTrainer](https://arxiv.org/abs/2606.03108) | 2026 | **Core** |
| [GEAR](https://arxiv.org/abs/2605.13874) | 2026 | **Core** |

</details>

<details>
<summary><strong>AI R&D</strong> — 26 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Auto Research](https://arxiv.org/abs/2605.05724) | 2026 | **Core** |
| [CliffSearch](https://arxiv.org/abs/2604.01210) | 2026 | **Core** |
| [LLMZero](https://arxiv.org/abs/2606.18388) | 2026 | **Core** |
| [POISE](https://arxiv.org/abs/2603.23951) | 2026 | **Core** |
| [Reward Synthesis](https://arxiv.org/abs/2605.02073) | 2026 | **Core** |
| [RF-Agent](https://arxiv.org/abs/2602.23876) | 2026 | **Core** |
| [SMCEvolve](https://arxiv.org/abs/2605.15308) | 2026 | **Core** |
| [TREX](https://arxiv.org/abs/2604.14116) | 2026 | **Core** |
| [AI4AI-Bench](https://arxiv.org/abs/2608.20318) | 2026 | **Adjacent** |
| [AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461) | 2026 | **Adjacent** |
| [AutoResearch](https://arxiv.org/abs/2608.17906) | 2026 | **Adjacent** |
| [AutoScientists](https://arxiv.org/abs/2605.28655) | 2026 | **Adjacent** |
| [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191) | 2026 | **Adjacent** |
| [Frontis-MA1](https://arxiv.org/abs/2607.28568) | 2026 | **Adjacent** |
| [FT-Dojo](https://arxiv.org/abs/2603.01712) | 2026 | **Adjacent** |
| [MLEvolve](https://arxiv.org/abs/2606.06473) | 2026 | **Adjacent** |
| [Towards End-to-End Automation of AI Research / AI Scientist-v2](https://doi.org/10.1038/s41586-026-10265-5) | 2026 | **Adjacent** |
| [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525) | 2026 | **Adjacent** |
| [AIDE](https://arxiv.org/abs/2502.13138) | 2025 | **Adjacent** |
| [Anthropic Institute — When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement) | 2025 | **Adjacent** |
| [LERO](https://arxiv.org/abs/2503.21807) | 2025 | **Adjacent** |
| [CARD](https://arxiv.org/abs/2410.14660) | 2024 | **Adjacent** |
| [DiscoPOP](https://arxiv.org/abs/2406.08414) | 2024 | **Adjacent** |
| [REvolve](https://arxiv.org/abs/2406.01309) | 2024 | **Adjacent** |
| [The AI Scientist](https://arxiv.org/abs/2408.06292) | 2024 | **Adjacent** |
| [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) | 2023 | **Adjacent** |

</details>

<details>
<summary><strong>Multi-agent</strong> — 6 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043) | 2025 | **Core** |
| [DEBATE, TRAIN, EVOLVE: Self Evolution of Language Model Reasoning](https://arxiv.org/abs/2505.15734) | 2025 | **Core** |
| [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://arxiv.org/abs/2406.14228) | 2024 | **Core** |
| [SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents](https://arxiv.org/abs/2403.08715) | 2024 | **Enabling** |
| [Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate](https://arxiv.org/abs/2305.19118) | 2023 | **Enabling** |
| [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325) | 2023 | **Enabling** |

</details>

<details>
<summary><strong>Evaluation</strong> — 12 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks](https://arxiv.org/abs/2608.23200) | 2026 | **Core** |
| [PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640) | 2026 | **Core** |
| [RSIBench-Data](https://arxiv.org/abs/2607.25886) | 2026 | **Core** |
| [ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence](https://arxiv.org/abs/2603.24621) | 2026 | **Adjacent** |
| [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](https://arxiv.org/abs/2606.05080) | 2026 | **Adjacent** |
| [Long-Horizon-Terminal-Bench](https://arxiv.org/abs/2607.08964) | 2026 | **Adjacent** |
| [MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI](https://arxiv.org/abs/2605.08678) | 2026 | **Adjacent** |
| [OSWorld 2.0](https://arxiv.org/abs/2606.29537) | 2026 | **Adjacent** |
| [MCPMark](https://arxiv.org/abs/2509.24002) | 2025 | **Adjacent** |
| [METR Task-Completion Time Horizon](https://arxiv.org/abs/2503.14499) | 2025 | **Adjacent** |
| [SWE-Bench Pro](https://arxiv.org/abs/2509.16941) | 2025 | **Adjacent** |
| [TheAgentCompany](https://arxiv.org/abs/2412.14161) | 2024 | **Adjacent** |

</details>

<details>
<summary><strong>Embodied</strong> — 7 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [ASPIRE](https://arxiv.org/abs/2607.00272) | 2026 | **Core** |
| [ENPIRE](https://arxiv.org/abs/2606.19980) | 2026 | **Core** |
| [MineEvolve](https://arxiv.org/abs/2603.13131) | 2026 | **Core** |
| [RISE](https://arxiv.org/abs/2602.11075) | 2026 | **Core** |
| [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) | 2026 | **Core** |
| [Self-Improving Vision-Language-Action Models via Residual RL](https://iclr.cc/virtual/2026/poster/10008318) | 2026 | **Core** |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | **Core** |

</details>

<details>
<summary><strong>Open-ended search</strong> — 11 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [PACEvolve](https://arxiv.org/abs/2601.10657) | 2026 | **Adjacent** |
| [AlphaEvolve](https://arxiv.org/abs/2506.13131) | 2025 | **Adjacent** |
| [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) | 2024 | **Adjacent** |
| [Higher Order and Self-Referential Evolution](https://openreview.net/forum?id=3tk6AES1Aj) | 2024 | **Adjacent** |
| [AutoML-Zero](https://arxiv.org/abs/2003.03384) | 2020 | **Adjacent** |
| [AI-GAs](https://arxiv.org/abs/1905.10985) | 2019 | **Adjacent** |
| [POET](https://arxiv.org/abs/1901.01753) | 2019 | **Adjacent** |
| [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474) | 2016 | **Adjacent** |
| [Quality Diversity](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00040/full) | 2016 | **Adjacent** |
| [MAP-Elites](https://arxiv.org/abs/1504.04909) | 2015 | **Adjacent** |
| [POWERPLAY](https://arxiv.org/abs/1112.5309) | 2011 | **Adjacent** |

</details>

<details>
<summary><strong>Self-modeling</strong> — 9 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Emergent Introspective Awareness in Large Language Models](https://arxiv.org/abs/2601.01828) | 2026 | **Enabling** |
| [Self-Reference in Large Language Models](https://arxiv.org/abs/2607.04277) | 2026 | **Enabling** |
| [Structure Enables Effective Self-Localization of Errors](https://arxiv.org/abs/2602.02416) | 2026 | **Enabling** |
| [Tell me about yourself](https://arxiv.org/abs/2501.11120) | 2025 | **Enabling** |
| [Looking Inward](https://arxiv.org/abs/2410.13787) | 2024 | **Enabling** |
| [Recursive Introspection](https://arxiv.org/abs/2407.18219) | 2024 | **Enabling** |
| [Self-Recognition in Language Models](https://arxiv.org/abs/2407.06946) | 2024 | **Enabling** |
| [Do LLMs Know What They Don't Know?](https://arxiv.org/abs/2305.18153) | 2023 | **Enabling** |
| [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) | 2022 | **Enabling** |

</details>

<details>
<summary><strong>Safety</strong> — 14 works</summary>

| Work | Year | Relevance |
|---|---:|---|
| [Optimal Policies Tend to Seek Power](https://arxiv.org/abs/1912.01683) | 2019 | **Foundational** |
| [Reward Tampering Problems and Solutions in Reinforcement Learning](https://arxiv.org/abs/1908.04734) | 2019 | **Foundational** |
| [Risks from Learned Optimization in Advanced Machine Learning Systems](https://arxiv.org/abs/1906.01820) | 2019 | **Foundational** |
| [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) | 2016 | **Foundational** |
| [SAHOO](https://arxiv.org/abs/2603.06333) | 2026 | **Enabling** |
| [TamperBench](https://arxiv.org/abs/2602.06911) | 2026 | **Enabling** |
| [Evaluating Goal Drift in Language Model Agents](https://arxiv.org/abs/2505.02709) | 2025 | **Enabling** |
| [Your Agent May Misevolve](https://arxiv.org/abs/2509.26354) | 2025 | **Enabling** |
| [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358) | 2024 | **Enabling** |
| [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) | 2024 | **Enabling** |
| [Model Evaluation for Extreme Risks](https://arxiv.org/abs/2305.15324) | 2023 | **Enabling** |
| [AGI Agent Safety by Iteratively Improving the Utility Function](https://arxiv.org/abs/2007.05411) | 2020 | **Enabling** |
| [Performance of Bounded-Rational Agents With the Ability to Self-Modify](https://arxiv.org/abs/2011.06275) | 2020 | **Enabling** |
| [Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142) | 2016 | **Enabling** |

</details>

---

## Companion resources

- [The Path to Recursive Self-Improving Agents — living survey & project page](https://github.com/D2I-ai/awesome-recursive-self-improving-agents)
- [RSI-Exam — code, data and evaluation resources](https://github.com/aiming-lab/RSI-Exam)

## Curation notes

- [Source review](SOURCE_REVIEW.md): the featured 20 received title/abstract/relevance checks on 2026-09-10; this does not certify all 213 entries or reproduce results.
- Freshness and importance are separate: the automated arXiv feed surfaces new work; this file is the curated long-lived index.
- Labels are maintained by RSI Observatory and can be corrected through Issues/PRs.
- The index is cross-checked against public field maps including Awesome RSI and The Path to Recursive Self-Improving Agents.

_Index snapshot: 2026-09-09 · 213 research works._
