---
name: n8n-api-operator
description: Operate n8n via REST API (workflows, executions, credentials placeholders, activations). Use for programmatic create/update/execute/list, integration with Queen/swarm, CI/CD of workflows, monitoring. Redacted patterns only.
---

# n8n API Operator

Programmatic control of n8n (Primary instance recommended for API/webhooks). Auth: X-N8N-API-KEY header. Base URL from estate Primary domain.

## Key Endpoints (Sanitized)
- GET /api/v1/workflows
- POST /api/v1/workflows (import JSON)
- PUT /api/v1/workflows/{id}
- POST /api/v1/workflows/{id}/activate
- GET /api/v1/executions
- POST /api/v1/workflows/{id}/run (manual trigger with data)

## Patterns
- Export → sanitize → validate → import/activate via API in automation.
- Swarm/Queen: Trigger executions, poll status, route results.
- CI: Validate JSON, then API deploy to non-prod first.
- With MCP: Combine API ops with MCP-exposed workflows.

## Safety
- Never commit API keys or live IDs.
- Use Infisical for tokens.
- Separate test/prod webhooks/activations.
- Human gate for production activations.

## Output
API response summary, execution ID, status, handoff packet for swarm.

Validate with scripts. See n8n-knowledgebase.md for full API notes and queue wiring.
