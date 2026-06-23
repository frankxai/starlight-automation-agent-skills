---
name: make-com-operations
description: Design, document, review, and govern Make.com automations, scenarios, modules, routers, webhooks, and Make MCP exposure. Use when a user asks about Make.com, Integromat, Make scenarios, SaaS workflow glue, form-to-CRM flows, Make MCP server setup, scenario inputs and outputs, or whether Make is preferable to n8n or Codex automations.
---

# Make.com Operations

Use Make.com when the workflow is mostly SaaS glue and speed matters more than
deep code ownership. Keep live scenario IDs, webhook URLs, and credentials out
of public artifacts.

## Best Fit

- lead capture and routing
- simple CRM or sheet updates
- purchase or signup follow-up
- approval notifications
- public-safe low-code demos
- MCP exposure of specific on-demand scenarios

## Use n8n Instead When

- the workflow needs code-heavy branching
- the export should become a public technical template
- sensitive data should stay self-hosted
- step volume makes action-based billing expensive
- git review of workflow JSON matters

## Scenario Design Checklist

Return a scenario map with:

- trigger
- modules
- filters and routers
- dedupe key
- retry policy
- error route
- audit trail
- human approval gate
- test payload
- rollback or disable step

## Make MCP Rule

Expose only activated on-demand scenarios with explicit inputs and outputs.
Prefer run-only scopes first. Avoid management scopes until the scenario has a
clear owner, tests, and approval gates.

## Safety

- Never run a production scenario while testing unless the user explicitly asks.
- Use mock payloads for public examples.
- Do not paste live webhook URLs or connection names into final answers.
- Human approval is required before outbound email, posting, deleting, inviting, or spending.

## Output Shape

Return: scenario map, data contract, risk gates, Make-vs-n8n rationale,
validation steps, and what remains manual.

