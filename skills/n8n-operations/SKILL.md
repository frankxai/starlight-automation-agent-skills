---
name: n8n-operations
description: Build, inspect, validate, document, migrate, and template n8n workflows, workflow JSON exports, nodes, credentials placeholders, MCP Server Trigger nodes, MCP Client Tool nodes, and self-hosted automation patterns. Use when a user asks about n8n, workflow exports, workflow templates, branching automation, private workflow engines, or Make-to-n8n migration.
---

# n8n Operations

Use n8n for durable technical workflow ownership, reusable templates, private
data paths, and workflows that benefit from JSON review.

## Best Fit

- multi-step branching workflows
- API orchestration with transformations
- workflow templates for developers
- private or self-hosted automations
- MCP Server Trigger entry points
- n8n agents using MCP Client Tool nodes

## Workflow Review Checklist

For exported workflow JSON:

- parse JSON before editing
- confirm all nodes have stable ids
- remove credentials before sharing
- check dangling connections
- separate test and production webhooks
- define retry and error workflow behavior
- record idempotency key and dedupe policy
- include mock input and output payloads

## MCP In n8n

Use n8n's MCP server capabilities to expose selected workflows to agents.
Use MCP Client Tool nodes when an n8n agent needs tools from an external MCP
server. Keep tool lists small and explicit.

## Safety

- Do not commit credentials blocks.
- Do not publish live webhook URLs.
- Do not activate production workflows as a validation shortcut.
- Human approval is required for outbound sends, deletes, production deploys, account changes, and spending.

## Validation

When available, run:

```bash
python scripts/validate_n8n_workflow.py path/to/workflow.json
python scripts/scan_public_safety.py path/to/public/export
```

## Output Shape

Return: workflow map, node table, data contract, error route, MCP exposure plan,
validation commands, and migration notes.

