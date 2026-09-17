---
name: n8n-testing-eval
description: Test, validate, evaluate n8n workflows and executions. JSON schema checks, execution simulation, safety scans, integration evals with swarm/Queen, tie to starlight-evals. Use before promotion or production.
---

# n8n Testing & Eval

## Validation Layers
- Structural: scripts/validate_n8n_workflow.py (nodes, connections, no credentials).
- Safety: scripts/scan_public_safety.py.
- Execution: Manual trigger with mocks, check outputs, error paths, idempotency.
- AI/Agent: Test MCP exposure, tool calls, model responses (LiteLLM + Langfuse traces).
- Swarm integration: End-to-end with Queen handoffs, webhook contracts.

## Advanced
- Sub-workflow testing.
- Concurrency/load considerations (queue mode).
- Eval harness: Compare outputs, cost, latency (link to starlight-evals).
- Regression: Export baseline JSON, diff on changes.

Run full suite before any community or production use. Update knowledgebase with lessons.
