# ag-professor-finder

A Claude skill for agriculture students looking for a graduate supervisor in the United States, Canada or Australia.

Give it your CV or a few lines about your background. It will:

1. Build a search profile from what you actually have done.
2. Find faculty whose work fits, then research each one: current projects, papers from the last 3 years, research direction, and funding from public databases (NIFA/CRIS, NSF, USWBSI, NSERC, AAFC, WGRF, ARC, GRDC, Hort Innovation and others).
3. Write a cold email in plain, human language, then check it against a list of AI-writing patterns taken from Wikipedia's "Signs of AI writing".

It does not guess emails or invent papers. Anything it cannot confirm is marked "not found".

## Install

**Claude.ai:** Settings, Capabilities, Skills, upload `ag-professor-finder.zip`.

**Claude Code:** copy the folder to `~/.claude/skills/ag-professor-finder/` (all projects) or `.claude/skills/ag-professor-finder/` (one project).

## Use

Examples:

- `Here is my CV. Find 10 professors in Canada and Australia working on wheat disease resistance, with their recent papers and funding.`
- `Research Dr. [Name] at [University] for me: last 3 years of papers, grants, and whether the lab is recruiting. Then draft an email.`
- `Rewrite this email so it doesn't sound like AI.` (attach the draft)

## What you get

```
output/
  student_profile.md
  shortlist.md             ranked table
  dossiers/<name>.md       one per professor, every claim with a source link
  emails/<name>_draft.md   subject, body, follow-up
  tracker.csv              outreach log
```

## Layout

```
SKILL.md                     workflow the agent follows
references/
  student-intake.md          CV to search profile, keyword expansion
  search-playbook.md         where and how to search, OpenAlex usage
  funding-databases.md       US, Canada, Australia funders and how to read hits
  country-notes.md           how supervisor contact and funding differ
  email-style-guide.md       AI-writing tells to avoid and why
templates/                   dossier, profile, email patterns, tracker
scripts/
  slop_check.py              scans an email for AI patterns (offline, stdlib only)
  openalex_lookup.py         lists an author's recent works (needs internet access)
```

## Notes

- Funding programs and admissions rules change. The skill tells the agent to confirm everything on the live page.
- Federal and provincial grants fund the professor's university, not students abroad. They are used here as evidence that a lab can pay an assistantship.
- The checker flags patterns. A flag is a prompt to rewrite, not proof that text is AI-written.
- Use it for a small number of researched emails, not mass mailing.
