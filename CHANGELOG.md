# Changelog

This project follows [Semantic Versioning](https://semver.org/) and the [Keep a Changelog](https://keepachangelog.com/) format.

## [1.0.0] - 2026-10-12

### Added
- Eight-step workflow in `SKILL.md`: intake, candidate search, screening, deep research, verification, report, email drafting, tracking.
- References for student intake, search method, funding databases (US, Canada, Australia), country admissions notes, and email style.
- Templates for the student profile, professor dossier, cold email patterns and outreach tracker.
- `scripts/slop_check.py`: offline scan of an email for AI-writing patterns.
- `scripts/openalex_lookup.py`: lists an author's recent works from OpenAlex.
- `evals/evals.json`: five test prompts for checking the skill.
- MIT license.

### Known limits
- Live research steps depend on the host's web search and fetch tools. Some funder sites block automatic fetching.
- Funding program names and admissions rules change. The skill tells the agent to confirm them on live pages.
