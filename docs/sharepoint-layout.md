# SharePoint layout and record lifecycle

Choose an approved team-owned library for shared use, or a personal location for an individual experiment. Verify access as each intended user. The root below is a proposed layout; setup does not create it automatically.

```text
Agentic_TPM/
├── registry/
│   └── projects.json
├── foundations/
│   └── standards-r0001.md.txt
├── shared/
│   ├── runbooks/general-delivery-v1.md.txt
│   └── templates/
└── projects/<project-id>/
    ├── project-config-r0001.json
    ├── context-r0001.md.txt
    ├── source-map-r0001.json
    ├── preferences-r0001.json
    ├── state-r0001.json
    ├── reporting-workflow-r0001.json
    ├── relationship-index-r0001.json
    ├── evidence/
    ├── actions/
    ├── runs/
    └── reports/
```

Use the JSON templates under templates/sharepoint and narrative templates beside them. Every project record carries project_id, schema_version and revision where structured. The registry points to the verified current configuration; that configuration points to current context, source map, preferences, state, reporting method and relationships. Live pointers use exact returned object URLs/IDs. The example fixture uses relative paths only for offline portability.

Use .json for structured records and UTF-8 .md.txt for Markdown narratives in this layout. This is a portability convention, not a universal SharePoint restriction. Keep .md for repository documentation. Preserve existing filenames unless a migration is explicitly requested.

## Save and resume

1. Read the existing record and revision. Preserve unknown and unrelated fields.
2. Prepare a new revision with the prior revision reference and exact project identity.
3. Save using actual connector-supported conflict behavior; read back and compare identity and content.
4. Advance the current pointer only after verification. If the pointer update fails, retain the previous valid pointer and record the new verified but unreferenced revision for repair.
5. Save partial results and exact unresolved targets. On resume, read destinations before retrying uncertain creates, sends, or pointer changes.

Separate report publication progress from evidence coverage. A verified partial report may have a publication timestamp while one source checkpoint remains behind. Do not advance an unavailable source's checkpoint beyond evidence actually read; retain gaps for backfill. One scalar report cutoff never proves all sources were covered.

Native version checks or conditional writes should be used when exposed. Without them, serialize writes operationally and re-read immediately before changes; this reduces risk but is not a transactional lock. Do not describe SharePoint files as a multi-system atomic transaction service.

Retention, audience, classification, redaction, and private-message promotion are deployment decisions. Copy only approved evidence into shared views. A private personal note needs explicit review before becoming shared project knowledge.
