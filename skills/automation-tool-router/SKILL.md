---
name: automation-tool-router
description: Choose the best automation layer across native connectors, Codex automations, MCP tools, Make.com scenarios, n8n workflows, and Starlight swarm queues. Use when a user asks which tool to use, how to automate a workflow, whether Make or n8n is better, how MCP should fit, how future agents should remember tool choices, or how to route recurring work safely.
---

# Automation Tool Router

Use this first when the work is about automation architecture or tool choice.
Return a concrete owner, not a vague stack.

## Routing Order

1. Use the native connector when one exists for the target system.
2. Use Codex automation for recurring reasoning, review, repo, inbox, or briefing work.
3. Use MCP when an agent needs a typed, bounded tool or resource.
4. Use Make.com for fast SaaS glue, forms, CRM updates, and simple approval chains.
5. Use n8n for branchy technical workflows, private data flows, reusable templates, and self-hostable automation.
6. Use a Starlight queue for cross-repo, multi-agent, eval-heavy, or handoff-heavy work.

## Safety Gates

- Require human approval before send, post, spend, delete, publish, invite, production deploy, or account-permission changes.
- Dry-run first for migrations, workflow activation, bulk edits, and storage cleanup.
- Fail closed on auth, schema, transport, webhook, or confidence errors.
- Never print or commit secrets, live webhook URLs, customer data, inbox content, or private memory.
- Public exports must use mock payloads and pass a sensitive-marker scan.

## Decision Output

Return:

- tool owner
- why this tool wins
- fallback tool
- trigger/input
- output contract
- approval gate
- validation step
- where durable state belongs

## Reference Routing

- For Make.com scenario design, use `make-com-operations`.
- For n8n workflow design or exported workflow review, use `n8n-operations`.
- For MCP scopes, tool schemas, and server boundaries, use `mcp-governance`.
- For recurring scheduled work in Codex, use `codex-automation-operator`.
- For multi-agent queues and handoffs, use `starlight-queen-queue`.

## Verification

For public artifacts, run `scripts/scan_public_safety.py` from the source repo
when available. For installable bundles, run `scripts/validate_skill_bundle.py`.

