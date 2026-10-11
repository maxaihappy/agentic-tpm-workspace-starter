# Agentic TPM Workspace Starter

A reusable setup for a Workspace Agent that helps a TPM or project lead onboard projects, reconcile status, prepare reports, coordinate requested follow-ups, and assess closure. Project knowledge stays in durable external records so the agent can be rebuilt without moving the project's history.

**Version:** 0.2.0. **Status:** portable starter, with fictional examples. This repository contains declarative instructions, seven skills, reference files, templates, and local packaging tools. It is not a hosted runtime, one-click deployment service, or claim of production qualification.

## Why use a shared Workspace Agent?

Agentic TPM packages a repeatable operating process for work that requires multiple people to coordinate against maintained commitments and shared records. Each person keeps their own working context; the agent applies common methods to the same project sources. Human owners retain decisions and accountability.

The useful dividing line is **shared continuity and accountability**, not how long a task lasts. A three-day launch across teams may need this process; a months-long personal investigation may not.

| Work or use case | Suggested working mode | Why |
| --- | --- | --- |
| Explore an idea, prototype code, compare approaches, or draft a one-off analysis | Direct Codex or ChatGPT use | Flexible scope with little shared coordination overhead |
| Maintain personal research, notes, preferences, or role context | Your private ChatGPT Project or Codex setup | Keeps your individual perspective under your control |
| Run a cross-team launch or recurring delivery review | Workspace Agent with registered project sources | Consistent status, evidence, commitments, and follow-through across stakeholders |
| Take over an in-flight project or return in a fresh conversation | Workspace Agent | Recovers project context from verified external records |
| Prepare sponsor, TPM, and engineering views of one program | Workspace Agent | Different emphasis grounded in compatible source facts |
| Assess handoff or closure | Workspace Agent | Checks acceptance evidence and remaining obligations beyond a Done label |

“Direct” describes the working pattern. It does not imply ChatGPT runs locally, or that Codex cannot support durable shared work. The same skills, connectors, and records can be used directly; the dedicated agent's value is packaging and sharing that setup.

| Intended benefit | What provides it | How to check that it helps |
| --- | --- | --- |
| Less repeated project explanation | Registry, source mappings, and verified continuity records | A fresh thread recovers the correct project with little guidance |
| Consistent project understanding | Common source ownership and reconciliation rules | Two authorized users receive compatible facts for the same source revisions |
| Repeatable reporting and handoffs | Seven reusable skills and shared templates | Results remain useful when someone other than the author runs them |
| More reliable follow-through | Destination readback, action identity, and retry reconciliation | Controlled repeat requests do not create duplicate actions |
| Reuse across projects and agent rebuilds | Separate methods, private deployment bindings, and external project records | Another project or replacement agent can reuse the methods without copying private context |

These are design benefits to validate, not exclusive platform capabilities or established production guarantees. Measure total effort including setup, review, correction, and maintenance. More generated reports alone do not demonstrate value. Proactive follow-through and scheduled operation require separate runtime evidence.

## Data sources: purpose, ownership, and access

| Source | Purpose and owned information | Boundary |
| --- | --- | --- |
| Individual ChatGPT Project or Codex setup | Private role context, goals, working notes, experiments, and personal preferences | User-private by design; verify the actual sharing settings. Never copy automatically into shared records |
| Jira | Authoritative project tracking and execution status: workflow state, assignee, priority, and execution dates | Reports and caches cite Jira; agent delivery-risk assessments remain separate from recorded status |
| Confluence | Shared human-facing context, plans, evidence links, documented decisions, reports, and history | Distinguish proposals, approved decisions, superseded information, and evidence; it is not a competing tracker |
| SharePoint | Shared registry, project metadata/configuration, source mappings, runbooks, checkpoints, provenance, and action history | Operational continuity, not personal memory or a second authoritative execution-status store |
| Slack, email, calendar, and approved meeting records | Supporting evidence and requested stakeholder coordination | A message is not automatically a commitment; a calendar invitation is not proof of a meeting or decision |
| This GitHub repository | Reusable agent instructions, skills, public templates, and fictional examples | Contains no live project records, private deployment bindings, or deployed-agent state |

