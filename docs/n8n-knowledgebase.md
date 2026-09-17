# Starlight n8n Knowledgebase (Curated Best-of 2026)

**Source of truth for n8n in the Starlight estate.** Public-safe index of up-to-date docs, templates, integrations, AI/agent patterns, queue/self-host best practices, MCP wiring, and Starlight-specific usage. All live credentials, private URLs, and customer data stay out of this repo.

Last curated: 2026-08-10 (from official docs, top GitHub, community, skills.sh alignment, estate runbooks).

## Official & Core Documentation (Always Verify Latest)
- Main docs: https://docs.n8n.io/
- Queue mode / scaling (Primary + Workers + Redis + Postgres): https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode
  - Best practices: Use queue mode for production. Primary handles UI/API/webhooks. Workers execute jobs. Redis for queue. Postgres for state (13+ recommended). Shared encryption key across instances. Set `N8N_CONCURRENCY_PRODUCTION_LIMIT` and worker concurrency >=5 (higher for scale; avoid low values to prevent DB pool exhaustion).
  - Estate mapping (n8n w/workers project): Primary (public UI/webhooks/API), Worker(s), Redis, Postgres. Use for durable technical/branchy automations.
- Webhook node (auth, variables, security): https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook
- MCP Server Trigger node (expose n8n workflows/tools to agents like Claude Desktop via MCP): https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger
  - Pattern: n8n as MCP server. Use with Basic/Header/JWT auth on webhooks. Proxy via mcp-remote or similar.
- AI / LangChain nodes: Search docs for "AI Agent", "LangChain", tools, vector stores, RAG patterns.
- API: Use X-N8N-API-KEY header for /api/v1/workflows, executions, etc. (generate in UI; store via Infisical in estate).
- Self-host / Docker / Railway patterns: See estate technology-runbooks and operating-cadence (Primary/Worker split, health checks).

## Best GitHub Repos & Template Collections (Curated, High-Signal)
- enescingoz/awesome-n8n-templates: 280+ free ready-to-import workflows (Gmail, Telegram, Slack, OpenAI, AI agents, RAG, chatbots, social, DevOps, docs). Largest open collection. Import JSON directly.
- n8n-io/n8n (core) + community examples in repo.
- Other high-volume: Repos claiming 1000–4300+ workflows (AI/ML folders strong for OpenAI/RAG). Search GitHub "n8n-workflow" or "n8n templates AI".
- Starlight preference: Start with official + awesome-n8n-templates. Sanitize, validate (no creds, stable node IDs, error routes, mock payloads), then promote to our examples/ or templates/.

Official community templates library: https://n8n.io/workflows (9000+ community-contributed; AI pipelines, CRM, content, finance, lead enrichment). Many approved via community forum.

## skills.sh & Agent Skills Ecosystem
- https://www.skills.sh/ — The Agent Skills Directory. Reusable capabilities for AI agents. Install with `npx skills add <org/repo>` or specific (e.g., npx skills update).
- Strong alignment with Starlight SKILL.md format. Use for n8n-related agent capabilities (image gen, LLM, search, workflows).
- Related: inference-sh/skills, mattpocock/skills, n8n-skills.com (14 complementary expert Claude Code skills for n8n workflows covering 525+ nodes, 2653+ templates, patterns. Installable for Claude Code/Desktop).
- n8n community discussion: Enable n8n agents to reference Agent Skills (SKILL.md + progressive disclosure).

Install Starlight automation skills (including n8n ones) via the repo's installation process or adapt to skills.sh where compatible.

## AI / Agentic / Swarm Integrations (Most Sophisticated Patterns)
- n8n AI Agent node + tools: LangChain-based chat models, tools, RAG, vector stores. Combine with LiteLLM (estate service) for model routing.
- MCP bidirectional:
  - n8n exposes workflows as MCP Server Trigger → agents (Claude, Hermes, Queen) call them.
  - n8n workflows call external MCP servers via MCP Client Tool nodes.
