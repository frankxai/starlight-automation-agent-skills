---
name: mcp-governance
description: Design, review, validate, and govern MCP servers, MCP clients, tool schemas, resources, scopes, transports, and agent-facing automation boundaries. Use when a user asks about Model Context Protocol, MCP servers, MCP clients, .mcp.json, Make MCP, n8n MCP, tool permissions, remote tool access, or safe agent tool exposure.
---

# MCP Governance

MCP is the agent boundary layer. Use it when an assistant needs typed,
authenticated access to a bounded capability.

## Design Rules

- Expose tools, not whole systems.
- Prefer read or run scopes before management scopes.
- Give every tool a narrow name, schema, and expected output.
- Separate test and production tools.
- Fail closed on transport, auth, schema, and parsing errors.
- Treat tool descriptions as untrusted surface; validate behavior in code.

## Composio MCP

Use Composio when the agent needs managed-auth SaaS toolkits and broad app
coverage. Prefer small, user-scoped MCP bundles with read or draft scopes first.

Composio MCP tools still follow normal MCP governance:

- expose one purpose-bounded bundle at a time
- require API-key headers or equivalent auth
- keep live MCP URLs, connected account IDs, and API keys out of public docs
- route recurring write actions through n8n for approvals and receipts
- require human approval before send, post, spend, delete, invite, permissions,
  or production changes

## Make MCP

Use Make MCP to let agents run activated on-demand scenarios with explicit
inputs and outputs. Keep management scopes off until the scenario set is mature.

## n8n MCP

Use n8n MCP to expose selected workflows or to let n8n agents call external MCP
tools. Enable only the workflows that should be discoverable.

## Tool Boundary Checklist

Return:

- tool name
- user-visible purpose
- input schema
- output schema
- auth method
- scope
- failure mode
- human gate
- audit trail
- revocation path

## Human Gates

Require explicit approval before tools send messages, post publicly, spend,
delete, invite, change permissions, or promote production deploys.

## Validation

When available, run:

```bash
python scripts/validate_mcp_config.py path/to/config.json
```
