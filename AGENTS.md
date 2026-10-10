# Working on this starter

This is a portable declarative Workspace Agent setup. Read README.md, agent/instructions.md, and agent/operating-contract.md before changing behavior. Keep organization bindings in private deployment configuration and project facts in external records. Keep the seven capabilities reusable across projects.

Use python3. Run `python3 scripts/validate.py` and `python3 scripts/package.py` after a change. Check packaged skills and shared references together. These are package checks, not hosted behavioral tests. Record real results separately using templates/validation-receipt.json.

Never commit actual project records, account IDs, tenant domains, credentials, source extracts, private communications, or screenshots. Examples are fictional. Do not add custom authority modes or assume that enabling a connector permits all of its actions. Keep native controls and explicit task constraints effective.

Do not claim a repository commit has deployed an agent. A maintainer must inspect the installed version, test it, and record a deployment receipt. Update VERSION and CHANGELOG.md when releasing a changed package. Do not silently migrate existing project data.