Shared means **available to authorized users**, not everyone who can invoke the agent. Verify the effective connector identity and destination audience on each path; an agent must not expand source access. Avoid copying restricted evidence into broader reports or shared caches. Different access rights can legitimately produce different coverage, which must be disclosed without exposing restricted material.

For example: Jira records “Blocked,” a message says “looks done,” and a Confluence report says “on track.” Preserve Jira's recorded status, cite and date the conflicting evidence, and flag the reconciliation needed. Do not silently redefine the status. Likewise, a newer proposed launch date does not replace an approved baseline.

These products are the reference deployment, not employer-specific dependencies. Other trackers, wikis, and record stores can substitute when source ownership, access, identity, revision handling, and write verification are explicitly mapped and retested.

## How personal work and shared project work fit together

1. Keep individual context in your own private ChatGPT Project or Codex setup. A personal workspace can be durable even when the current task is short.
2. For coordinated project work, invoke the shared agent from a Project thread **if your environment supports that workflow**. Verify which instructions, files, and context actually reach it; invocation does not prove full context transfer.
3. Supply the registered project identity, your role, the task, relevant preferences, and sharing constraints. If invocation is unavailable, use a direct agent conversation with that explicit context.
4. The agent resolves shared project configuration in SharePoint, reads Confluence context and Jira tracking, and uses permitted supporting evidence. It tailors the response to you without changing shared facts.
5. When an experiment becomes an accepted project decision or commitment, deliberately publish the approved content to its owning system and verify the result. Personal opinions and exploratory notes stay private unless explicitly selected for sharing.

An engineering lead might ask for technical dependencies while a TPM asks for delivery exposure. Their views should differ in emphasis, with compatible facts where their permissions and source versions overlap. Private context must not leak through reports, action logs, caches, or another user's response. See the [context and isolation test procedure](docs/personal-project-context.md).

## Start here

1. Read [the architecture](docs/architecture.md) and [build/install guide](docs/build-and-install.md).
2. Inspect the [agent instructions](agent/instructions.md), [operating contract](agent/operating-contract.md), and seven skill directories.
3. Run the local checks and package builder below. They need Python 3.10+ and only its standard library; no credentials or network access.
4. Paste the [creation prompt](prompts/create-workspace-agent.md) into your supported Workspace Agent creation assistant. Codex can also prepare the artifacts and guide installation. Supply a tag/commit or the generated archive.
5. Connect your own approved sources, then test the [fictional first run](prompts/first-run.md) before onboarding real project data.

```bash
python3 scripts/validate.py
python3 scripts/package.py
```

The build writes dist/agentic-tpm-workspace-starter-0.2.0.zip, seven ZIPs in dist/skill-packages, and a SHA-256 manifest. Source files are human-readable and can be installed manually if the creation assistant cannot retrieve GitHub.

## What is included

| Path | Purpose |
| --- | --- |
| agent/instructions.md | Standing role, routing, evidence and reliability instructions |
| agent/operating-contract.md | Source ownership, persistence and native controls |
| agent/acceptance-tests.md | Behavioral acceptance scenarios; not an executed test result |
| skills/ | Seven reusable skills with metadata and supporting files |
| deployment/deployment.example.json | Empty organization-specific bindings; fill a private copy |
| docs/ | Architecture, connectors, installation, SharePoint and Confluence layouts, personal-context testing |
| templates/sharepoint/ | Registry, configuration, context, source map, preferences, state, evidence, actions, runs and report manifests |
| templates/confluence/ | Project home, daily, weekly and meeting templates |
| examples/example-launch/ | Complete fictional project context, connected records, evidence and sample project pages |
| prompts/ | Creation, first exercise and optional schedule prompts |
| scripts/ | Offline validation and reproducible packaging |
| templates/validation-receipt.json | Record actual installation and test outcomes |

