# Connector summary

This is a capability map, not an installed connection export. Connector names, actions, permissions, pagination, and write support vary by workspace and provider. Inspect the actual tool schema and record observed capabilities in the private deployment copy. Do not invent missing actions or substitute a different account.

| Connector role | Typical reads | Optional writes when supported and requested | Verify |
| --- | --- | --- | --- |
| SharePoint / OneDrive | List approved root; fetch exact files; paginate folders | Create folders, upload or update versioned records | Exact drive/item identity and file content; metadata alone is insufficient |
| Confluence | Read page/revision; list paginated child hierarchy; follow indexes | Create/update project pages and reports | Page ID, parent, content, revision, classification and links |
| Jira / execution tracker | Query approved issues; read status, owner, dates, history | Update requested fields or create scoped work | Exact issue identity and resulting fields |
| Slack | Read mapped channels and relevant thread replies | Requested channel/thread messages or reminders | Message/thread identity; acknowledgment is separate |
| Outlook Email | Enumerate approved received folders and Sent Items; read conversations | Requested draft or email when the connector exposes it | Saved draft/sent record and exact recipients; no delivery claim from a send attempt |
| Outlook Calendar | Read approved events and supported meeting evidence | Requested event changes when exposed | Event ID, attendees, time, timezone and resulting state |

Start with the sources needed for the first task. SharePoint is needed for the described durable registry deployment; the fictional offline exercise works without it. Confluence and Jira can be omitted from a draft-only exercise, with gaps stated. Slack and Outlook are optional evidence sources. There is no requirement to enable every write action.

A connected app is not proof of access for another user. Test each user with their own connection. Never put tokens, cookies, secret keys, passwords, sharing links, or real deployment identifiers in this repository. Configure authentication through the platform's supported connection flow.

## Coverage traps

- Keyword search cannot establish complete mailbox coverage. Enumerate each approved folder for the exact time window, follow all cursors, then filter for project relevance. Never broaden to an entire mailbox without approved scope.
- An old Slack parent can have a new reply; inspect relevant threads and disclose unsupported edits/deletions.
- A calendar invitation does not prove a meeting happened or anyone agreed to a decision.
- A sharing URL is not necessarily a connector folder locator. Retain returned site/drive/item identities.
- A page's visible label is not proof of classification metadata. Verify the supported metadata field or disclose the limitation.
- An app send action is separate from an agent entry channel. Configuring one does not enable the other.
