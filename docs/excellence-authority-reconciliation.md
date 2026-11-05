# Authority reconciliation — 2026-10-27

This branch is an **adapter**, not a competing portfolio constitution.

Canonical portfolio authority: [agentic-ops](https://github.com/frankxai/agentic-ops), specifically `QUALITY.md`, reviewed Registry decisions, and its `AGENTS.md` agent-rule synchronizer. Review those accepted documents before implementing any policy update. The short chat entrypoint, excellence skill, and evidence-gate script here are consumers/projections and cannot silently replace or weaken accepted product gates.

Design ownership: GenCreator retains its own Design Taste Kernel, creators and media validation; agentic-creator-os retains its Agent OS/compiled generals and harness tooling; Arcanea retains its canon and product-specific constraints. Use existing integrations and domain suites before proposing a second registry, a new runtime, or a global injection hook.

Integration order:
1. Diff candidate quality rules against accepted `agentic-ops/QUALITY.md`; retain strictest applicable existing release gates.
2. Propose reviewed changes in `agentic-ops` for accepted portfolio policy, with authority IDs, source SHA, costs, rollback and scope.
3. Run existing `node scripts/sync-agent-rules.mjs --full --check --json` to prove adoption/no drift; do not claim this happened in this repository.
4. Add role-specific pointers through existing compiler/harness integrations. No auto-agent creation without real runtime and permissions.
5. Compare executable mission receipt checks with existing `agentic-ops` receipt schema before integration: `excellence_gate.py` is a local prototype and must not be made a blocking CI gate until contract compatibility and false-negative evaluation pass.
6. Validate with existing `agentic-ops` quality/release gates, plus product-specific checks, not a single numeric quality score.

The private ChatGPT Starlight Excellence plugin is a user-invoked interface; neither its creation nor this repo grants universal ChatGPT initialization.
