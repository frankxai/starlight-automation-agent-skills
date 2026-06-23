# Workflow Catalog

These are the first workflows agents should recognize and route well.

## 1. Repo Change To Preview

GitHub or local git creates the change, Vercel produces a preview, Codex verifies
the URL, and production promotion waits for approval.

## 2. Inbox To Follow-Up

Gmail connector reads context, Codex drafts, Calendar checks availability, and
the human approves any send or calendar write.

## 3. Meeting Brief

Calendar plus relevant docs produce a short brief on a schedule. Codex automation
is the default owner because the task needs summarization and judgment.

## 4. Lead Intake

Form submission goes to Make.com for low-risk routing. Use n8n when the payload
is sensitive, branchy, or should become a reusable template.

## 5. Content Pipeline

Codex and local swarm agents draft, review, and queue content. Publishing remains
human gated.

## 6. Public Template Release

Private workflow pattern is sanitized, scanned, converted into mock payloads,
validated, and published to a public template repo.

## 7. Memory And Provenance Sync

MCP or n8n writes structured events into a private memory/provenance layer.
Public exports use curated summaries only.

## 8. Payment Or Spend Validation

Payments tooling verifies caps and records audit entries. No agent moves money.

