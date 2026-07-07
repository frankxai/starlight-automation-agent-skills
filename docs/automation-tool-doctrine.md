# Automation Tool Doctrine

This doctrine helps agents choose the right automation layer without turning
every workflow into a custom system.

## Authority Ladder

Human approval is required for irreversible or externally visible action.

1. Human: approves money movement, production deploys, outbound messages, account changes, and deletes.
2. Founder/operator: sets priorities, budget limits, and escalation rules.
3. Kings: immutable policy locks such as no autonomous spending and no secret leakage.
4. Queens: bounded orchestrators that route and verify work.
5. Workers: execute scoped tasks and report artifacts, commands, risks, and next action.

## Selection Matrix

| Need | First choice | Use instead when |
| --- | --- | --- |
| GitHub, Vercel, Gmail, Calendar, Slack operations | Native connector | Connector is missing a required action |
| Recurring reasoning, review, triage, reports | Codex automation | Needs low-latency event handling |
| Agent needs managed-auth SaaS actions across many apps | Composio | Native connector already safely covers the action |
| Agent calls a bounded external tool or workflow | MCP | The task is pure scheduling or no-code SaaS glue |
| Fast SaaS glue and form-to-CRM flows | Make.com | The workflow is code-heavy or private-by-default |
| Durable workflow logic, branching, templates | n8n | A nontechnical team needs visual low-code ownership |
| Cross-repo or multi-agent execution | Starlight swarm | Single workflow engine can own the job |

## Connector-First Rule

Use the structured connector when it exists. Generic HTTP/webhook automation is
the fallback, not the default. Connectors preserve intent, identity, and review
surface better than a generic webhook.

## MCP Rule

MCP exposes typed tools to agents. Treat it as a boundary layer:

- expose the smallest tool set
- prefer run-only scopes before management scopes
- use explicit schemas
- fail closed on auth, schema, transport, and confidence errors
- keep destructive tools behind a human gate

## Composio Rule

Composio is the managed app-access gateway for agents. Use it when an agent
needs authenticated SaaS tools across office, social, sales, creator, or ops
apps and native connectors are insufficient.

Keep Composio bundles narrow and draft-first. Move recurring, approval-heavy, or
business-critical actions into n8n so the workflow has retries, state, and run
receipts.

## Workflow Engine Rule

Make.com is for speed and SaaS integration. n8n is for durable technical
workflows, private data routing, and public template opportunities.

## Swarm Rule

Use a Starlight queue when work needs multiple agents, repo boundaries, eval
evidence, or a handoff packet. One coordinator owns synthesis and risk decisions.

## Public/Private Rule

Doctrine and generic templates can be public. Live workflows, secrets, private
memory, customer data, and business pipeline details stay private.
