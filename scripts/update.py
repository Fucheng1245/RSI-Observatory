#!/usr/bin/env python3
"""Update RSI Observatory data, historical snapshots, README blocks, and Pages data.

Uses Python stdlib only. In GitHub Actions, GITHUB_TOKEN is provided automatically.
"""
from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Any
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
HISTORY = DATA / "history"
README = ROOT / "README.md"
DOCS = ROOT / "docs"

GITHUB_API = "https://api.github.com"
ARXIV_API = "https://export.arxiv.org/api/query"
REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "Fucheng1245/RSI-Observatory")
USER_AGENT = f"RSI-Observatory/1.0 (+https://github.com/{REPO_SLUG})"


def _request_json(url: str) -> dict[str, Any]:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_repo(full_name: str, category: str, note: str) -> dict[str, Any]:
    url = f"{GITHUB_API}/repos/{full_name}"
    raw = _request_json(url)
    return {
        "full_name": raw["full_name"],
        "html_url": raw["html_url"],
        "description": raw.get("description"),
        "category": category,
        "note": note,
        "stars": raw.get("stargazers_count", 0),
        "forks": raw.get("forks_count", 0),
        "open_issues": raw.get("open_issues_count", 0),
        "language": raw.get("language"),
        "created_at": raw.get("created_at"),
        "updated_at": raw.get("updated_at"),
        "pushed_at": raw.get("pushed_at"),
        "topics": raw.get("topics", []),
        "delta_7d": None,
    }


def load_old_snapshot(today: dt.date) -> dict[str, Any] | None:
    target = today - dt.timedelta(days=7)
    candidates = []
    for p in HISTORY.glob("*.json"):
        try:
            d = dt.date.fromisoformat(p.stem)
        except ValueError:
            continue
        if d == target:
            candidates.append((d, p))
    if not candidates:
        return None
    _, path = max(candidates, key=lambda x: x[0])
    return json.loads(path.read_text(encoding="utf-8"))


def add_deltas(repos: list[dict[str, Any]], old: dict[str, Any] | None) -> None:
    if not old:
        return
    old_by_name = {r["full_name"]: r for r in old.get("repositories", [])}
    for repo in repos:
        prev = old_by_name.get(repo["full_name"])
        if prev and not prev.get("stale") and isinstance(prev.get("stars"), int):
            repo["delta_7d"] = repo["stars"] - prev["stars"]


def fetch_arxiv(max_results: int = 30) -> list[dict[str, Any]]:
    query = 'all:"recursive self-improvement" OR all:"self-improving agent" OR all:"self-evolving agent" OR all:"automated AI research"'
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    req = urllib.request.Request(f"{ARXIV_API}?{params}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml = resp.read()
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml)
    papers = []
    seen = set()
    for entry in root.findall("atom:entry", ns):
        title = " ".join((entry.findtext("atom:title", default="", namespaces=ns)).split())
        summary = " ".join((entry.findtext("atom:summary", default="", namespaces=ns)).split())
        url = entry.findtext("atom:id", default="", namespaces=ns)
        published = entry.findtext("atom:published", default="", namespaces=ns)
        authors = [a.findtext("atom:name", default="", namespaces=ns) for a in entry.findall("atom:author", ns)]
        key = url or title.lower()
        if not title or key in seen:
            continue
        seen.add(key)
        papers.append({
            "title": title,
            "url": url,
            "published": published,
            "authors": authors,
            "summary": summary,
        })
    return papers


def replace_block(text: str, name: str, body: str) -> str:
    start = f"<!-- {name}_START -->"
    end = f"<!-- {name}_END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    replacement = start + "\n" + body.rstrip() + "\n" + end
    if not pattern.search(text):
        raise RuntimeError(f"README block {name} not found")
    return pattern.sub(lambda _: replacement, text)


def fmt_delta(value: int | None) -> str:
    if value is None:
        return "—"
    return f"+{value}" if value > 0 else str(value)