## Seven capabilities

| Skill | Use it for |
| --- | --- |
| tpm-runtime-onboarding | Resolve missing project identity and verified per-user defaults |
| tpm-onboarding-planning | Register new work or preserve an in-flight handover |
| tpm-status-attention | Find changes, blockers, stale evidence, risks and decisions |
| tpm-daily-snapshot | Reconcile an exact time window into one dated snapshot |
| tpm-reporting | Prepare weekly, milestone or audience-specific reports |
| tpm-stakeholder-followup | Draft or execute specifically requested coordination |
| tpm-closeout | Assess acceptance, handoff and remaining obligations |

A new project gets configuration and a runbook. It does not need a new copy of every skill or a separate agent.

## Prerequisites and platform boundaries

You need access to a workspace that supports creating/editing the intended agent, plus the apps you choose to connect and source-system permissions for the exact project. This package does not provide those entitlements. User interface labels and connector actions may change; inspect the current surface. [Official Workspace Agent documentation](https://learn.chatgpt.com/workspace-agents) is the product reference; this repository documents a particular setup pattern.

The main deployment uses SharePoint for durable metadata, Confluence for the team-facing project record, Jira for execution fields, and optional Slack/Outlook evidence. Other systems can be mapped deliberately, with ownership and verification contracts retested. See [connector summary](docs/connectors.md).

Native platform and connector controls remain effective. This starter does not implement custom authority modes, persisted blanket grants, or approval bypasses. Task authorization, tool permission and accountable business decisions are separate. Draft-only work stays draft-only. A configured connector is not a proven connection for every user.

## Your project data belongs outside this public repository

Use a private deployment copy and your approved record store. Do not commit actual tenant domains, emails, project IDs, source extracts, account mappings, credentials, tokens, cookies, internal screenshots or operational audit history. Example Launch is entirely fictional; example.invalid links intentionally do not resolve.

Templates contain nulls and named placeholders by design. Resolve required bindings before live access. Store classification and retention choices in private configuration. Never replace an incomplete real record with a blank template.

## A useful first task

Ask: “For this registered project, what changed since the previous cutoff, what needs attention today, and which claim is uncertain?” Start with the fixture and draft-only behavior. Then test one exact approved read, fresh-conversation recovery, and an explicitly requested reversible write with destination readback.

A daily snapshot should lead with current status, due work and the top risk. The appendix holds traceability and coverage. A weekly report uses verified daily snapshots and admits missing days. An invitation does not prove a meeting occurred; a chat suggestion does not create a commitment; a Done label does not prove closure acceptance.

## What the checks prove

The local validator checks required files, JSON parsing, linked fixture identity, local Markdown links, skill layout, and common accidental private-data patterns. The packaging script validates first and builds deterministic archives with SHA-256 hashes. These checks do not prove hosted reasoning, live permissions, connector behavior, schedule execution, or fault recovery.

Use the [read-only implementation audit](prompts/audit-workspace-agent.md) to compare an installed agent with this model. Run [acceptance scenarios](agent/acceptance-tests.md) against the actual agent and record outputs. [Personal-project context transfer](docs/personal-project-context.md) must be tested independently. Configure and observe schedules separately; a saved cadence is not a running automation.

## Maintaining your version

Fork or copy the starter, keep private bindings separate, review changes, increment VERSION, update CHANGELOG.md, rerun checks, and build a new release. Upload instructions, references and skills as a matched version. Verify the installed inventory and a fresh chat before broader use. GitHub version control does not automatically deploy or roll back the hosted agent; see the release procedure in the install guide.

## Reuse and contribution

Licensed under [MIT](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md). Keep examples fictional and changes reproducible. A useful contribution includes the failing scenario, expected behavior, revised instructions or templates, and the limits of the validation performed.
