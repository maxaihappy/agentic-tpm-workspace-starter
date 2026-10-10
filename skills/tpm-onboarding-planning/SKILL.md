---
name: tpm-onboarding-planning
description: Onboard a new project or take over an in-flight project while preserving identity, baselines, history, ownership, provenance, and incomplete progress.
---

# TPM Onboarding and Planning

## Trigger
Use for new-project onboarding, in-flight handover, project registration, initial plans, source mapping, or workspace proposals.

## Workflow
1. Resolve exactly one project from a verified ID, URL, alias, or registry mapping. Treat incomplete search or denied access as a coverage problem, not absence. Use ChatGPT Project context only for project identity, role, scope, preferences, and working context; verify project facts against authoritative records.
2. If unregistered, retain the original request and capture the minimum viable record. Purpose, scope, and accountable owner are enough to propose supervised support. Register incomplete work early and mark unknowns. Onboarding and tool setup do not create agent-level permissions or authorization state.
3. For handovers, preserve exact IDs, source URLs, original dates, approved baselines, completed work, decisions, commitments, and provenance. Never recreate or silently rebaseline.
4. Capture or update: purpose, strategy, scope, accountable owner, stakeholders, success criteria, deliverables, milestones, dependencies, risks, approved sources, runbooks, rollout, rollback, operational handoff, and acceptance requirements.
5. Keep baseline, forecast, actual, and proposed changes distinct. Proposed changes require a human decision before becoming a baseline.
6. Reuse verified records and mappings. Do not migrate or duplicate a project without explicit direction.
7. For a new Confluence workspace, offer `Project Name (Agentic TPM)` under the configured parent page with the organization-approved classification, after verifying access and destination. Create only needed child pages:
   - Stakeholders
   - Project Plan
   - Risks, Constraints and Dependencies, with three separate tables
   - Decisions
   - Open Questions and Action Items, with separate visible question and action tables
   - Backlog and Ideas
   - Status Report, with Daily Status Snapshot, Weekly Status, and Project Milestone Status indexes
   - Meeting Minutes
   - Slack Updates
   - Working Documents
   - Closure
8. Do not create a separate action tracker. Keep uncommitted ideas in backlog. A committed action requires confirmed owner and agreed due date; otherwise mark it awaiting confirmation.

## Completion
Return the selected project, what was verified, what remains unknown, and the smallest next supervised action. Do useful work without blocking on optional dates, schedules, complete requirements, or communication connectors.
