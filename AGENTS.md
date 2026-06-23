# Agent Instructions

This repo is public-safe automation doctrine and skill packaging.

## Rules

- Keep live workflow exports, private URLs, secrets, customer data, and personal memory out of this repo.
- Prefer concise skills over long manuals. Put detailed platform notes in references.
- Validate every skill with `scripts/validate_skill_bundle.py`.
- Run `scripts/scan_public_safety.py` before publishing.
- Do not include local machine paths in public docs.
- Use mock payloads and placeholders for examples.

## Publishing

Before release, classify changes as:

- `public-safe`: generic doctrine, skills, mock examples, validation scripts.
- `private-only`: live automations, credentials, private memory, business-sensitive data.
- `rewrite`: useful pattern that needs sanitization before publication.