def render_readme(repos: list[dict[str, Any]], papers: list[dict[str, Any]]) -> None:
    text = README.read_text(encoding="utf-8")
    ranked = sorted(repos, key=lambda r: (r.get("delta_7d") if r.get("delta_7d") is not None else -1, r.get("stars", 0)), reverse=True)
    rows = ["| Repository | Category | Stars | 7d Δ | Forks | Last push |", "|---|---|---:|---:|---:|---|"]
    for r in ranked[:15]:
        pushed = (r.get("pushed_at") or "")[:10] or "—"
        stale = " (cached; refresh failed)" if r.get("stale") else ""
        rows.append(f"| [{r['full_name']}]({r['html_url']}){stale} | {r['category']} | {r['stars']} | {fmt_delta(r.get('delta_7d'))} | {r['forks']} | {pushed} |")
    text = replace_block(text, "TRENDING", "\n".join(rows))

    if papers:
        prows = []
        for p in papers[:12]:
            date = (p.get("published") or "")[:10]
            authors = ", ".join(p.get("authors", [])[:3])
            if len(p.get("authors", [])) > 3:
                authors += " et al."
            prows.append(f"- **[{p['title']}]({p['url']})** — {authors} ({date})")
        paper_body = "\n".join(prows)
    else:
        paper_body = "No matching papers returned in this update."
    text = replace_block(text, "PAPERS", paper_body)
    README.write_text(text, encoding="utf-8")


def normalize_self_links() -> None:
    repo_slug = os.environ.get("GITHUB_REPOSITORY")
    if not repo_slug:
        return
    for path in (README, DOCS / "index.html"):
        if path.exists():
            text = path.read_text(encoding="utf-8")
            text = text.replace("Fucheng1245/RSI-Observatory", repo_slug)
            path.write_text(text, encoding="utf-8")


def main() -> int:
    normalize_self_links()
    today = dt.datetime.now(dt.timezone.utc).date()
    config = json.loads((DATA / "repos.json").read_text(encoding="utf-8"))
    previous = json.loads((DATA / "latest.json").read_text(encoding="utf-8"))
    previous_by_name = {r["full_name"]: r for r in previous.get("repositories", [])}
    repos = []
    failures = []
    for item in config["repositories"]:
        try:
            repos.append(fetch_repo(item["full_name"], item["category"], item.get("note", "")))
        except Exception as exc:  # keep one bad repo from breaking the whole observatory
            failures.append({"full_name": item["full_name"], "error": str(exc)})
            if item["full_name"] in previous_by_name:
                cached = dict(previous_by_name[item["full_name"]])
                cached["stale"] = True
                cached["delta_7d"] = None
                repos.append(cached)
        time.sleep(0.1)

    if len(failures) == len(config["repositories"]):
        print("All repository fetches failed; existing data preserved.", file=sys.stderr)
        return 1
    old = load_old_snapshot(today)
    add_deltas([r for r in repos if not r.get("stale")], old)
    snapshot = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "repositories": repos,
        "failures": failures,
    }
    HISTORY.mkdir(parents=True, exist_ok=True)
    (HISTORY / f"{today.isoformat()}.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    (DATA / "latest.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")

    try:
        papers = fetch_arxiv()
        paper_payload = {"generated_at": snapshot["generated_at"], "papers": papers}
    except Exception as exc:
        print(f"warning: arXiv fetch failed: {exc}", file=sys.stderr)
        paper_payload = json.loads((DATA / "papers.json").read_text(encoding="utf-8"))
        papers = paper_payload.get("papers", [])
    (DATA / "papers.json").write_text(json.dumps(paper_payload, indent=2) + "\n", encoding="utf-8")

    render_readme(repos, papers)
    DOCS.mkdir(exist_ok=True)
    (DOCS / "data.json").write_text(json.dumps({"generated_at": snapshot["generated_at"], "failures": failures, "papers_generated_at": paper_payload.get("generated_at"), "repositories": repos, "papers": papers[:20]}, indent=2) + "\n", encoding="utf-8")
    scorecard = DATA / "scorecard.json"
    if scorecard.exists():
        (DOCS / "scorecard.json").write_text(scorecard.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"updated {len(repos)} repos; {len(papers)} papers; {len(failures)} failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
