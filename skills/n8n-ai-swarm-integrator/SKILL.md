---
name: n8n-ai-swarm-integrator
description: Integrate n8n AI Agent nodes, LangChain tools, MCP, and LiteLLM with Starlight swarms/Queen. Design RAG, agentic workflows, bidirectional agent calls via MCP/webhook. For sophisticated agent orchestration using n8n as durable layer.
---

# n8n AI + Swarm Integrator

Use n8n's AI Agent node (LangChain) + tools for agentic logic inside durable workflows. Wire to Queen swarms for multi-agent coordination.

## Key Capabilities
- AI Agent node: Chat models (via LiteLLM in estate), tools (MCP Client Tool, HTTP, code).
- MCP Server Trigger: Expose n8n flows as tools to external agents (Claude, Hermes, Queen).
- RAG / vector / memory patterns inside n8n.
- Bidirectional: n8n calls swarm agents; swarms trigger n8n.

## Starlight Wiring
- Models: LiteLLM for routing/cost control.
- Tracing: Langfuse.
- Handoffs: Webhook to swarm bus or MCP.
- Queue mode for reliable agentic runs at scale.

## Design Rules
- Keep tools narrow and explicit.
- Error handling + human gates for writes/sends.
- Sanitize before sharing.
- Validate with n8n-operations checks + evals.

See n8n-knowledgebase.md (AI/agent section) and n8n-queen-swarm for full patterns and resources (MCP docs, skills.sh, n8n-skills.com).
