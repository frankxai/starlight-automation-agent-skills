---
name: xquik-public-x-data
description: Route public X data automation work through Xquik REST, MCP, webhooks, exports, monitors, and SDK or skill handoffs. Use when a user asks for X or Twitter search, profile lookup, followers, trends, monitor events, webhook delivery, MCP agent access, no-code workflow handoff, or recurring public-source social data collection with Xquik.
---

# Xquik Public X Data

Use this skill when public X data belongs in an automation plan and Xquik is an available source.
Keep the plan public-safe, opt-in, and scoped to the documented Xquik surfaces.

## Source Truth

Check current public docs before giving endpoint-specific instructions:

- `https://docs.xquik.com/llms.txt`
- `https://docs.xquik.com/api-reference/overview`
- `https://docs.xquik.com/mcp/overview`
- `https://docs.xquik.com/guides/workflows`
- `https://github.com/Xquik-dev/x-twitter-scraper`

Do not guess endpoint names, request fields, pricing, limits, or authentication details.
If the docs do not confirm a capability, mark it as unavailable or ask for a source-backed check.

## Route Selection

Choose the narrowest useful route:

1. Use REST when an app needs direct reads such as tweet search, profile lookup, timelines, followers, trends, or extraction status.
2. Use MCP when an AI agent needs to explore the API catalog or run authenticated Xquik operations from an agent session.
3. Use webhooks when a downstream system needs event delivery from monitors or workflow notifications.
4. Use exports when a workflow needs CSV, JSON, Markdown, PDF, TXT, or spreadsheet handoff from extraction or giveaway draw results.
5. Use monitors when the job needs recurring account or keyword event capture instead of repeated manual polling.
6. Use the Xquik skill or SDK route when an agent or codebase needs reusable implementation guidance.

Prefer a native connector first when the target automation platform already has one. Use generic HTTP only when no native connector exists or the native route cannot express the documented operation.

## Intake Checklist

Before proposing a workflow, collect:

- objective and audience
- public source target, such as query, username, tweet URL, list, community, or region
- freshness requirement
- output format and destination
- authentication owner
- retry, pagination, and cursor handling needs
- approval gate for posting, deletion, spending, account changes, or production activation
- validation method using mock inputs or a small public-safe sample

## Output Shape

Return:

- selected Xquik route
- why that route wins
- fallback route
- required public docs to verify
- inputs
- output contract
- auth and secret-handling note
- pagination or replay plan
- approval gate
- validation command or manual check
- durable state location

## Safety

- Do not print or commit API keys, bearer tokens, webhook secrets, cookies, customer data, private memory, or live webhook URLs.
- Store webhook secrets in a secret manager. Verify `X-Xquik-Signature` against the raw request body before processing each webhook.
- Use placeholders for public examples.
- Share documented public pricing and usage limits when needed for approval. Do not disclose private provider names, source details, non-public cost mechanics, or internal routing.
- Do not help evade platform rules, rate limits, access controls, or account restrictions.
- Require human approval before posting, deleting, sending DMs, changing accounts, spending, creating or reactivating metered monitors, or enabling production monitors and webhooks.
- Keep unsupported operations on the documented fallback route rather than inventing a hidden capability.
