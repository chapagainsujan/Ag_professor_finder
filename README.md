# ag-professor-finder

A Claude skill that helps agriculture students find graduate supervisors in the **United States, Canada and Australia**, research them properly, and write a cold email that reads like a person wrote it.

You give it your CV or a few lines about your background. It gives you a ranked shortlist, a research file on each professor (current projects, papers from the last 3 years, research direction, public funding), and draft emails.

Built with Claude by Anthropic. This is a community project and is not an official Anthropic product.

Version 1.0.0 | MIT license | Last reviewed October 2026

## Contents

1. [What it does](#what-it-does)
2. [Who it is for](#who-it-is-for)
3. [Install](#install)
4. [How to use it](#how-to-use-it)
5. [How it works, step by step](#how-it-works-step-by-step)
6. [What you get](#what-you-get)
7. [Funding sources it searches](#funding-sources-it-searches)
8. [How the emails are kept human](#how-the-emails-are-kept-human)
9. [Accuracy rules and limits](#accuracy-rules-and-limits)
10. [Privacy and safety](#privacy-and-safety)
11. [Repository layout](#repository-layout)
12. [Testing the skill](#testing-the-skill)
13. [Troubleshooting](#troubleshooting)
14. [Claude Skills in depth](#claude-skills-in-depth)
15. [Contributing, license, credits](#contributing-license-credits)

## What it does

| Job | What happens |
|---|---|
| Match | Reads your CV, pulls out your real skills and interests, expands them into search keywords, and finds faculty who work on them. |
| Investigate | For each shortlisted professor it opens the lab page, recent papers, and funder databases. It records current projects, papers from the last 3 years, how the research direction changed, who funds it and until when, and whether the lab takes students. |
| Write | Drafts a short cold email using one paper the professor actually wrote and one fact from your own record. Then it checks the draft against a list of AI-writing patterns. |
| Track | Fills an outreach tracker with email status, follow-up dates and replies. |

## Who it is for

- Students from any country who want an MSc, PhD, research assistant post or visiting placement in agriculture, in the US, Canada or Australia.
- Fields: plant breeding and genetics, plant pathology, entomology, agronomy, soil science, horticulture, irrigation, precision agriculture, animal science, food science, agricultural economics, extension, agroecology.
- Not meant for mass mailing. It is built for a small number of researched emails.

## Install

Claude skills are not shared between products. Install it in each place where you want to use it.

### Claude.ai (web and desktop)

Anthropic's documentation says custom skill uploads need a Pro, Max, Team or Enterprise plan with code execution turned on. Check the current rules on the [Claude Help Center](https://support.claude.com).

1. Download this repository as a ZIP (Code, then Download ZIP).
2. Unzip it and rename the folder to `ag-professor-finder`. Zip that folder again so the zip contains one folder with `SKILL.md` at its top.
3. In Claude, open Settings, then Features (or Capabilities), find Skills, and upload the zip.
4. Turn the skill on. Start a new chat and ask for what you need.

### Claude Code (terminal, desktop or IDE)

Personal install, available in every project:

```bash
git clone https://github.com/YOUR-USERNAME/ag-professor-finder.git ~/.claude/skills/ag-professor-finder
```

Project install, shared with a team through the repository:

```bash
git clone https://github.com/YOUR-USERNAME/ag-professor-finder.git .claude/skills/ag-professor-finder
```

Start a new session. Run `/ag-professor-finder` or just describe the task.

### Claude API

Upload the folder through the `/v1/skills` endpoint and reference its `skill_id` in the `container` parameter together with the code execution tool. The API sandbox has no internet access, so the live research steps will not work there unless you supply your own search tool.

### If you have no paid plan

You can still use the method by hand. Open `SKILL.md`, paste it into a chat with a model that has web search, and attach the files in `references/` and `templates/` when the step asks for them. It works less smoothly than an installed skill.

## How to use it

Attach your CV (PDF or Word) or paste a short description, then ask. Examples:

```
Here is my CV. Find 10 professors in Canada and Australia working on wheat
disease resistance. I want a funded MSc starting fall 2027. Include their
last 3 years of papers and funding.
```

```
Research Dr. [Name] at [University]. What have they published since 2023,
which grants do they hold, and are they taking students? Then draft an email.
```

```
I am a BSc soil science graduate from Nepal. I like carbon and microbes.
I have used R and run field trials for two seasons. Which US land-grant
universities should I look at?
```

```
Rewrite this email so it does not sound like AI. [paste]
```

Useful details to include: degree level, start term, countries, whether you need funding, your thesis topic, tools you have used, and any publications.

After the shortlist arrives, tell it which professors to write to. It drafts one email per professor.

## How it works, step by step

The agent follows the workflow in `SKILL.md`.

| Step | What the agent does | Output |
|---|---|---|
| 0 | Says what it will do. | One sentence |
| 1 | Builds your profile from the CV. Asks at most four questions, and only for what is missing. | `student_profile.md` |
| 2 | Expands keywords, searches institutions, topics, funded-project lists and recent papers. Collects 15 to 25 candidates and drops anyone retired, emeritus or moved. | Candidate list |
| 3 | Scores each candidate on topic fit (35%), skills fit (20%), recent output (15%), active funding (20%) and signs of taking students (10%). Keeps the top 8 to 12. | Shortlist |
| 4 | Researches each shortlisted professor in depth. Uses parallel subagents when the host offers them. | `dossiers/<name>.md` |
| 5 | Verifies: opens each DOI, confirms each grant in the funder's database, confirms emails on official pages, and dates every admissions claim. | Checked dossiers |
| 6 | Reports the top matches in chat with country notes, and asks who you want to write to. | `shortlist.md`, `tracker.csv` |
| 7 | Drafts each email, runs the checker, applies a humanizer pass if one is installed, then rereads as the professor would. | `emails/<name>_draft.md` |
| 8 | Updates the tracker as you send emails and get replies. | `tracker.csv` |

Why the order matters: screening before deep research keeps the expensive work for people who are worth it, and verification before reporting stops a wrong paper or email from reaching you.

## What you get

```
output/
  student_profile.md          your profile and keywords
  shortlist.md                ranked table: name, university, country, score, funding, email found
  dossiers/
    <lastname>_<university>.md   one per professor, every claim with a source link
  emails/
    <lastname>_draft.md          subject, body, attachments, 10 to 14 day follow-up
  tracker.csv                 status, dates, replies
```

A dossier contains: identity and contact, why the person fits you, research direction over the last 3 years, current projects, papers from the last 3 years with DOIs, funding with role and dates, lab members and admissions notes, a suggested email angle, and a list of anything that could not be confirmed.

## Funding sources it searches

The full list with search tips is in [`references/funding-databases.md`](references/funding-databases.md).

| Country | Main sources |
|---|---|
| United States | USDA NIFA data gateway and CRIS, AFRI, SCRI, OREI, Crop Protection and Pest Management, SARE, Specialty Crop Block Grants, U.S. Wheat and Barley Scab Initiative, International Wheat Yield Partnership, NSF Award Search, USAspending, state commodity boards |
| Canada | NSERC awards data, AAFC AgriScience clusters and project databases, Canadian National Wheat Cluster, Canadian Wheat Research Coalition, WGRF, Saskatchewan ADF, Alberta RDAR, Manitoba, Ontario Agri-Food Research Initiative, Vineland, AgPal, Mitacs |
| Australia | ARC Data Portal and Grants Dataset, Research Link Australia, GRDC, Hort Innovation, AgriFutures, MLA, Dairy Australia, Cotton RDC, Wine Australia, FRDC, ACIAR, state agencies |

Most of these programs fund the professor's university, not students abroad. The skill uses them as evidence that a lab has money for an assistantship. It does not tell you to apply to them.

## How the emails are kept human

The rules come from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, plus the structure of cold emails that get replies. Full rules: [`references/email-style-guide.md`](references/email-style-guide.md).

What the skill avoids:

- stock openers such as "I hope this email finds you well"
- "not just X but Y" contrasts and one-line dramatic closers
- inflated words such as pivotal, robust, delve, tapestry, groundbreaking
- flattery that fits any professor
- forced lists of three, dashes everywhere, bold labels, bullets and emojis
- chatbot leftovers and unfilled placeholders

What it does:

- 110 to 170 words, three short paragraphs, one ask
- one specific detail from a paper the professor wrote
- one specific, true detail from your record, including an honest gap
- your own voice if you give it a sample

Run the checker yourself on any draft:

```bash
python3 scripts/slop_check.py my_email.txt
```

It prints each flagged pattern and exits with code 1 if anything needs a look. A flag is a prompt to rewrite, not proof the text is machine-written. AI detectors are unreliable, and the goal is a specific, honest email, not beating a detector.

## Accuracy rules and limits

- No invented emails, papers, grants or openings. Anything unconfirmed is marked "not found".
- Emails are copied only from official pages. The skill never guesses a format.
- Every dossier claim has a source link.
- "Last 3 years" is counted from today's date.
- A missing grant record is reported as "no public record found", with the databases checked. Industry and start-up money often does not appear.
- A professor's page may be out of date. The skill cross-checks with a recent paper.
- It never states that a professor will fund you.
- Funding rules and admissions pages change. Treat the country notes as orientation and confirm on the official page.
- Some sites block automated fetching. The skill reports this and uses other sources instead of trying to bypass the block.

## Privacy and safety

- Only public, professional information is used: faculty pages, publications, grants.
- It does not collect personal social media, home addresses or family details.
- Your CV stays in your session. Skills are not covered by Zero Data Retention, so Anthropic's standard retention policy applies to skill definitions and execution data.
- The skill contains two small Python scripts. Read them before you install. `slop_check.py` makes no network calls. `openalex_lookup.py` calls only `api.openalex.org`.
- Install skills only from sources you trust. A skill is instructions plus code, and Anthropic advises treating installation like installing software.

## Repository layout

```
ag-professor-finder/
  SKILL.md                    workflow and rules (loaded when the skill triggers)
  README.md                   this file
  LICENSE                     MIT
  CHANGELOG.md                version history
  CONTRIBUTING.md             how to contribute
  references/                 loaded by the agent only when a step needs them
    student-intake.md
    search-playbook.md
    funding-databases.md
    country-notes.md
    email-style-guide.md
  templates/
    student-profile.md
    professor-dossier.md
    cold-email-patterns.md
    tracker.csv
  scripts/
    slop_check.py             offline email checker
    openalex_lookup.py        recent works for an author, via OpenAlex
  evals/
    evals.json                five test prompts
  docs/
    how-claude-skills-work.md
    usage-guide.md
```

## Testing the skill

`evals/evals.json` holds five realistic prompts: a full shortlist from a CV, a deep dive on one professor, a cold email, an AI-text rewrite, and a mass-mailing request that should be declined.

Run each prompt with the skill and once without it, then compare. Check:

- every paper has an opened DOI
- no email appears that is not on an official page
- funding entries name the database and the professor's role
- emails pass `slop_check.py`
- the mass-mailing request is declined politely

Anthropic's skill authoring guidance recommends at least three evaluations, a baseline run without the skill, and testing on more than one model size.

## Troubleshooting

| Problem | What to do |
|---|---|
| The skill does not trigger | Start with a clear request such as "find me professors for ..." or call it by name. In Claude Code run `/ag-professor-finder`. |
| Upload fails on Claude.ai | Make sure the zip contains one folder with `SKILL.md` at its top, and the frontmatter has only `name`, `description`, `license`, `compatibility`, `metadata`. |
| Skills option is missing | Your plan or admin settings may not allow custom skills. Use Claude Code or the manual method. |
| Funder pages will not load | The site blocks automated access. Ask the agent to use the funder's news pages, or open the page and paste the text. |
| No email found | Many departments hide emails. Use the department contact form or the application portal, and follow the page's instructions. |
| Shortlist is short | Few good matches exist in that country or subfield. The skill says so instead of padding the list. |
| `openalex_lookup.py` fails | The environment has no internet access to OpenAlex. The agent falls back to web search. |

## Claude Skills in depth

The short version is below. The long version, with the loading model, frontmatter rules, surfaces and authoring practices, is in [`docs/how-claude-skills-work.md`](docs/how-claude-skills-work.md).

- A skill is a folder with a `SKILL.md` file (name, description, instructions) plus optional scripts, references and templates.
- Claude always sees the name and description (about 100 tokens). It reads the instructions only when a request matches, and opens reference files only when the instructions point to them. Scripts run without their code entering the context.
- Because of this, a skill can hold a large amount of material at almost no cost until it is needed.
- The `description` decides whether the skill triggers, so it must say what the skill does and when to use it.

## Contributing, license, credits

- Contributions: see [`CONTRIBUTING.md`](CONTRIBUTING.md).
- License: [MIT](LICENSE).
- Built with [Claude](https://claude.ai) by Anthropic.
- AI-writing patterns: Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.
- The structure of the two projects that inspired this one, a spreadsheet-based professor finder and ProfRadar, informed the workflow design. This repository contains none of their code.
- Data sources: the funders and databases listed above. Not affiliated with any of them.
