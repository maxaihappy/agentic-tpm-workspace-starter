# Build and install

## 1. Inspect and choose a version

Read the README and inspect the downloaded source. Use a tag or commit so the builder works from a stable version. Run the two local commands in README. The generated archive includes skill ZIPs plus the readable source and manifest.

## 2. Prepare the deployment privately

Copy deployment/deployment.example.json to private/deployment.local.json. Fill only known values: exact SharePoint site/drive/root, Confluence destination and classification, optional Jira project, and selected connectors. The starter has no live bindings. Never commit the completed copy. Resolve missing fields only when they block the next task.

## 3. Use the creation assistant

Open your workspace's supported agent creation surface. Paste prompts/create-workspace-agent.md with this repository URL and the selected release or commit. If the assistant cannot retrieve GitHub, attach the generated source archive. Ask it to inspect source files before composing the agent.

Use agent/instructions.md as the standing instructions; attach agent/operating-contract.md and agent/acceptance-tests.md as references. Install all seven skills. For a manual install, upload the ZIP for each skill from dist/skill-packages. Each ZIP has SKILL.md at its root. Where the editor supports mentions, bind skill and file references to the actual installed resources. Plain names in Markdown are not proof of editor binding.

The builder may help assemble artifacts or operate supported UI, but repository preparation does not itself deploy the hosted agent. If direct creation is unavailable, it must return the exact paste-ready instructions, references, skill archives and remaining UI steps.

## 4. Connect only the required tools

Follow docs/connectors.md. Use end-user accounts and native confirmations. Inspect available actions and test an exact approved read first. A live test write must have a known target and task authorization; verify its content at the destination. Record configured, connected, read-tested and write-tested separately.

## 5. Run the fictional exercise

Use examples/example-launch and prompts/first-run.md. Run the acceptance scenarios against a draft/preview agent. Capture actual outputs and assess expected behavior. The local validator checks file integrity, not the model's reasoning. Do not fabricate a behavioral pass because the documents contain the right rules.

## 6. Onboard your first project

Use minimum identity, purpose, scope and accountable owner. Preserve existing plans and records for an in-flight project. Verify the registry pointer and restart in a fresh conversation. Add sources progressively. Use the configured Confluence parent, create only needed areas, and retain tracker ownership of execution fields.

## 7. Test optional personal context and schedules

Use docs/personal-project-context.md to test the actual entry point. Configure a schedule only after selecting exact project, timezone, reporting window, destinations, recipient if any, execution user, cadence and recovery behavior. The prompt under prompts/daily-snapshot-schedule.md is a template, not an active automation. Verify the schedule configuration and then observe an actual run. Avoid overlapping schedules for the same report window.

## Release and rollback

Record the package version, commit, manifest, installed instruction/skill/reference inventory and observed acceptance results in templates/validation-receipt.json. Keep an export of the prior agent setup. A rollback restores a reviewed setup through supported controls; it does not undo external writes. Reconcile project data and outstanding actions separately. Do not migrate records or permissions just because a new package was installed.
