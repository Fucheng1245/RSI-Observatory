# Observatory Data

The data layer is intentionally simple and reusable.

| File | Purpose |
|---|---|
| `repos.json` | Curated repositories tracked by the live Radar |
| `latest.json` | Most recent GitHub metadata snapshot |
| `history/YYYY-MM-DD.json` | Immutable daily snapshots used for momentum calculations |
| `papers.json` | Fresh discovery feed |
| `paper-index.json` | Curated long-lived research index |
| `scorecard.json` | Curated scope/depth/evidence classifications |

## Separation of concerns

**Automated fields** — stars, forks, timestamps, recent paper feed.

**Curated judgments** — project role, improvement scope, L-depth, E-evidence, confidence and rationale.

Automation must never silently overwrite a curated judgment. “Core” in the paper index means core to self-improvement research; it does **not** mean L4 RSI.
