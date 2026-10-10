# Confluence project layout

Create a home under the privately configured parent and classification. Create child areas only as needed. Preserve existing structures for in-flight projects; this tree is a starting template, not permission to reorganize them.

```text
Project Name (Agentic TPM)
├── 01. Stakeholders
├── 02. Project Plan
├── 03. Risks, Constraints and Dependencies
├── 04. Decisions
├── 05. Open Questions and Action Items
├── 06. Backlog and Ideas
├── 07. Status Report
│   ├── Daily Status Snapshot
│   │   └── YYYY-MM-DD
│   ├── Weekly Status
│   │   └── YYYY-MM-DD
│   └── Project Milestone Status
├── 08. Meeting Minutes
│   └── YYYY-MM-DD — Subject
├── 09. Slack Updates
├── 10. Working Documents
└── 11. Closure
```

Use separate tables for risks, constraints and dependencies. Keep questions and committed actions visibly separate on one page; put uncommitted ideas in Backlog. Optional email evidence or ad hoc report areas may be added when the project needs them. Do not silently add a second action tracker.

Each page includes recent changes, exact evidence links, stable item IDs and relevant dates. Store original meeting records and use dated corrections. Reports have inventories and dated children. The home links to current verified views. SharePoint stores stable category-root references; the agent discovers children and root indexes with pagination rather than relying on an exhaustive manually maintained list.

The complete fictional example is under examples/example-launch/confluence. Markdown is a content template, not a guaranteed native Confluence import format. Use the actual connector's supported Markdown or storage representation. Verify rendering, page parent, links, classification metadata, content and revision after publication.
