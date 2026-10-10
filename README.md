# Agentic TPM Workspace Starter

A reusable setup for a Workspace Agent that helps a TPM or project lead onboard projects, reconcile status, prepare reports, coordinate requested follow-ups, and assess closure. Project knowledge stays in durable external records so the agent can be rebuilt without moving the project's history.

**Version:** 0.1.0. **Status:** portable starter, with fictional examples. This repository contains declarative instructions, seven skills, reference files, templates, and local packaging tools. It is not a hosted runtime, one-click deployment service, or claim of production qualification.

Intended GitHub home: [maxaihappy/agentic-tpm-workspace-starter](https://github.com/maxaihappy/agentic-tpm-workspace-starter). Verify the repository is available before using that URL in a builder.

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

The build writes dist/agentic-tpm-workspace-starter-0.1.0.zip, seven ZIPs in dist/skill-packages, and a SHA-256 manifest. Source files are human-readable and can be installed manually if the creation assistant cannot retrieve GitHub.

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

Run [acceptance scenarios](agent/acceptance-tests.md) against the actual agent and record outputs. [Personal-project context transfer](docs/personal-project-context.md) must be tested independently. Configure and observe schedules separately; a saved cadence is not a running automation.

## Maintaining your version

Fork or copy the starter, keep private bindings separate, review changes, increment VERSION, update CHANGELOG.md, rerun checks, and build a new release. Upload instructions, references and skills as a matched version. Verify the installed inventory and a fresh chat before broader use. GitHub version control does not automatically deploy or roll back the hosted agent; see the release procedure in the install guide.

## Reuse and contribution

Licensed under [MIT](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md). Keep examples fictional and changes reproducible. A useful contribution includes the failing scenario, expected behavior, revised instructions or templates, and the limits of the validation performed.
