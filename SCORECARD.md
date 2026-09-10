# RSI Scorecard

> **A conservative evidence layer for self-improving AI.** The scorecard rewards evidence, not branding.

[← Observatory](README.md) · [Methodology](METHODOLOGY.md) · [Landscape](LANDSCAPE.md) · [Benchmarks](BENCHMARKS.md)

<p align="center"><img src="assets/evidence-ladder.svg" alt="RSI Evidence Ladder" width="100%"></p>

## Snapshot

| System | Role | Scope | Depth | Persistent | Loop | Improver mutable? | Evidence | Confidence |
|---|---|---|---:|---|---|---|---:|---|
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) | **Direct RSI** | Harness / agent code | **L4** | Yes | Closed, bounded | **Yes** | **E4** | High |
| [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) | **Direct RSI** | Harness / agent code | **L4** | Yes | Closed, bounded | **Yes** | **E4** | High |
| [OpenRSI / OpenMLE](https://github.com/FrontisAI/OpenRSI) | RSI-directed meta-evolution | Model + harness + trainer | **L4-like, bounded** | Yes | Closed, bounded domain | **Bounded meta-evolution** | **E4** | Medium |
| [Recuris](https://github.com/Gen-Verse/Recuris) | Self-improving system | Data / memory + harness | **L3** | Yes | Closed | **Not demonstrated** | **E3** | High |
| [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) | Self-improving system | Harness / skills | L3-like | Yes | Closed | **Not demonstrated** | E2 | Medium |
| [KnowAct](https://github.com/HITsz-TMG/KnowAct) | Self-improving system | Data + harness | L3-like | Yes | Closed | **Not demonstrated** | E2 | Medium |
| [Reflexion](https://arxiv.org/abs/2303.11366) | Enabling / self-improving memory | Data / memory | **L3** | Yes | Task-level | No | **E3** | High |
| [The AI Scientist](https://github.com/SakanaAI/AI-Scientist) | Adjacent AI R&D | Research process | Not RSI-scored | Artifacts persist | Research loop | No | E3 | High |
| [LightRSI](https://github.com/zjunlp/LightRSI) | RSI substrate | Harness / runtime | N/A | N/A | N/A | Score the instantiated loop | E1 | High |

### Why these labels are stricter than project names

- The 2026 *Path to Recursive Self-Improving Agents* survey grades **Gödel Agent** and **Darwin Gödel Machine** at **L4**.
- **OpenRSI** explicitly describes its current starting point as **bounded Meta-Evolution — training the improver itself — without claiming general RSI is solved**.
- A project described as “self-improving” is therefore not automatically Direct RSI here. L3-style persistent improvement and L4-style recursive improvement are separated.
- Runtimes such as **LightRSI** are substrates. A runtime does not inherit the capability score of every loop that might be built with it.

## What changes a score?

Useful evidence includes:

- a released implementation exposing the self-modification path;
- an executable evaluator, hidden/held-out test, or formal verifier;
- later-task gains caused by retained changes rather than extra test-time compute;
- a mutable search/update/evaluator mechanism;
- multiple generations of improvement without manual patching;
- independent reproduction.

## Machine-readable source

[`data/scorecard.json`](data/scorecard.json) is the source used by the website. Classification disputes should use the repository's correction Issue template.

> **Policy:** under-claim by default. A missing “yes” is not a negative judgment of a project; it means the required public evidence was not found or was not yet independently clear.
