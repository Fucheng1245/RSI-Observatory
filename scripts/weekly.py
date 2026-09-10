#!/usr/bin/env python3
"""Generate the weekly RSI Radar from local Observatory data.

This intentionally produces a compact signal layer rather than another full catalog.
"""
from __future__ import annotations
import datetime as dt
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'
RADAR=ROOT/'radar'

def fmt_delta(v):
    if v is None:return '—'
    return f'+{v}' if v>0 else str(v)

def main():
    now=dt.datetime.now(dt.timezone.utc)
    year,week,_=now.date().isocalendar()
    slug=f'{year}-W{week:02d}'
    latest=json.loads((DATA/'latest.json').read_text(encoding='utf-8'))
    papers=json.loads((DATA/'papers.json').read_text(encoding='utf-8')).get('papers',[])
    repos=latest.get('repositories',[])
    movers=sorted(repos,key=lambda r:((r.get('delta_7d') if r.get('delta_7d') is not None else -1),r.get('stars',0)),reverse=True)[:8]
    active=sorted(repos,key=lambda r:r.get('pushed_at') or '',reverse=True)[:6]
    lines=[f'# RSI Radar — {slug}','',f'> Generated {now.date().isoformat()} · Recursive Self-Improvement, self-improving agents, AI4AI and evaluation signals.','', '[← Observatory](../README.md) · [Scorecard](../SCORECARD.md) · [Trends](../TRENDS.md)','', '## Momentum board','', '| Project | Track | Stars | 7d Δ | Last push |','|---|---|---:|---:|---|']
    for r in movers:
        lines.append(f"| [{r['full_name']}]({r['html_url']}) | {r['category']} | {r.get('stars',0):,} | {fmt_delta(r.get('delta_7d'))} | {(r.get('pushed_at') or '')[:10] or '—'} |")
    lines += ['','## Recently active','']
    for r in active:
        lines.append(f"- **[{r['full_name']}]({r['html_url']})** — {r['category']} · last push {(r.get('pushed_at') or '')[:10] or '—'}")
    lines += ['','## Fresh research','']
    for p in papers[:8]:
        authors=', '.join(p.get('authors',[])[:3])
        lines.append(f"- **[{p.get('title','Untitled')}]({p.get('url','#')})** — {authors} · {(p.get('published') or '')[:10]}")
    lines += ['','## Questions worth watching','', '- Which systems expose the **updater itself** as a modifiable object?', '- Which benchmarks use hidden or external evaluation robust enough to resist evaluator gaming?', '- Do persistent memory/skill gains generalize beyond the tasks that generated them?', '- Are rollback, versioning and independent verification becoming first-class primitives?', '', '---', '', '> **Radar is signal, not a verdict.** Use the Scorecard and primary sources before interpreting momentum as capability.','']
    text='\n'.join(lines)
    RADAR.mkdir(exist_ok=True)
    (RADAR/f'{slug}.md').write_text(text,encoding='utf-8')
    (RADAR/'LATEST.md').write_text(text,encoding='utf-8')
    print(slug)

if __name__=='__main__':main()
