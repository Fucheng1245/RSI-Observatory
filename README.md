<p align="center">
  <img src="assets/hero.png" alt="RSI Observatory — the living map of Recursive Self-Improvement" width="100%" />
</p>

<p align="center">
  <a href="SCORECARD.md"><img alt="RSI Scorecard" src="https://img.shields.io/badge/RSI-Scorecard-7c3aed?style=for-the-badge"></a>
  <a href="PAPERS.md"><img alt="Research Library" src="https://img.shields.io/badge/Research-213_works-2563eb?style=for-the-badge"></a>
  <a href="radar/LATEST.md"><img alt="Weekly Radar" src="https://img.shields.io/badge/Weekly-Radar-0891b2?style=for-the-badge"></a>
  <a href="METHODOLOGY.md"><img alt="Conservative Methodology" src="https://img.shields.io/badge/Methodology-Conservative-0f766e?style=for-the-badge"></a>
</p>

<p align="center"><strong>Projects · Research · Benchmarks · Evidence · Safety · Labs · Timeline · Trends</strong></p>

> **RSI Observatory is an opinionated, evidence-driven living map of Recursive Self-Improvement.** It is built to answer three questions: **what is changing, how recursive is it, and how strong is the public evidence?**

**RSI = Recursive Self-Improvement**, not the trading Relative Strength Index.

