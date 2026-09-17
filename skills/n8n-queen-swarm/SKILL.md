---
name: n8n-queen-swarm
description: Dedicated Starlight Queen swarm lane and agent roles for n8n. Use when orchestrating n8n workflows as durable automation layer for multi-agent/Queen work, n8n-triggered agents via MCP/webhook, n8n as spine for content pipelines, API orchestration, or swarm handoffs. Architect, executor, optimizer, curator roles.
---

# n8n Queen Swarm

n8n serves as the durable, queue-backed automation engine for Starlight Queen swarms. Use queue mode (Primary + Workers + Redis + Postgres) for reliability at scale. Wire via webhooks, MCP Server Trigger (n8n exposes tools/workflows to agents), MCP Client Tool nodes (n8n calls external agents), or n8n API.

## Roles
- **n8n-Architect**: Design branching workflows, sub-workflows, error handling, MCP exposure, AI Agent nodes (with LiteLLM), idempotency, dedupe. Produce validated JSON + contracts.
- **n8n-Executor**: Trigger/monitor executions (webhook or API), handle approvals, route results to swarm bus or Hermes. Use n8n for stateful runs.
- **n8n-Optimizer**: Analyze executions (tie to Langfuse), tune concurrency, concurrency limits, worker scaling, subflow reuse, performance. Recommend queue best practices.
- **n8n-Community-Curator**: Curate/sanitize templates from official (n8n.io/workflows), awesome-n8n-templates, community. Validate, mock payloads, promote to public awesome or examples/. Maintain knowledgebase.

## Integration Patterns (Sophisticated)
- Queen → n8n: Swarm job → HTTP Request or dedicated webhook node in n8n (auth via Header/JWT). Or MCP Server Trigger for direct agent calls.
- n8n → Queen/Agents: Workflow ends with webhook to swarm_bus.py or Hermes endpoint. Or n8n AI Agent + MCP Client Tool calling external skills/agents.
- Models: Route via estate LiteLLM in n8n AI nodes. Trace with Langfuse.
- Secrets: Infisical (redacted patterns only). Never commit keys.
- Durable queue: Primary for UI/API/webhooks (public domain). Workers for execution. Redis queue. Postgres state. Shared encryption key. Concurrency >=5 per worker.
- MCP for agents: Expose selected workflows as MCP tools. Use in Claude Desktop, Hermes, Queen via mcp-remote + bearer.

## Safety & Gates
- Human approval for production activates, deletes, outbound sends, spend-impacting actions.
- Public-safe only: Sanitized JSON, mocks, no live webhooks/creds.
- Validation: Run validate_n8n_workflow.py + scan_public_safety.py before any promotion.
- Error routes, retries, idempotency keys always.

## Output Shape
Workflow map + node table, execution plan, MCP exposure or webhook contract, Langfuse trace link pattern, swarm handoff packet, validation commands, scaling notes.

## Commands & Wiring Examples
```bash
# Local test with n8n CLI
npx n8n export:workflow --id <id> --output workflow.json
python scripts/validate_n8n_workflow.py workflow.json

# Trigger example (sanitized)
curl -X POST https://<primary-domain>/webhook/<path> \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input": "payload"}'
```

Tie to swarm-comms-protocol for durable envelopes. Use starlight-queen-queue for coordination.

See n8n-knowledgebase.md for full curated resources and estate runbooks.
