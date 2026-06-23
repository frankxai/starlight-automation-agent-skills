# Automation Operating Guide

This guide is for Frank, Codex, Hermes, Starlight agents, and any future coding
agent that needs to decide how automation should work across the estate.

Last reviewed: 2026-06-23.

## The Mental Model

Automation is not one tool. It is a stack of ownership layers:

| Layer | Use it for | Main cost | Long-term risk |
| --- | --- | --- | --- |
| Native connectors | GitHub, Vercel, Gmail, Calendar, Slack, Drive, Notion, Linear | Usually included with the host/app | Connector coverage gaps |
| Codex automations | Recurring reasoning, repo health, triage, briefs, reports | Plan/usage budget plus local machine availability | Too many noisy reports |
| Hermes and retrieval agents | Search, recall, synthesis, source gathering, context recovery | Model/tool calls and index freshness | Stale or over-broad context |
| MCP | Typed agent access to tools and data | Build/maintenance/security overhead | Over-exposed tools |
| Make.com | Fast SaaS glue and nontechnical workflow ownership | Credit usage per module/action and plan tier | Credit sprawl and opaque complexity |
| n8n | Technical branching, private workflows, templates, self-hosting | Cloud executions or self-hosting ops | Workflow maintenance burden |
| Starlight swarm queues | Multi-agent, cross-repo, eval-heavy execution | Coordination/model cost | Unbounded jobs if not scoped |
| Custom scripts/GitHub Actions | Deterministic checks and repo automation | Engineering time and CI minutes | Brittle scripts without owners |

Use the narrowest layer that can safely own the outcome.

## Tool Choice Rules

### Use native connectors first

Choose a connector when the workflow is mainly inside a supported app:

- GitHub issue/PR/repo work
- Vercel project/deployment/log inspection
- Gmail reading and draft review
- Calendar availability and meeting prep
- Slack summarization and drafting
- Drive/Docs/Sheets/Slides reads and structured edits

Connectors preserve identity, permissions, and auditability better than generic
HTTP automation.

### Use Codex automations for recurring judgment

Use Codex automations when the task needs interpretation, synthesis, or repo
context on a schedule:

- "Every morning, tell me what needs attention."
- "Weekly, inspect these repos for stale PRs or failing checks."
- "After a deploy, verify the preview and report issues."
- "Summarize inbox/calendar context but do not send."

Codex automations are not an integration bus. They are a recurring agent.
According to OpenAI's docs, project-scoped automations need the local Codex app,
the machine, and the project path to be available when the job runs.

### Use Hermes and retrieval agents for context

Use Hermes-style agents when the bottleneck is finding, comparing, or recovering
context:

- cross-repo search
- source gathering
- memory recall
- "what did we decide before?"
- research packets for another builder agent

Hermes should usually feed another lane rather than mutate production systems.
When Hermes output will drive a public claim, run a source/evidence gate.

### Use MCP for agent-facing tool boundaries

Use MCP when an agent needs a typed tool or resource:

- run a selected Make scenario
- call a selected n8n workflow
- query a local memory or registry
- expose a small operational API to multiple agent clients

MCP is not the automation engine. It is the boundary that lets agents call tools
safely. Keep tools small, explicit, logged, and revocable.

### Use Make.com for fast SaaS glue

Use Make when speed and visual SaaS integration matter:

- form submission to CRM/sheet
- lead intake notifications
- purchase follow-up
- simple enrichment and routing
- low-risk approval workflows

Watch credit usage. Make's official pricing now uses credits; the free plan
includes 1,000 credits/month, and paid tiers begin with Core/Pro/Teams plans.
Use Make when low-code speed is worth the credit model.

### Use n8n for technical durable workflows

Use n8n when the workflow is branchy, private, template-worthy, or needs JSON
review:

- API pipelines
- private data routing
- reusable workflow templates
- self-hosted automations
- workflows with many steps per execution
- MCP Server Trigger or MCP Client Tool patterns

n8n Cloud pricing is execution-based, regardless of workflow complexity, and
the official pricing page says all plans include unlimited users, workflows, and
integrations. Self-hosting can reduce platform fees but adds operations work.

### Use Starlight swarm queues for bounded multi-agent work

Use a Starlight queue when one automation should not own the whole job:

- cross-repo audit plus fixes
- release verification requiring several perspectives
- plugin or skill publication reviews
- long-running build/eval waves
- work that needs worker lanes and a synthesis owner

Every queued job needs objective, input context, allowed tools, write scope, stop
condition, evidence, and handoff format.

## Cost Model

Think in total cost, not subscription price.

