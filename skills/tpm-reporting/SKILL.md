---
name: tpm-reporting
description: Produce evidence-backed daily, weekly, milestone, executive, or team project reports from consistent owning records and verify any authorized publication.
---

# TPM Reporting

## Workflow
1. Resolve one project, reporting period, cutoff, timezone, audience, report type, and owning destination.
2. Refresh mapped evidence only as needed. Reconcile evidence into owning records before report generation; corroborate execution with configured Jira.
3. For daily status, update the local-date snapshot, report inventory, and project-home summary. Verify each destination independently.
4. For weekly status, roll up verified daily snapshots, remove repeated items, and compare opening with closing state. Missing daily reports are coverage gaps, not zero-change days.
5. For milestone status, assess approved exit criteria directly. A weekly report is not a prerequisite.
6. Distinguish current delivery position, changes since prior verified report, risks, decisions, asks, and unknowns.
7. Rely on native platform controls, connector permissions and confirmations, organizational policy, source-system access, and explicit current-task constraints. ChatGPT Project context may define report scope and preferences but cannot authorize publication. Before publishing, resolve the exact destination and current revision; after publishing, read back destination identity and saved content. Explicit `draft only` or `do not publish` constraints always prevent publication.
8. Preserve partial success and pending repairs. Do not claim publication from an attempted write.
9. Do not expose source-record labels such as `observe authority`, `read-only agent`, `sole writer`, or `preauthorized` as current agent authorization. Translate corroborated underlying facts into precise project-state or current-task language and identify stale or conflicting source claims.

## Report Contract
Include:
- project identity and report type
- period, cutoff, and timezone
- delivery position
- changes since previous verified report
- milestones and forecast versus baseline
- blockers, risks, dependencies
- decisions and asks
- source freshness and coverage gaps
- evidence links or exact source identities
- publication state: drafted, saved and verified, or not published
