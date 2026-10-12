# Contributing

Fixes and additions are welcome, especially new funding sources and corrections to country notes.

## Before you open a pull request

1. Keep `SKILL.md` under 500 lines. Put detail in `references/` and link to it from `SKILL.md`, one level deep.
2. Keep the frontmatter to the fields that Claude.ai and the Skills API accept: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Other keys cause an upload error outside Claude Code.
3. Keep `name` lowercase letters, numbers and hyphens, at most 64 characters, and without the words "claude" or "anthropic". Keep `description` under 1,024 characters, in the third person, and say both what the skill does and when to use it.
4. Use forward slashes in paths.
5. Any new funding source needs a name, what it funds, who it funds (institution or individual), and one search tip. Confirm the link is live.
6. Any claim about admissions or scholarships needs an official source in the pull request description.
7. Run `python3 scripts/slop_check.py` on any sample email you add to the templates.
8. Add or update an entry in `evals/evals.json` if you change behavior.
9. Update `CHANGELOG.md` and bump `metadata.version` in `SKILL.md`.

## What not to add

- Scrapers that bypass site blocks or log-ins.
- Lists of professors' personal details. The skill uses public professional information only.
- Guessed email formats.

## Reporting a problem

Open an issue with the prompt you used, what you expected, what you got, and the model and surface you ran it on (Claude.ai, Claude Code or API).
