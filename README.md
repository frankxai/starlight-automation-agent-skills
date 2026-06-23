# Starlight Automation Agent Skills

Codex skills and public-safe doctrine for choosing the right automation layer:
SaaS connectors, Codex automations, MCP tools, Make.com scenarios, n8n workflows,
and Starlight swarm queues.

This repo is intentionally not a vault of live workflows. It contains reusable
agent instructions, validation scripts, and sanitized operating doctrine that can
be shared publicly.

## Skill Bundle

- `automation-tool-router` - first-stop decision skill for tool selection.
- `make-com-operations` - Make.com scenario design, MCP exposure, and safety.
- `n8n-operations` - n8n workflow design, import/export checks, and templates.
- `mcp-governance` - MCP tool/server boundaries, auth, scopes, and fail-closed rules.
- `codex-automation-operator` - recurring Codex task design and review gates.
- `starlight-queen-queue` - bounded Starlight swarm queue jobs and handoffs.

## Core Rule

Use the narrowest reliable tool:

1. Native connector when a connector exists.
2. Codex automation when the job needs recurring reasoning and review.
3. MCP when an agent needs typed access to a bounded tool.
4. Make.com when the workflow is SaaS glue and speed matters.
5. n8n when the workflow is technical, private, branchy, or template-worthy.
6. Starlight swarm when work spans repos, agents, evaluation, or durable handoff.

## Public/Private Boundary

Public here:

- doctrine
- generic routing tables
- sanitized skill instructions
- mock payloads
- validation scripts

Private elsewhere:

- live Make or n8n scenarios
- webhook URLs
- credentials and env values
- customer or inbox data
- private memory vaults
- revenue and partner pipeline state

## Validation

```powershell
python scripts/validate_skill_bundle.py .
python scripts/scan_public_safety.py .
python scripts/validate_mcp_config.py examples/mcp/minimal.mcp.json
python scripts/validate_n8n_workflow.py examples/n8n/minimal-workflow.json
```

Restart Codex after installing or updating skills.

