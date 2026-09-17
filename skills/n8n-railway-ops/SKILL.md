---
name: n8n-railway-ops
description: Operate n8n on Railway (n8n w/workers project). Primary/Worker/Redis/Postgres health, queue mode config, env via Infisical, deploys, domains, scaling. Use for estate spine maintenance and sophisticated self-hosted patterns.
---

# n8n Railway Ops

Estate setup: Project "n8n w/workers".
- Primary: UI, API, webhooks (public domain for triggers).
- Worker: Job execution.
- Redis: Queue.
- Postgres: Persistence.

## Key Practices (from runbooks)
- Shared encryption key for queue mode.
- Concurrency recommendations (5+ per worker).
- Health: Monitor Primary + workers, DB connections, queue backlog.
- Deploy: Service updates, variables (redacted), compatible images.
- Domains: Public on Primary only.
- Integrations: Connect to estate LiteLLM, Langfuse, Infisical.

Commands (run with proper Railway context):
- Project/service listing and status.
- Variable management (keys only in docs).
- Deploy and logs.

See estate technology-runbooks.md and n8n-knowledgebase.md for details. Human gate production changes.
