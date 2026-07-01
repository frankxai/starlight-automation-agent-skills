# Canonical Home Map

This map answers where automation doctrine should live across the GitHub estate.

Last reviewed: 2026-07-01.

## Decision

`frankxai/starlight-automation-agent-skills` is the canonical home for:

- automation tool-choice doctrine
- installable Codex automation skills
- Make.com, n8n, MCP, Composio, Codex automation, Hermes/retrieval, and swarm routing guidance
- public-safe validation scripts and mock examples
- decision records for durable automation patterns

## Why This Repo Owns It

It is the only repo whose purpose is both:

1. public-safe automation doctrine, and
2. installable agent skills that future Codex sessions can actually load.

That combination matters. A guide in an awesome list is discoverable but not
operational. A note in SIS memory is durable but not public/installable. A policy
inside local agent config is powerful but private and machine-specific. This repo
is the bridge: public enough to share, structured enough for agents, and concrete
enough to install.

## Repo Roles

| Repo | Role | What belongs there |
| --- | --- | --- |
| `starlight-automation-agent-skills` | Canonical owner | Tool router skills, automation guide, ADR templates, validation scripts, mock configs |
| `awesome-automation-agent-skills` | Discovery index | Curated links, rankings, examples, public references |
| `Starlight-Intelligence-System` | Memory and provenance | Decisions, private/public boundary notes, SIS routing memory |
| `starlight-agent-config` | Local/private agent control plane | Machine policy, installed-skill wiring, secrets-safe local operator config |
| `starlight-agent-skills` | Substrate skill library | Portable Starlight substrate skills that are broader than automation |
| `starlight-swarm` | Runtime and queue substrate | Queen/worker execution, queue mechanics, eval-backed multi-agent runs |
| `hermes` and `hermes-cockpit` | Retrieval/search operating layer | Search, source gathering, context recovery, cockpit operations |
| `workflow-tier-plugin` | Ready workflow pack | Packaged workflow tiers that consume this doctrine |
| Domain repos | Local use only | Domain-specific automation that should not become global doctrine |

## Placement Rules

- Put global automation doctrine here.
- Put public discovery and rankings in `awesome-automation-agent-skills`.
- Put private runbooks, secrets, live scenario ids, live webhook URLs, and customer data outside public repos.
- Put local machine policy in `starlight-agent-config`.
- Put durable memory of major decisions in SIS memory.
- Put reusable substrate skills in `starlight-agent-skills` only when they are not specifically automation-tool routing.
- Put execution mechanics in `starlight-swarm`, not in this repo.
- Put retrieval/search execution in Hermes repos, then link back here for tool-choice rules.

## Future Agent Start Path

When a future agent is unsure where automation work belongs:

1. Read this file.
2. Read `docs/automation-operating-guide.md`.
3. Use `skills/automation-tool-router/SKILL.md`.
4. Write or update an automation decision record.
5. Keep public-safe doctrine here and private operational state out.

## Promotion Path

Use this lifecycle:

1. A workflow starts in a domain repo or private ops note.
2. If it repeats, write an automation decision record.
3. If it generalizes, add or update a skill in this repo.
4. If it is useful publicly, link it from `awesome-automation-agent-skills`.
5. If it needs runtime execution, wire it through `starlight-swarm`, n8n, Make.com, MCP, Composio, or Codex automations according to the router.