- Webhooks + auth (Basic/Header/JWT/IP whitelist) for triggering from Queen/swarm bus or receiving from agents.
- Example wiring (sanitized):
  - Queen enqueues job → n8n webhook (or MCP) starts workflow.
  - Workflow uses AI Agent node (LiteLLM) + tools (MCP or HTTP to swarm/Hermes).
  - Execution results via webhook back to swarm bus or stored in Langfuse (estate tracing).
- Estate integrations: LiteLLM for models, Langfuse (web + worker) for observability, Infisical for creds/secrets, Redis/Postgres for durability, Postiz for publishing where appropriate.
- Advanced: Sub-workflows for reusability, error workflows, idempotency keys, dedupe, retry policies. Break large flows into branches/subflows. Use Execute Command or specialized workers for heavy CPU/GPU if needed.
- n8n as durable automation spine for swarms: Queue mode for reliability at scale. Use for content pipelines, lead intake (sensitive), memory/provenance sync, approval routing (human-gated), API orchestration.

## Top Template Categories & Starlight Usage
See workflow-catalog.md and examples/n8n/ for estate-aligned patterns.
- Content pipelines (draft → review → n8n approval routing → Postiz).
- AI agent chat / RAG / enrichment.
- Lead intake (sensitive data → n8n).
- Repo change → preview verification.
- Meeting briefs, inbox triage (feed to Codex/Queen).
- MCP-exposed tools and agent handoffs.
- Social authority packets, Google News → Instagram (community examples).

Validation required before any public or production use:
- Run `python scripts/validate_n8n_workflow.py <file.json>`
- `python scripts/scan_public_safety.py`
- Remove credentials, check node IDs/connections, add error routes, mock payloads, document contracts.

## Installation & Local Development (Best Tools)
- n8n CLI: `npm install -g n8n` or `npx n8n` for export/import/validate locally. Useful for testing JSON before Railway.
- Community nodes: Install via n8n UI or package.json in self-host (e.g., AI/MCP extras).
- Railway (estate primary): Link service, set env (N8N_ENCRYPTION_KEY shared, queue mode vars, DB/Redis connections via Infisical). Primary exposes public domain for webhooks/UI. Workers internal.
- Self-host Docker reference: See official queue mode docs + estate runbooks.
- Skills: Follow installation.md. Restart agent after adding n8n-operations or new skills.
- MCP: Use mcp-remote or native for Claude Desktop / agent clients. Auth tokens via env (never hardcode).

## Estate / Starlight Specifics
- Primary automation layer for technical/branchy/private/template-worthy work (per automation-tool-doctrine and operating-guide).
- Pair with: Codex for judgment, Composio for broad SaaS auth (narrow), MCP for typed boundaries, Starlight swarm queues for multi-agent/cross-repo/eval-heavy.
- Human gates: Outbound, deletes, production, spend, account changes.
- Public/private: Doctrine + sanitized templates here. Live workflows, webhooks, creds in private vaults or Railway/Infisical.
- Validation & evals: Tie to starlight-evals. Use in Queen swarms.
- References: estate-map.md, technology-runbooks.md (n8n w/workers), operating-cadence.md.

## Community & Evolution
- Contribute: Sanitized, validated templates + docs to awesome-automation-agent-skills or this repo's examples/.
- Top external sources for inspiration (always sanitize/validate):
  - awesome-n8n-templates
  - n8n.io/workflows + community forum
  - n8n-skills.com
  - skills.sh ecosystem
  - GitHub n8n-workflow topic + AI automation repos
- Starlight goal: Best-of-best validated & tested collection. Run full validation + safety scan before promotion. Wire community via public awesome index + installable skills.

## Quick Start for Agents
1. Read automation-operating-guide.md + this KB.
2. Use automation-tool-router or n8n-operations.
3. For new workflow: Design in n8n (or import template), validate JSON, add to examples/, document in catalog.
4. For agentic: Expose via MCP Server Trigger or webhook; call from Queen/swarm.
5. For Railway: Follow estate runbooks for deploy/health.

Update this file when major new patterns, docs, or estate changes land. Prefer evidence from official sources + tested usage.