---
name: codex-automation-operator
description: Design and operate recurring Codex automations for scheduled reports, repo health, issue triage, inbox summaries, meeting briefs, deployment monitors, and agentic follow-up work. Use when a user asks to remember recurring work, schedule future Codex tasks, automate routine reviews, or decide whether a task belongs in Codex rather than Make.com, n8n, or MCP.
---

# Codex Automation Operator

Use Codex automations for recurring work that needs judgment, synthesis, repo
context, or connector-backed review.

## Best Fit

- daily or weekly repo health summaries
- issue and PR triage
- Vercel preview checks
- inbox and calendar briefings
- partner follow-up drafts
- stale task reminders
- recurring public-safety scans

## Use Another Tool When

- event latency matters more than reasoning: use Make.com or n8n
- a non-agent system must own execution: use n8n or Make.com
- the task is only a typed external tool call: use MCP
- the task needs multiple parallel repo workers: use a Starlight queue

## Automation Spec

Return:

- name
- cadence
- scope
- sources/connectors
- output shape
- no-findings behavior
- archive behavior
- approval gates
- escalation condition
- owner and review cadence

## Gates

Codex may draft, summarize, inspect, and report. Human approval is required
before sending messages, posting publicly, spending, deleting, inviting,
changing access, or production promotion.

## Output Shape

Return: automation spec, why Codex is the owner, connectors needed, risk gates,
and validation method.

