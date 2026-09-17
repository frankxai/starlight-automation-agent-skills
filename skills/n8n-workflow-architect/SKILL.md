---
name: n8n-workflow-architect
description: Design, structure, and review complex n8n workflows for scalability, maintainability, reusability. Sub-workflows, error handling, idempotency, branching, AI integration, MCP exposure. Produce validated, documented artifacts.
---

# n8n Workflow Architect

Best practices for production-grade n8n:
- Modular: Sub-workflows for reuse.
- Resilient: Error workflows, retries, dedupe, idempotency keys.
- Observable: Logging, Langfuse tracing.
- Agent-ready: MCP Server Trigger or webhook contracts.
- Scalable: Queue mode considerations, concurrency.

## Review Checklist (Extend n8n-operations)
- Stable node IDs.
- No credentials in exports.
- Clear data contracts and mocks.
- Separation of test/prod.
- AI nodes use estate LiteLLM.
- Integration points documented for swarm/Queen/MCP.

Output: Structured workflow + docs + validation report + swarm wiring plan.

Reference n8n-knowledgebase.md (queue, structuring best practices from community) and official docs.