**[Open the live website →](https://fucheng1245.github.io/RSI-Observatory/)**

**New here? [Take the five-minute tour →](START_HERE.md)**

---

## Why this exists

The field is growing fast, but the vocabulary is messy. “Self-refine”, “self-evolve”, “self-improving agent”, “AI researcher” and “RSI” are often used for systems with very different capabilities.

The Observatory does **not** solve that by making a bigger link dump. It adds an evidence layer:

<table>
<tr><td width="33%" valign="top"><h3>🗺️ Map</h3><p>Organize work by <b>what changes</b>: model, harness, data, trainer, improvement mechanism.</p><p><a href="LANDSCAPE.md"><b>Explore the landscape →</b></a></p></td>
<td width="33%" valign="top"><h3>🧬 Judge</h3><p>Separate L3 persistent self-improvement from L4 bounded RSI instead of trusting project names.</p><p><a href="SCORECARD.md"><b>Open the scorecard →</b></a></p></td>
<td width="33%" valign="top"><h3>🔥 Track</h3><p>Watch projects, fresh papers, benchmarks and weekly movement instead of freezing the field in time.</p><p><a href="radar/LATEST.md"><b>Read the Radar →</b></a></p></td></tr>
</table>

---

## The method in one screen

<p align="center"><img src="assets/observatory-framework.svg" alt="RSI Observatory three-axis framework" width="100%"></p>

**Axis A — what changes?** `Model · Harness · Data · Trainer · Improvement Mechanism`

**Axis B — how recursive?** `L1 Manual → L2 Assisted → L3 Programmatic Self-Improvement → L4 Bounded RSI → L5 General RSI`

**Axis C — how strong is the evidence?** `E0 Claim → E1 Artifact → E2 Executable Eval → E3 Persistent Held-out Gain → E4 Meta-Improvement → E5 Independent Replication`

> **Key boundary:** L4 begins when the **improvement mechanism itself** becomes modifiable. Automated research, persistent memory, or a closed loop can all be important without crossing that boundary.

[Read the full methodology →](METHODOLOGY.md)

---

## Scorecard snapshot

| System | Role | Scope | Depth | Improver mutable? | Evidence |
|---|---|---|---|---|---|
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) | Direct RSI | Harness / agent source code | L4 | yes | E4 |
| [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) | Direct RSI | Harness / agent code | L4 | yes | E4 |
| [OpenRSI / OpenMLE](https://github.com/FrontisAI/OpenRSI) | RSI-directed meta-evolution | Model + harness + trainer | L4-like framing; recursion unverified | trained improver; autonomous meta-loop unverified | E3 |
| [Recuris](https://github.com/Gen-Verse/Recuris) | Self-improving system | Data system / memory + harness | L3 | not demonstrated | E3 |
| [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) | Self-improving system | Harness / skills / coding workflow | L3-like | not demonstrated | E1 |
| [KnowAct](https://github.com/HITsz-TMG/KnowAct) | Self-improving system | Data system + harness | L3-like | not demonstrated | E2 |
| [Reflexion](https://arxiv.org/abs/2303.11366) | Enabling / self-improving memory | Data system / memory | L3 | no | E2 |
| [The AI Scientist](https://github.com/SakanaAI/AI-Scientist) | Adjacent AI R&D | Research process | Not RSI-scored | no | E2 |
| [LightRSI](https://github.com/zjunlp/LightRSI) | RSI substrate | Harness / runtime | N/A (substrate) | score instantiated loop | E1 |

**Why this is conservative:** the 2026 *Path to Recursive Self-Improving Agents* survey grades **Gödel Agent** and **Darwin Gödel Machine** L4. OpenRSI describes its current starting point as bounded **Meta-Evolution — training the improver itself — while explicitly not claiming general RSI is solved**. Other self-improving systems stay L3/L3-like here until comparable public evidence appears.

Author-reported evidence; no independent reproduction by this Observatory. [Review scope and corrections](SOURCE_REVIEW.md).

[Full scorecard + rationale →](SCORECARD.md)

---

## The improvement loop

<p align="center"><img src="assets/improvement-loop.svg" alt="Persistent improvement loop and recursive meta-loop" width="100%"></p>

A useful mental model is:

`Observe → Diagnose → Modify → Evaluate → Retain → Repeat`

At L3, that loop can improve persistent system components. At L4, the **meta-loop** can also change how diagnosis, proposal, evaluation or integration will work in future rounds.

---

## Research Library

The curated library contains **213 works** with separate relevance labels:

- **Core** — persistent self-improvement, self-modification, or recursive/meta-improvement is central. **Core does not automatically mean L4 RSI.**
- **Enabling** — memory, verification, tooling, optimization and other mechanisms useful to self-improvement.
- **Adjacent** — automated AI R&D, evaluation, open-ended search and safety work that materially informs RSI.
- **Foundational** — theory, surveys and historical work.

The website exposes the index as a searchable library; [`data/paper-index.json`](data/paper-index.json) is machine-readable.

[Browse the 213-work Research Library →](PAPERS.md)

---

## Featured systems by role

<table>
<tr><td width="50%" valign="top"><h3>🧬 Direct RSI</h3><p><b><a href="https://github.com/jennyzzt/dgm">Darwin Gödel Machine</a></b> — L4 in the 2026 survey; evolves agent code and retains validated variants.</p><p><b><a href="https://github.com/Arvid-pku/Godel_Agent">Gödel Agent</a></b> — L4 in the same survey; self-referential agent logic.</p></td>
<td width="50%" valign="top"><h3>🧪 RSI-directed</h3><p><b><a href="https://github.com/FrontisAI/OpenRSI">OpenRSI / OpenMLE</a></b> — executable AI4AI and bounded meta-evolution; explicitly framed as progress toward RSI rather than a claim that general RSI is solved.</p></td></tr>
<tr><td width="50%" valign="top"><h3>🧠 Self-improving systems</h3><p><b><a href="https://github.com/Gen-Verse/Recuris">Recuris</a></b> — persistent experiential/working-memory evolution.</p><p><b><a href="https://github.com/PrimeIntellect-ai/prime-agent">Prime Agent</a></b> — long-running self-improving coding agent.</p><p><b><a href="https://github.com/HITsz-TMG/KnowAct">KnowAct</a></b> — persistent personal-agent improvement.</p></td>
<td width="50%" valign="top"><h3>🔭 Substrates & adjacent systems</h3><p><b><a href="https://github.com/zjunlp/LightRSI">LightRSI</a></b> — runtime/substrate; score the instantiated loop, not the runtime.</p><p><b><a href="https://github.com/SakanaAI/AI-Scientist">AI Scientist</a></b> — important automated AI R&D, but not automatically RSI.</p></td></tr>
</table>

[Browse projects & systems →](PROJECTS.md)

---

## Benchmarks: different questions, not one leaderboard

| Benchmark | Main question |
|---|---|
| [PAST-Bench](https://arxiv.org/abs/2608.04003) | Does retained experience make later behavior measurably better? |
| [RSI-Exam](https://github.com/aiming-lab/RSI-Exam) | Can agents improve executable research methods over long horizons? |
| [AI4AI-Bench](https://arxiv.org/abs/2608.20318) | Can agents improve training algorithms under executable evaluation? |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | Can agents autonomously choose and execute post-training strategies under real budgets? |
| [RE-Bench](https://github.com/METR/RE-Bench) | How capable are agents at open-ended ML research engineering? |

[Understand what each benchmark really measures →](BENCHMARKS.md)

---

## Live Observatory

### Repository momentum

Seven-day changes require a snapshot from exactly seven days earlier. A dash means that baseline is not available.

<!-- TRENDING_START -->
| Repository | Category | Stars | 7d Δ | Forks | Last push |
|---|---|---:|---:|---:|---|
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | Self-improving agent | 21632 | +156 | 2387 | 2026-10-09 |
| [lobehub/awesome-rsi](https://github.com/lobehub/awesome-rsi) | Research map | 429 | +49 | 34 | 2026-10-06 |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | Automated AI R&D | 14686 | +38 | 2057 | 2025-12-19 |
| [FrontisAI/OpenRSI](https://github.com/FrontisAI/OpenRSI) | Core / AI4AI | 793 | +16 | 75 | 2026-09-17 |
| [selfimproving-agent/Awesome-Self-Improving-Agents](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents) | Research map | 537 | +15 | 54 | 2026-10-09 |
| [jennyzzt/dgm](https://github.com/jennyzzt/dgm) | Open-ended agent evolution | 2398 | +12 | 450 | 2025-08-13 |
| [aiming-lab/RSI-Exam](https://github.com/aiming-lab/RSI-Exam) | Benchmark | 175 | +9 | 7 | 2026-09-27 |
| [scaleapi/rsi-benchmark](https://github.com/scaleapi/rsi-benchmark) | Benchmark | 76 | +9 | 33 | 2026-10-09 |
| [Gen-Verse/Recuris](https://github.com/Gen-Verse/Recuris) | Memory evolution | 232 | +7 | 29 | 2026-08-30 |
| [CosmosMind-ai/RSI-Harness](https://github.com/CosmosMind-ai/RSI-Harness) | Harness evolution | 728 | +5 | 28 | 2026-09-23 |
| [D2I-ai/awesome-recursive-self-improving-agents](https://github.com/D2I-ai/awesome-recursive-self-improving-agents) | Research map | 49 | +3 | 3 | 2026-08-27 |
| [Arvid-pku/Godel_Agent](https://github.com/Arvid-pku/Godel_Agent) | Self-modifying agent | 230 | +2 | 54 | 2025-09-17 |
| [zjunlp/LightRSI](https://github.com/zjunlp/LightRSI) | Runtime | 72 | +1 | 15 | 2026-10-03 |
| [Gen-Verse/PAST-Bench](https://github.com/Gen-Verse/PAST-Bench) | Benchmark | 33 | +1 | 7 | 2026-08-05 |
| [HITsz-TMG/KnowAct](https://github.com/HITsz-TMG/KnowAct) | Personal agent | 486 | 0 | 41 | 2026-08-26 |
<!-- TRENDING_END -->

### Recent paper feed

Automatically discovered papers are candidates for review, not curated endorsements.

<!-- PAPERS_START -->
- **[Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](http://arxiv.org/abs/2610.12369v1)** — Kairui Hu, Siyuan Hu, Fangzhou Hong et al. (2026-10-08)
- **[TestPrism: Rethinking Test Evaluation Beyond a Single Reference](http://arxiv.org/abs/2610.12289v1)** — Han Li, Lingxiang Hu, Jiacheng Huang et al. (2026-10-08)
- **[Language Models as AI Research World Models](http://arxiv.org/abs/2610.12235v1)** — Zijun Wang, Zewen Liu, Minhua Lin et al. (2026-10-08)
- **[ReSI: Recursive Safety Improvement toward Resistant and Resilient AI](http://arxiv.org/abs/2610.12233v1)** — Jingnan Zheng, Dongcheng Zhang, Yi Zhang et al. (2026-10-08)
- **[DataSense-Bench: The First Step Toward an AI Scientist](http://arxiv.org/abs/2610.12190v1)** — Yudi Zhang, Mingyu Cao, Lu Yin et al. (2026-10-08)
- **[Recursive Self-Improvement through Multi-Agent Self-Supervision](http://arxiv.org/abs/2610.12176v1)** — Hyunin Lee, Jinglue Xu, Jeffrey Seely et al. (2026-10-08)
- **[Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks](http://arxiv.org/abs/2610.11794v1)** — Haoyu Zhao, Zhengxu Yu, Zhiyuan He et al. (2026-10-08)
- **[Who Verifies the Verifier? Co-Evolving Inspectable Graders with Self-Improving Agents](http://arxiv.org/abs/2610.11464v1)** — Xing Zhang, Guanghui Wang, Yanwei Cui et al. (2026-10-08)
- **[EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution](http://arxiv.org/abs/2610.10498v1)** — Python Song, Zhixuan Liang, Kelsey Fu et al. (2026-10-07)
- **[RSIGym: A Flexible Environment for Recursive Self-Improvement](http://arxiv.org/abs/2610.10310v1)** — Fanqing Meng, Lingxiao Du, Haocheng Lu et al. (2026-10-07)
- **[SkillSandbox: Skill Verification via Dynamic Scenario Synthesis](http://arxiv.org/abs/2610.10088v1)** — Serin Kim, Kwangwook Seo, Dokyung Song et al. (2026-10-07)
- **[Comprehension Audits to Mitigate Risks from Automated AI Research](http://arxiv.org/abs/2610.10064v1)** — Ronald J. Bodkin, Bahrad A. Sokhansanj, Gillian K. Hadfield (2026-10-07)
<!-- PAPERS_END -->

The automated layer tracks GitHub metadata, daily snapshots and a fresh paper feed. Human curation stays separate from automation.

- **Daily:** repository stars, forks, push time and historical snapshots.
- **Weekly:** a Radar digest for high-signal changes.
- **Curated:** project roles, L-depth, E-evidence, featured papers and benchmark interpretation.

> Machines maintain **breadth and freshness**. Humans maintain **importance and judgment**.

[Project trends →](TRENDS.md) · [Latest weekly Radar →](radar/LATEST.md) · [Labs & teams →](LABS.md) · [Safety →](SAFETY.md) · [Timeline →](TIMELINE.md)

---

## Disagree with a classification?

Good. The scorecard should be challengeable.

Open a **classification correction** Issue with the exact field, proposed replacement and supporting public evidence. The default policy is to **under-claim rather than inflate**.

[Contributing guide →](CONTRIBUTING.md) · [Methodology →](METHODOLOGY.md)

---

<p align="center"><strong>RSI Observatory</strong><br><sub>Map what matters. Track what moves. Keep the labels meaningful.</sub></p>