| Tool | Direct cost to watch | Hidden cost to watch | Cost control |
| --- | --- | --- | --- |
| Connector | Usually platform/account plan | Missing actions, rate limits | Prefer read/draft before writes |
| Codex automation | Codex/ChatGPT plan and usage | Noisy recurring tasks, local app dependency | Archive no-finding tasks; review cadence monthly |
| Hermes/retrieval | Model/tool calls | Stale indexes, broad search | Require source receipts and scoped queries |
| MCP | Hosting/build time | Security surface, schema drift | Small tools, read/run scopes, explicit owners |
| Make.com | Credits and plan | Credit sprawl, hard-to-review visual logic | Credit budget, scenario owner, monthly run review |
| n8n Cloud | Monthly executions | Workflow sprawl | Error workflows, templates, execution budget |
| n8n self-hosted | Hosting and maintenance | Backups, upgrades, security | Only self-host when privacy/scale justifies it |
| Swarm queue | Model/agent time | Coordination overhead | Bounded jobs and stop conditions |
| Custom scripts | Engineer time and CI | Maintenance drift | Tests and ownership |

## Decision Protocol

Before creating automation, write down:

1. Outcome: what changes in the world?
2. Trigger: human, schedule, event, webhook, or agent request?
3. Risk class: read-only, draft, internal write, external write, destructive, financial.
4. Tool owner: connector, Codex, Hermes, MCP, Make, n8n, swarm, script.
5. Data contract: input fields, output fields, and where state lives.
6. Approval gate: what requires Frank or another human?
7. Observability: where logs, costs, failures, and run receipts show up.
8. Evaluation: how we know it works.
9. Maintenance owner: who revisits it and when.
10. Exit rule: when to delete, migrate, or promote it.

Use `templates/automation-decision-record.md` for repeatable decisions.

## Observability

Every automation needs one visible receipt surface:

- run history for Make/n8n
- Codex inbox item for Codex automations
- GitHub Actions log for CI/script jobs
- MCP server logs for tool calls
- Starlight queue report for multi-agent jobs
- SIS memory/provenance entry for durable decisions

Minimum log fields:

- run id
- timestamp
- trigger
- tool owner
- input summary
- output summary
- cost signal when available
- pass/fail
- human action needed
- next retry or stop state

## Evaluation

Do not trust an automation because it ran once. Trust it because it has evidence.

| Eval type | Use for | Pass signal |
| --- | --- | --- |
| Smoke test | New workflow | It runs on a mock payload |
| Regression test | Scripts, MCP configs, workflow JSON | Known fixture still passes |
| Rubric eval | Agent summaries, briefs, research | Output meets stated criteria |
| Red-team check | Public release, destructive tools | Abuse path is blocked or gated |
| Cost eval | Make/n8n/Codex recurring jobs | Cost stays under budget |
| Handoff eval | Swarm jobs | Fresh agent can continue from report |

Public releases need at least one representative output and one boundary review.

## Maintenance Cadence

### Weekly

- Review failed or noisy automations.
- Check Make/n8n run usage and obvious cost spikes.
- Archive no-finding Codex automations that are just noise.
- Confirm no public-facing automation bypasses human approval.

### Monthly

- Audit active workflows by owner and purpose.
- Rotate or review high-risk credentials.
- Delete stale scenarios and workflows.
- Check MCP exposed tools and scopes.
- Review top recurring costs.
- Promote useful patterns into skills or templates.

### Quarterly

- Re-evaluate Make vs n8n vs Codex ownership.
- Decide what should become an MCP tool.
- Decide what should become a public template.
- Run a publication-safety scan on public automation repos.
- Kill automations that no longer save time or reduce risk.

## Evolution Ladder

Start small and promote only after evidence:

1. Manual checklist.
2. Codex-assisted repeated task.
3. Codex automation or connector workflow.
4. Make/n8n automation.
5. MCP tool boundary.
6. Starlight queue for multi-agent scaling.
7. Public template or productized workflow.

Do not jump to a swarm when a checklist or connector solves the job.

## Agent Working Agreement

When an agent touches automation, it should:

1. Invoke the automation router.
2. Identify the owner tool.
3. State the approval gate.
4. Avoid live credentials and live webhook URLs.
5. Produce or update an automation decision record.
6. Run the relevant validation or scan.
7. Record durable decisions in memory when appropriate.

## Current Official References

- Make pricing: https://www.make.com/en/pricing
- n8n pricing: https://n8n.io/pricing/
- Codex pricing: https://developers.openai.com/codex/pricing
- Codex automations: https://developers.openai.com/codex/app/automations
- MCP introduction: https://modelcontextprotocol.io/docs/getting-started/intro

