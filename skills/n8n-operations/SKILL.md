---
name: n8n-operations
description: Build, inspect, validate, document, migrate, and template n8n workflows, workflow JSON exports, nodes, credentials placeholders, MCP Server Trigger nodes, MCP Client Tool nodes, and self-hosted automation patterns. Use when a user asks about n8n, workflow exports, workflow templates, branching automation, private workflow engines, or Make-to-n8n migration.
---

# n8n Operations

Use n8n for durable technical workflow ownership, reusable templates, private
data paths, and workflows that benefit from JSON review. Primary layer for
technical/branchy/private/template-worthy automation (see doctrine).

## Best Fit
- multi-step branching workflows
- API orchestration with transformations
- workflow templates for developers
- private or self-hosted automations
- MCP Server Trigger entry points
- n8n agents using MCP Client Tool nodes
- AI Agent + LangChain patterns with LiteLLM
- Durable spine for Queen swarms and agent handoffs

## Advanced Capabilities (Sophisticated Setup)
- Queue mode (Primary + Workers + Redis + Postgres): Estate standard for scale and reliability.
- API operations: Create, activate, execute, monitor via REST (X-N8N-API-KEY).
- MCP integration: Bidirectional with agents (Server Trigger to expose, Client Tool to call).
- AI/swarm: AI Agent nodes, RAG, tools wired to Queen via webhook/MCP. LiteLLM models, Langfuse tracing.
- Railway ops: Health, scaling, env (Infisical), deploys for the n8n w/workers project.
- Testing & evals: Structural + execution + safety + swarm integration tests. Tie to starlight-evals.

See dedicated skills for depth:
- n8n-api-operator
- n8n-workflow-architect
- n8n-ai-swarm-integrator
- n8n-testing-eval
- n8n-railway-ops
- n8n-queen-swarm (dedicated Queen lane)

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
- document MCP/webhook contracts for agents/swarm
- verify AI nodes use estate model routing

## MCP In n8n
Use n8n's MCP server capabilities to expose selected workflows to agents.
Use MCP Client Tool nodes when an n8n agent needs tools from an external MCP
server. Keep tool lists small and explicit. Combine with Queen swarms for
sophisticated orchestration.

## Safety
- Do not commit credentials blocks.
- Do not publish live webhook URLs.
- Do not activate production workflows as a validation shortcut.
- Human approval is required for outbound sends, deletes, production deploys, account changes, and spending.
- Use estate Infisical for secrets; redacted patterns only in this repo.

## Validation
When available, run:
```bash
python scripts/validate_n8n_workflow.py path/to/workflow.json
python scripts/scan_public_safety.py path/to/public/export
npx n8n export:workflow ... (for local testing)
```

Full curated resources, queue best practices, top templates, skills.sh alignment, and estate wiring in docs/n8n-knowledgebase.md.

## Output Shape
Return: workflow map, node table, data contract, error route, MCP exposure plan,
validation commands, migration notes, swarm/Queen integration plan, and scaling notes.

## Related Skills & Wiring
- automation-tool-router (first decision)
- n8n-queen-swarm (dedicated orchestration)
- starlight-queen-queue
- mcp-governance

See operating guide and canonical-home-map for placement.
