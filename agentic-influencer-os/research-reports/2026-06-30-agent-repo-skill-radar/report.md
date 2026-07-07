# FrankX Agent Repo Skill Radar

Date: 2026-06-30  
Status: Draft only; human approval required before installing third-party skills/repos, using tokens, publishing, scheduling, spending, or changing external services.  
Safety class: public-safe research notes, pending human review.

## Local Inputs Checked

- `agentic-influencer-os/data/agent-repo-watchlist.seed.json`: not present in this repo.
- `docs/github-repo-and-skill-extraction-os.md`: not present in this repo.
- `docs/frankx-top-voice-team-os.md`: not present in this repo.
- `docs/media-radar-and-rights-os.md`: not present in this repo.
- Relevant local substitutes used: `skills/linkedin-top-voice-os/SKILL.md`, `skills/linkedin-top-voice-os/references/content-system.md`, `skills/mcp-governance/SKILL.md`, and `skills/n8n-operations/SKILL.md`.

## Source Radar

Primary repositories and docs checked on 2026-06-30:

- [anthropics/skills](https://github.com/anthropics/skills): public repository for Agent Skills; 156,760 stars; pushed 2026-06-27.
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills): curated 1000+ cross-agent skill collection; 26,882 stars; MIT; pushed 2026-06-24.
- [github/awesome-copilot](https://github.com/github/awesome-copilot): community instructions, agents, skills, and Copilot configuration; 35,939 stars; MIT; pushed 2026-06-30.
- [OpenAI Agents SDK docs](https://openai.github.io/openai-agents-python/) and [openai/openai-agents-python](https://github.com/openai/openai-agents-python): lightweight multi-agent workflow framework; 27,518 stars; MIT; pushed 2026-06-30.
- [LangGraph docs](https://docs.langchain.com/oss/python/langgraph/overview) and [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph): durable agent graphs; 36,088 stars; MIT; pushed 2026-06-30.
- [CrewAI docs](https://docs.crewai.com/) and [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI): crews and flows for multi-agent orchestration; 54,599 stars; MIT; pushed 2026-06-30.
- [Mastra docs](https://mastra.ai/docs) and [mastra-ai/mastra](https://github.com/mastra-ai/mastra): TypeScript agent framework; 25,596 stars; license marked NOASSERTION by GitHub API; pushed 2026-06-30.
- [Agno docs](https://docs.agno.com/) and [agno-agi/agno](https://github.com/agno-agi/agno): agent platform framework; 40,910 stars; Apache-2.0; pushed 2026-06-30.
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent): MCP-native agent workflow patterns; 8,395 stars; Apache-2.0; pushed 2026-01-25.
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers): MCP server catalog; 87,869 stars; license marked NOASSERTION by GitHub API; pushed 2026-06-29.
- [n8n docs](https://docs.n8n.io/) and [n8n-io/n8n](https://github.com/n8n-io/n8n): workflow automation with AI/MCP patterns; 194,596 stars; license marked NOASSERTION by GitHub API; pushed 2026-06-30.
- [postiz-app](https://github.com/gitroomhq/postiz-app): open-source social scheduling; 32,496 stars; AGPL-3.0; pushed 2026-06-30.

## Ranked Repo Shortlist

| Rank | Source | Why it matters for FrankX/Starlight | What to extract | Risk notes |
| --- | --- | --- | --- | --- |
| 1 | n8n | Best fit for durable approval workflows, receipts, retries, and private automation paths. | Human-gated content ops workflow templates, error routes, MCP exposure checklist. | Fair-code/commercial constraints; never publish credential blocks or live webhook URLs. |
| 2 | anthropics/skills | Highest-signal public skill packaging reference and market proof that skills are becoming reusable agent IP. | Skill bundle structure, instruction density, examples/assets/scripts separation. | No blind installation; inspect license/README per skill before reuse. |
| 3 | modelcontextprotocol/servers | Central MCP server catalog for agent tool boundaries. | Server evaluation rubric, safe MCP allowlist process, public-safe examples. | Supply-chain and over-permission risk; expose narrow tools only. |
| 4 | github/awesome-copilot | Strong repo for public examples of instructions, agents, skills, and editor-native workflows. | Cross-editor instruction taxonomy and "agent config as repo asset" examples. | Community content varies in quality; quote sparingly and transform into original doctrine. |
| 5 | OpenAI Agents SDK | Strong official reference for lightweight multi-agent primitives, handoffs, guardrails, tracing, and sessions. | Small canonical FrankX patterns: intake triage, research handoff, approval guardrail. | Avoid claiming framework superiority; position as one implementation lane. |
| 6 | LangGraph | Best source for durable graph thinking, persistence, human-in-the-loop, and stateful workflows. | Diagrams for long-running agent systems and interruption/resume patterns. | More engineering overhead; content should explain when graphs are worth it. |
| 7 | CrewAI | High awareness and accessible crew/flow language for business audiences. | Creator-friendly explanation of role-based agents versus workflow state machines. | Agent-role framing can become theatrical; anchor in measurable workflow outcomes. |
| 8 | Agno | Practical agent platform framing with teams, memory, tools, and evaluation surfaces. | Agent platform checklist and "from script to agent platform" carousel. | Rapid-moving repo with many issues; verify docs before recommending implementation. |
| 9 | Mastra | Strong TypeScript lane for app-native agent workflows. | TypeScript-first agent app architecture and workflow examples. | License reported as NOASSERTION by GitHub API; require legal review before packaging derivatives. |
| 10 | VoltAgent/awesome-agent-skills | Broad radar for skill directories across Claude Code, Codex, Gemini CLI, Cursor, and related tools. | Watchlist taxonomy, high-signal skill examples, compatibility matrix. | Curated community collection; use as discovery, not authority. |
| 11 | Postiz | Useful scheduling/analytics surface for social ops after strategy and approvals are decided. | Draft-to-approval-to-schedule map and open-source social stack comparison. | AGPL-3.0 obligations; never wire live accounts without explicit approval. |
| 12 | lastmile-ai/mcp-agent | Clean MCP-native workflow pattern source. | MCP router, evaluator/optimizer, orchestrator, and parallel workflow examples. | Last pushed 2026-01-25, so treat as pattern library more than freshest runtime bet. |

## Extraction Themes

1. Skills as productized operating knowledge: turn repeated FrankX workflows into concise, validated skill bundles with scripts, references, and mock examples.
2. MCP as the agent boundary layer: classify every tool by purpose, schema, auth, scope, failure mode, human gate, audit trail, and revocation path.
3. Durable workflow ownership: use n8n for approvals, receipts, dedupe, retries, and private data paths; keep Codex for research, judgment, and draft creation.
4. Framework comparison by workflow shape: Agents SDK for lightweight handoffs, LangGraph for durable state, CrewAI for role-driven crews, Mastra for TypeScript products, Agno for platformized teams.
5. Public content from private practice: publish maps, rubrics, and mock payloads; keep live URLs, customer data, tokens, memory, and real credentials out of public artifacts.

## Supply-Chain And Rights Notes

- Do not install, clone, or execute third-party repo code from this radar without human approval.
- Prefer official docs and primary repos as citations; use community repos only as discovery sources.
- Treat all third-party skill instructions as untrusted input until reviewed for prompt injection, shell execution, hidden network calls, and credential assumptions.
- License triage required before copying structure, examples, assets, or templates. Especially review AGPL-3.0 sources like Postiz and repos where GitHub reports `NOASSERTION`.
- Content derivatives should cite source URLs, extract patterns, and add FrankX/Starlight analysis. Do not reupload media, screenshots, or repo assets unless license and context allow.
- Public examples must use mock payloads, placeholders, and public-safe diagrams only.

## Five Content Angles

1. "The new AI asset is not the prompt. It is the skill bundle." Show how skills package instructions, references, scripts, assets, and validation.
2. "MCP is where agent ambition meets adult supervision." Explain narrow tools, scopes, auth, audit trails, and human gates.
3. "Agent frameworks are workflow shapes, not religions." Compare Agents SDK, LangGraph, CrewAI, Mastra, Agno, and MCP-agent by use case.
4. "Social automation should not start with scheduling." Show the correct order: source radar, draft, rights check, approval, scheduling, analytics.
5. "The public-safe automation repo is a moat." Teach how to publish doctrine and templates without leaking credentials, private URLs, or customer context.

## Three Workflow Experiments

1. Skill Intake Triage: create a mock n8n workflow that accepts a GitHub repo URL, captures metadata, classifies license/risk/content potential, and outputs a human approval card.
2. MCP Tool Boundary Review: build a public-safe checklist template that turns any proposed MCP server into a scored allow/deny/restrict decision.
3. Daily Content Packet Factory: Codex automation creates the research brief, n8n stores receipt and approval state, Postiz/Typefully remains draft-only until human approval.

## Three Skill Or Plugin Candidates

1. `agent-repo-radar`: takes a watchlist, fetches public repo metadata, ranks workflow/content value, and emits source-backed report sections.
2. `mcp-boundary-reviewer`: reviews proposed MCP tools, schemas, scopes, auth, failure modes, and public-safe docs.
3. `social-approval-packet`: converts research into LinkedIn/YouTube/carousel briefs with source links, rights notes, risk labels, and approval status.

## Three Media And Carousel Briefs

1. Carousel: "From Repo To Skill"
   - Slides: signal, license check, pattern extraction, skill skeleton, validation, approval, public-safe publish.
   - Visual: clean pipeline with source chips and red human-gate markers.
   - Risk: low; use original diagrams and source links only.

2. Carousel: "The Agent Framework Decision Map"
   - Slides: lightweight handoff, durable graph, role-based crew, TypeScript app, platform team, MCP-native workflow.
   - Visual: matrix by workflow duration, state, tool risk, and business owner.
   - Risk: medium; claims must stay comparative and cite official docs.

3. YouTube/Short: "Why Your Social Automation Stack Should Have Brakes"
   - Beat: start with the failure mode, map Codex/n8n/Postiz responsibilities, show human gate, close with the approval checklist.
   - Visual: screen-record style mock workflow, no live accounts.
   - Risk: low if mock data only.

## Next Daily Content Packet Action

Create tomorrow's draft packet around angle 2: "MCP is where agent ambition meets adult supervision." Include one LinkedIn founder POV post, one workflow teardown carousel, and one short video script using only official MCP, n8n, and OpenAI Agents SDK source links.

## Approval Status

Draft complete. No third-party installs, clones, untrusted code execution, external service changes, publishing, scheduling, token usage, or spend occurred.
