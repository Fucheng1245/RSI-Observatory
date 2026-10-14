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
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | Self-improving agent | 22008 | +416 | 2433 | 2026-10-14 |
| [lobehub/awesome-rsi](https://github.com/lobehub/awesome-rsi) | Research map | 669 | +267 | 51 | 2026-10-14 |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | Automated AI R&D | 14711 | +37 | 2061 | 2025-12-19 |
| [FrontisAI/OpenRSI](https://github.com/FrontisAI/OpenRSI) | Core / AI4AI | 813 | +32 | 77 | 2026-09-17 |
| [selfimproving-agent/Awesome-Self-Improving-Agents](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents) | Research map | 556 | +27 | 57 | 2026-10-12 |
| [jennyzzt/dgm](https://github.com/jennyzzt/dgm) | Open-ended agent evolution | 2416 | +25 | 452 | 2025-08-13 |
| [aiming-lab/RSI-Exam](https://github.com/aiming-lab/RSI-Exam) | Benchmark | 184 | +12 | 8 | 2026-09-27 |
| [Gen-Verse/Recuris](https://github.com/Gen-Verse/Recuris) | Memory evolution | 238 | +11 | 29 | 2026-08-30 |
| [zjunlp/LightRSI](https://github.com/zjunlp/LightRSI) | Runtime | 82 | +11 | 15 | 2026-10-03 |
| [scaleapi/rsi-benchmark](https://github.com/scaleapi/rsi-benchmark) | Benchmark | 82 | +9 | 42 | 2026-10-14 |
| [D2I-ai/awesome-recursive-self-improving-agents](https://github.com/D2I-ai/awesome-recursive-self-improving-agents) | Research map | 53 | +7 | 3 | 2026-08-27 |
| [Arvid-pku/Godel_Agent](https://github.com/Arvid-pku/Godel_Agent) | Self-modifying agent | 235 | +6 | 54 | 2025-09-17 |
| [Tencent/VideoHarness-RSI](https://github.com/Tencent/VideoHarness-RSI) | Harness evolution | 10 | +2 | 0 | 2026-09-07 |
| [Gen-Verse/PAST-Bench](https://github.com/Gen-Verse/PAST-Bench) | Benchmark | 34 | +1 | 7 | 2026-08-05 |
| [HITsz-TMG/KnowAct](https://github.com/HITsz-TMG/KnowAct) | Personal agent | 480 | -6 | 41 | 2026-08-26 |
<!-- TRENDING_END -->

### Recent paper feed

Automatically discovered papers are candidates for review, not curated endorsements.

<!-- PAPERS_START -->
- **[Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](http://arxiv.org/abs/2610.18868v1)** — Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh et al. (2026-10-13)
- **[The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](http://arxiv.org/abs/2610.18845v1)** — Sijie Zhao, Zeqi Zhou, Heli Qi et al. (2026-10-13)
- **[Who Improves the Robot? Toward Physical Recursive Self-Improvement](http://arxiv.org/abs/2610.18842v1)** — Hai Zhou, Fan Yang, Zeyi Chen et al. (2026-10-13)
- **[Self-Evolving Agent Harness](http://arxiv.org/abs/2610.18813v1)** — Chuyang Wei, Haoxiang Guan, Minghang Zhu et al. (2026-10-13)
- **[SEAR: Self-Evolving Agentic Robotics](http://arxiv.org/abs/2610.18792v1)** — Xinyi Wang, Bangzheng Li, Hanyu Wang et al. (2026-10-13)
- **[The Singularity Has a Distribution: Exact Timing Laws and Detection Limits for a Stochastic Intelligence Explosion](http://arxiv.org/abs/2610.18445v1)** — Xiaoyu Li, Zheng Gao, Chiwun Yang et al. (2026-10-13)
- **[APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation](http://arxiv.org/abs/2610.18097v1)** — Sirui Zhang, Fangyun Wei, Dong Chen et al. (2026-10-13)
- **[AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement](http://arxiv.org/abs/2610.18083v1)** — Wenhao Zhou, Jiajun Song, Haitao Wang et al. (2026-10-13)
- **[ECG-RSI: Recursive Self-Improvement through Targeted Electrocardiogram Waveform Evolution](http://arxiv.org/abs/2610.17718v1)** — Xiaoliang Wang, Zhuo Chen, Chuanyang Zheng et al. (2026-10-13)
- **[D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control](http://arxiv.org/abs/2610.17114v1)** — Xuan Wen, Baichao Wang (2026-10-12)
- **[Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems](http://arxiv.org/abs/2610.16491v1)** — Xin Xu, Ke Cheng, Hao Wang et al. (2026-10-12)
- **[Heterogeneous Agentic Coevolution](http://arxiv.org/abs/2610.16078v1)** — Wenqian Ye, Ziwei Guan, Zi Yang et al. (2026-10-12)
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
