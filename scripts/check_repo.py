#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]

def err(msg): errors.append(msg)

for p in ROOT.glob('*.md'):
    if not p.read_text().strip(): err(f'Empty documentation: {p.name}')
readme = (ROOT/'README.md').read_text()
for name in ('TRENDING', 'PAPERS'):
    for edge in ('START', 'END'):
        if readme.count(f'<!-- {name}_{edge} -->') != 1:
            err(f'Missing or duplicate README marker: {name}_{edge}')
for filename in ('scorecard.json', 'paper-index.json'):
    if json.loads((ROOT/'data'/filename).read_text()) != json.loads((ROOT/'docs'/filename).read_text()):
        err(f'Website copy differs from data/{filename}')

# JSON parse
for p in (ROOT/'data').glob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: err(f'Invalid JSON {p.relative_to(ROOT)}: {e}')

# paper schema
try:
    papers=json.loads((ROOT/'data/paper-index.json').read_text())['papers']
    allowed={'Core','Enabling','Adjacent','Foundational'}
    seen=set()
    for i,p in enumerate(papers):
        for k in ('title','url','year','layer','relevance'):
            if k not in p: err(f'paper[{i}] missing {k}')
        if p.get('relevance') not in allowed: err(f"paper[{i}] bad relevance {p.get('relevance')}")
        key=(p.get('title','').strip().lower(),p.get('url'))
        if key in seen: err(f'duplicate paper record: {p.get("title")}')
        seen.add(key)
except Exception as e: err(f'paper-index schema failure: {e}')

# scorecard schema
try:
    sc=json.loads((ROOT/'data/scorecard.json').read_text())
    required={'name','role','scope','depth','persistent','loop','improver_mutable','evidence','confidence','basis'}
    for i,s in enumerate(sc['systems']):
        miss=required-set(s)
        if miss: err(f'scorecard system {i} missing {sorted(miss)}')
        if not re.fullmatch(r'E[0-5]',str(s.get('evidence',''))): err(f"scorecard {s.get('name')} bad evidence {s.get('evidence')}")
except Exception as e: err(f'scorecard schema failure: {e}')

# Relative links in markdown
link_re=re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for p in ROOT.rglob('*.md'):
    text=p.read_text(encoding='utf-8',errors='ignore')
    for m in link_re.finditer(text):
        u=m.group(1).split('#')[0].strip()
        if not u or u.startswith(('http://','https://','mailto:','#')): continue
        target=(p.parent/u).resolve()
        try: target.relative_to(ROOT.resolve())
        except ValueError: continue
        if not target.exists(): err(f'broken relative link {p.relative_to(ROOT)} -> {u}')

# Placeholders and banned ambiguous paper label
for p in ROOT.rglob('*'):
    if p.resolve()==Path(__file__).resolve(): continue
    if not p.is_file() or p.suffix.lower() not in {'.md','.html','.py','.json','.yml','.yaml','.txt'}: continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    if 'OWNER/RSI-Observatory' in text: err(f'owner placeholder remains in {p.relative_to(ROOT)}')
    if '"relevance": "Direct"' in text: err(f'legacy paper relevance Direct remains in {p.relative_to(ROOT)}')

if errors:
    print('Repository checks failed:')
    for e in errors: print(' -',e)
    sys.exit(1)
print('Repository checks: OK')
