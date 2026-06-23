---
name: starlight-queen-queue
description: Define bounded Starlight swarm queue jobs, queen/worker lanes, handoff packets, safety gates, and validation evidence for multi-agent or cross-repo work. Use when a user asks for a swarm, council, fanout, queen queue, multi-agent execution, long-running agent wave, context-preserving handoff, or Starlight automation operating model.
---

# Starlight Queen Queue

Use a Starlight queue when one linear automation is the wrong shape and work
needs bounded multi-agent execution with a synthesis owner.

## Queue Job Contract

Every job needs:

- objective
- repo or workspace
- source context
- worker lanes
- allowed tools
- write scopes
- stop condition
- validation evidence
- risk gates
- handoff format

## Lane Types

- Doctrine lane: decision rules, docs, memory.
- Build lane: code, repo, plugin, skill changes.
- Safety lane: secrets, private/public split, policy gates.
- Verification lane: tests, validation scripts, release checks.
- Synthesis lane: final decision and user handoff.

## Safety Spine

- One coordinator owns the final risk call.
- Workers do not revert each other's changes.
- Public releases pass a private-memory and secret scan.
- Human approval is required for irreversible external actions.
- Payments and spend actions are verify-only unless the human explicitly approves.

## Handoff Format

Return:

- swarm objective
- worker lanes
- context packet
- execution waves
- validation evidence
- risks
- next handoff

