# Installation

Install these skills by copying or linking the skill folders into the Codex skill
directory. Restart Codex after installation.

Recommended installed skills:

- `automation-tool-router`
- `make-com-operations`
- `n8n-operations`
- `mcp-governance`
- `codex-automation-operator`
- `starlight-queen-queue`

After installation, use the guide:

- `docs/automation-operating-guide.md` for human and agent operating doctrine.
- `templates/automation-decision-record.md` before adding a durable automation.

Validate before installation:

```powershell
python scripts/validate_skill_bundle.py .
python scripts/scan_public_safety.py .
```

If using the repo as a plugin, validate the plugin manifest too:

```powershell
python path/to/plugin-creator/scripts/validate_plugin.py .
```
