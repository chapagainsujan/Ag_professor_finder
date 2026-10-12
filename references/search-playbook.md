# Search playbook

How to find, check and read professors online. Use WebSearch and WebFetch first. If the shell has internet access (it often does not), `scripts/openalex_lookup.py` automates the paper lookup.

## 0. Check today's date

"Last 3 years" counts back from today. Example: on 2026-10-12, use publications from 2023 onward (2023-10 and later is strict). When in doubt include the full calendar year three years back and say so.

## 1. Find candidates

### By institution
Start with institutions known for agriculture, then widen.

- **US:** land-grant universities (e.g. Cornell, UC Davis, Purdue, Iowa State, Michigan State, Kansas State, Texas A&M, Wisconsin-Madison, Minnesota, Nebraska-Lincoln, Illinois, Ohio State, Penn State, NC State, Florida, Georgia, Washington State, Oregon State, Colorado State, Oklahoma State, Arkansas, Clemson, Virginia Tech, North Dakota State, South Dakota State). Also 1890 institutions such as NC A&T, Tuskegee, Prairie View A&M, Alcorn State.
- **Canada:** University of Saskatchewan (College of Agriculture and Bioresources), University of Manitoba, University of Alberta (ALES), University of Guelph (OAC), UBC (Land and Food Systems), McGill (Macdonald Campus), Laval, Dalhousie (Faculty of Agriculture), University of Lethbridge, Brandon.
- **Australia:** University of Adelaide (Waite), University of Queensland (QAAFI), UWA, University of Sydney, University of Melbourne, University of New England, Charles Sturt, Curtin, La Trobe, University of Tasmania, University of Southern Queensland, Western Sydney (Hawkesbury), Queensland University of Technology, CSIRO adjuncts.

This list is a start, not the full set. Add others that show up in funder databases.

### By topic
Search combinations:
```
"<keyword>" professor site:edu faculty
"<keyword>" lab <country> university
"<keyword>" "graduate students" OR "prospective students" site:edu
"<keyword>" site:edu.au OR site:ca
<keyword> research group "join us"
```

### From funded-project lists
Open the funder databases in `funding-databases.md` and search the student's keywords. People who show up with current grants are strong candidates.

### From recent papers
Search the topic on Google Scholar, OpenAlex, or Web of Science if available. Sort by recent. The last author is usually the lab head. The corresponding author often has the public email. Check affiliations and country.

## 2. Confirm the person is a fit

Open the official faculty or lab page and check:
- Current title and department. Exclude emeritus, adjunct only, retired, and "former".
- Research statement matches the student's profile.
- Last update of the page. Old pages are common. Cross-check with a paper from the last 12 months.
- Admissions notes for prospective students. Copy them exactly.
- Current lab members with dates. Many recent students means an active lab.

## 3. Last-3-year publications

Preferred order:
1. OpenAlex: author profile, then works filtered by year.
2. Google Scholar profile (only when affiliation is clear).
3. ORCID page.
4. Faculty page publication list.
5. Publisher pages and DOI landing pages to verify.

OpenAlex API examples (base `https://api.openalex.org`). A free API key is recommended; without one the daily budget is small. If the key is not available, keep requests few.
```
/authors?search=<full name>&select=id,display_name,last_known_institutions,works_count,orcid
/works?filter=authorships.author.id:<ID>,publication_year:2023-2026&select=title,publication_year,doi,primary_location,abstract_inverted_index&per-page=50
```
- Identify the right person by institution and ORCID. Common names collide. Never filter by name alone.
- Reconstruct the abstract from `abstract_inverted_index` or open the page.
- Always open the DOI before listing a paper.

For each paper kept, record: title, year, journal, DOI, one-line takeaway read from the abstract.

## 4. Research direction

After reading 5 to 10 titles and 2 to 3 abstracts, answer:
- What is the lab's main question?
- What changed in the last 3 years (new crop, new tool, new pathogen, new collaboration, new funder)?
- Which paper is most connected to the student, and why?

Write two sentences. These feed the email.

## 5. Current projects

- Lab page "Research" or "Projects"
- Department news
- Funder project pages (see `funding-databases.md`)
- Conference abstracts or talks from the last 12 months
- Preprints on bioRxiv or Research Square if relevant

## 6. Contact details

- Use the official page only. Copy the address exactly.
- If only a form or a department admin address is given, say so.
- Do not infer formats from other staff.
- If the page says "do not email about admissions, apply through the portal", report that exactly and tell the student. Respect it.

## 7. Time and effort budget

- Candidate discovery: about 15 to 25 searches.
- Screening: one page per candidate.
- Deep research: 6 to 12 sources per professor.
- Stop when you have 8 to 12 well-checked professors. Do not keep going to pad the list.

## 8. When searches fail

- No hits for a niche topic: broaden one level (disease to disease group, crop to crop family) and say you did.
- Site blocks fetch: use search snippets, university news, or ask the student to open the page. Do not scrape around a block.
- Conflicting dates: prefer the most recent official source and note the conflict.
