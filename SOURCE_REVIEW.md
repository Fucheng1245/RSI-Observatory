# Source review

Reviewed on **2026-09-10**. This record covers the homepage’s featured systems and benchmark links, all nine scorecard entries, and the 20-paper reading list. The remaining research index has not received this same item-by-item review.

The review checked public repository descriptions, paper titles and abstracts, and whether editorial descriptions follow those sources. It did not rerun experiments, audit all implementation code, or independently reproduce reported gains. Sources can change after this date.

## Scorecard decisions

- Each [scorecard entry](SCORECARD.md) now links its sources and states the review date and author-reported status in the JSON.
- DGM and Gödel Agent retain survey-aligned L4 and provisional editorial E4, with medium classification confidence. Neither score establishes independent replication or accelerating improvement.
- OpenRSI retains its bounded meta-evolution framing, but E4 is withheld: training an improver is insufficient evidence of autonomous repeated modification of the updater itself.
- Reflexion is E2: retention across trials is not by itself held-out cross-task gain. AI Scientist is E2: retained research artifacts do not demonstrate self-improvement of the agent.
- Prime Agent is E1 pending review of an improvement-specific evaluator. KnowAct remains E2 based on the released workflow and evaluation artifacts.
- Recuris remains L3/E3 based on reported held-out memory gains with a fixed meta-agent; LightRSI is scored as a substrate.

## Featured reading list

All 20 arXiv landing pages resolved and their titles/abstracts were checked. The descriptions below identify why the work is included, rather than certify the results.

| Source | Review note |
|---|---|
| [Gödel Machines](https://arxiv.org/abs/cs/0309048) | The classic self-referential improvement formalism. |
| [STOP](https://arxiv.org/abs/2310.02304) | Self-improvement of a code improver; reclassified Core. The authors distinguish this from full RSI. |
| [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) | Lets an agent inspect and rewrite its own logic. |
| [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) | Empirical self-modification with an archive of validated improvements. |
| [MetaSkill-Evolve](https://arxiv.org/abs/2607.05297) | Makes the skill-improvement machinery itself part of the evolving system. |
| [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | A clean self-improving-harness loop with held-out validation. |
| [Recursive Experiential-Working Memory Evolution / Recuris](https://arxiv.org/abs/2608.24876) | Persistent experience/working-memory evolution for long-horizon agents. |
| [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) | Jointly updates the agent harness and model weights. |
| [Frontis-MA1](https://arxiv.org/abs/2607.28568) | Execution-grounded AI4AI training in ML engineering. |
| [AI4AI-Bench](https://arxiv.org/abs/2608.20318) | Tests whether agents can improve training algorithms under executable evaluation. |
| [PAST-Bench](https://arxiv.org/abs/2608.04003) | Tests whether retained experience actually improves later performance. |
| [PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640) | Measures autonomous post-training under a real compute/time budget. |
| [AutoScientists](https://arxiv.org/abs/2605.28655) | Decentralized research-team coordination. Reclassified Adjacent / AI R&D; the abstract does not establish a mutable recursive updater. |
| [Bilevel Autoresearch](https://arxiv.org/abs/2603.23420) | Explicit bilevel optimization of the research/improvement process. |
| [AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461) | Iterative research and auditing plus a trained context tool. Classified Adjacent / AI R&D; task-time refinement is not evidence of persistent self-modification. |
| [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191) | Two case studies of autonomous research limits; these are not a universal capability bound. |
| [Your Agent May Misevolve](https://arxiv.org/abs/2509.26354) | Focuses directly on emergent risks from self-evolving agents. |
| [TamperBench](https://arxiv.org/abs/2602.06911) | Stress-tests whether safety survives fine-tuning and tampering. |
| [Evaluating Goal Drift in Language Model Agents](https://arxiv.org/abs/2505.02709) | Measures long-horizon objective drift. |
| [Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142) | Formal conditions for goal-preserving self-modification. |

## Homepage benchmarks

The homepage links resolve to [PAST-Bench](https://arxiv.org/abs/2608.04003), [RSI-Exam](https://github.com/aiming-lab/RSI-Exam), [AI4AI-Bench](https://arxiv.org/abs/2608.20318), [PostTrainBench](https://arxiv.org/abs/2603.08640) and [RE-Bench](https://github.com/METR/RE-Bench). Their descriptions distinguish retained experience, executable research improvement, training-algorithm improvement, post-training and ML research engineering. Benchmark inclusion is not a claim that passing it proves general RSI.

Corrections are welcome through the classification-correction issue template. Include the exact disputed claim and a primary source.
