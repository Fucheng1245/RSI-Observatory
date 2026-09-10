#!/usr/bin/env python3
from pathlib import Path
from collections import Counter, defaultdict
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "paper-index.json"
OUT = ROOT / "PAPERS.md"

LAYER_ORDER = [
    "Foundations","Field maps","Memory / Skills","Harness","Verification",
    "Agent / Architecture","Cross-component","Code / Agent","Model / Trainer",
    "Improvement mechanism","AI R&D","Multi-agent","Evaluation",
    "Embodied","Open-ended search","Self-modeling","Safety","Other"
]
REL_RANK = {"Core":0,"Foundational":1,"Enabling":2,"Adjacent":3}

FEATURED = [
    ("https://arxiv.org/abs/cs/0309048","Foundations","The classic self-referential improvement formalism."),
    ("https://arxiv.org/abs/2310.02304","Harness","A concrete modern bridge from code-generation to recursive scaffold improvement."),
    ("https://arxiv.org/abs/2410.04444","Agent","Lets an agent inspect and rewrite its own logic."),
    ("https://arxiv.org/abs/2505.22954","Code","Empirical self-modification with an archive of validated improvements."),
    ("https://arxiv.org/abs/2607.05297","Skills","Makes the skill-improvement machinery itself part of the evolving system."),
    ("https://arxiv.org/abs/2606.09498","Harness","A clean self-improving-harness loop with held-out validation."),
    ("https://arxiv.org/abs/2608.24876","Memory","Persistent experience/working-memory evolution for long-horizon agents."),
    ("https://arxiv.org/abs/2605.27276","Cross-component","Jointly updates the agent harness and model weights."),
    ("https://arxiv.org/abs/2607.28568","AI R&D","Execution-grounded AI4AI training in ML engineering."),
    ("https://arxiv.org/abs/2608.20318","Evaluation","Tests whether agents can improve training algorithms under executable evaluation."),
    ("https://arxiv.org/abs/2608.04003","Evaluation","Tests whether retained experience actually improves later performance."),
    ("https://arxiv.org/abs/2603.08640","Evaluation","Measures autonomous post-training under a real compute/time budget."),
    ("https://arxiv.org/abs/2605.28655","Meta-loop","Improves the improvement mechanism rather than only the task solution."),
    ("https://arxiv.org/abs/2603.23420","Meta-loop","Explicit bilevel optimization of the research/improvement process."),
    ("https://arxiv.org/abs/2607.21461","Research agent","Uses an outer audit/improvement loop to drive targeted follow-up research."),
    ("https://arxiv.org/abs/2607.27191","Reality check","Useful negative evidence on current open-ended AI R&D limits."),
    ("https://arxiv.org/abs/2509.26354","Safety","Focuses directly on emergent risks from self-evolving agents."),
    ("https://arxiv.org/abs/2602.06911","Safety","Stress-tests whether safety survives fine-tuning and tampering."),
    ("https://arxiv.org/abs/2505.02709","Safety","Measures long-horizon objective drift."),
    ("https://arxiv.org/abs/1605.03142","Theory","Formal conditions for goal-preserving self-modification."),
]

def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    papers = payload["papers"]
    by_url = {p["url"]: p for p in papers}
    counts = Counter(p["relevance"] for p in papers)
    years = Counter(p["year"] for p in papers)

    lines = [
        "# RSI Research Library","",
        f"> **{len(papers)} papers and research works, structured by how they relate to Recursive Self-Improvement.**","",
        "Not everything that improves an AI system is RSI. This library separates **Core self-improvement**, **Enabling mechanisms**, **Adjacent AI R&D/evaluation**, and **Foundational work** so breadth does not come at the cost of precision.","",
        f"**Coverage:** {len(papers)} research works · {counts['Core']} Core · {counts['Enabling']} Enabling · {counts['Adjacent']} Adjacent · {counts['Foundational']} Foundational · {years[2026]} from 2026","",
        "[← Observatory](README.md) · [Landscape](LANDSCAPE.md) · [Scorecard](SCORECARD.md) · [Benchmarks](BENCHMARKS.md) · [Safety](SAFETY.md)","",
        "---","","## If you only read 20","",
        "| Work | Track | Why it matters |","|---|---|---|",
    ]
    for url, track, why in FEATURED:
        p = by_url.get(url)
        if p:
            lines.append(f"| [{p['title']}]({url}) | **{track}** | {why} |")
    lines += [
        "","---","","## How the library is labeled","",
        "| Label | Meaning |","|---|---|",
        "| **Core** | Persistent self-improvement, self-modification, or recursive/meta-improvement is central. **Core does not automatically mean L4 RSI.** |",
        "| **Enabling** | Memory, verification, tooling, optimization, or another mechanism useful for RSI, but not itself a recursive loop. |",
        "| **Adjacent** | AI R&D automation, open-ended search, or evaluation that materially informs the path to RSI. |",
        "| **Foundational** | Historical, theoretical, or survey work used to frame the field. |","",
        "> These labels are **RSI Observatory judgments**, not author claims. They are deliberately conservative and can be challenged through a classification-correction issue.","",
        "### Research routes","",
        "- **Self-modifying agents:** STOP → Gödel Agent → Darwin Gödel Machine → Self-Harness → MetaSkill-Evolve",
        "- **Memory & skills:** Reflexion → A-MEM → Recuris → SkillOpt → MetaSkill-Evolve",
        "- **Automated AI R&D:** AI Scientist → Execution-Grounded AI Research → Frontis-MA1 → AutoScientists → AI4AI-Bench",
        "- **Evaluation:** PAST-Bench → PostTrainBench → AI4AI-Bench → LongWoF-Bench → MLS-Bench",
        "- **Safety:** Self-Modification of Policy/Utility → Goal Drift → TamperBench → Misevolution → SAHOO","",
        "---","","## Full research index","",
        "The machine-readable source is [`data/paper-index.json`](data/paper-index.json).",""
    ]

    groups = defaultdict(list)
    for p in papers:
        groups[p["layer"]].append(p)
    for layer in LAYER_ORDER:
        items = groups.get(layer, [])
        if not items:
            continue
        items = sorted(items, key=lambda p:(REL_RANK.get(p["relevance"],9), -(p["year"] or 0), p["title"].lower()))
        lines += ["<details>", f"<summary><strong>{layer}</strong> — {len(items)} works</summary>","",
                  "| Work | Year | Relevance |","|---|---:|---|"]
        for p in items:
            lines.append(f"| [{p['title']}]({p['url']}) | {p.get('year') or '—'} | **{p['relevance']}** |")
        lines += ["","</details>",""]
    lines += [
        "---","","## Companion resources","",
        "- [The Path to Recursive Self-Improving Agents — living survey & project page](https://github.com/D2I-ai/awesome-recursive-self-improving-agents)",
        "- [RSI-Exam — code, data and evaluation resources](https://github.com/aiming-lab/RSI-Exam)","",
        "## Curation notes","",
        "- Freshness and importance are separate: the automated arXiv feed surfaces new work; this file is the curated long-lived index.",
        "- Labels are maintained by RSI Observatory and can be corrected through Issues/PRs.",
        "- The index is cross-checked against public field maps including Awesome RSI and The Path to Recursive Self-Improving Agents.","",
        f"_Index snapshot: {payload.get('generated_at','—')} · {len(papers)} research works._",""
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
