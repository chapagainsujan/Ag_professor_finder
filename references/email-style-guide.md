# Email style guide: write like a person

Professors read dozens of student emails a week and spot template and chatbot text fast. The patterns below come from Wikipedia's guide "Signs of AI writing" (WikiProject AI Cleanup) and reviews of AI-generated text. They are signs, not proof, and a person can use any one of them. But several in one short email is the giveaway, and a cold email has no room for them.

## What a good email is

A real student wrote it, once, to one person, for a reason. It has:
- one specific fact from the professor's work that the student actually read
- one specific fact from the student's own record
- one clear ask
- plain words

## Length and shape

- 110 to 170 words in the body. Under 120 is fine when the point is simple.
- 3 short paragraphs. No headings, no bullet points, no bold, no emojis.
- Subject line under 12 words, informative: `Prospective MSc student, wheat scab resistance (Univ. of X)`.
- Plain-text style. Straight quotes. No fancy formatting.

## Patterns to avoid

Each item gives the tell, then what to do instead.

### Staging and contrast
- "It's not just X, it's Y", "not only X but also Y", "This isn't about X, it's about Y". Say the point directly.
- One-line closers that restate: "That's what drew me to your lab." Cut it, or add a fact.
- Dramatic fragments: "No shortcuts. No excuses." Merge into a sentence.
- Run-ups: "I hope this email finds you well", "I am writing to express my keen interest", "Let me introduce myself", "Honestly?". Start with who you are in one clause.
- Arguing with no one: "I know you are busy, but...", "I'm not asking for a favor, I'm..." Say what you need.

### Inflated language
- Words that appear far more often in AI text than in student writing: delve, pivotal, crucial, robust, tapestry, landscape (abstract), intricate, meticulous, testament, underscore, highlight (verb), showcase, foster, vibrant, enduring, groundbreaking, cutting-edge, innovative, passionate, deeply, profoundly, leverage, align with, resonate, keen, esteemed, renowned, prestigious.
- Significance claims: "your pioneering work", "a pivotal contribution", "plays a key role", "a game-changer", "the future of agriculture". Say what the paper did.
- Sales language: "a unique opportunity", "a perfect fit", "a dream".
- "-ing" riders at the end: "..., highlighting the importance of...", "..., ensuring that...", "..., reflecting my commitment to...". Cut them.
- "Serves as", "stands as", "boasts", "features", "offers" where "is" or "has" works.

### Flattery
- "I have long admired your groundbreaking research." Flattery that fits any professor is noise. Replace with a specific detail: the method, the result, the sample size, a figure that raised a question.

### Rhythm
- Triads: "curiosity, dedication, and a drive to learn". Choose the one that is true and give evidence.
- Several sentences in a row with the same opening ("I am... I have... I want...").
- Dashes and double hyphens used as the universal connector. Use commas, periods or parentheses. A student email rarely needs a dash at all. Do not use em dashes.
- Stacked qualifiers: "could potentially perhaps". Pick one hedge or none.
- Over-hyphenation after the noun: "the work is well-documented". "Well documented".

### Formatting
- Bold labels, bullets, headers, tables, emojis, or arrows in an email. Remove.
- Title Case In Subject Lines Or Headings. Use sentence case.
- Curly quotes if the rest of the text is plain.

### Chatbot residue
- "I hope this helps", "Certainly!", "Great question", "Please let me know if you would like me to expand", "As an AI". Remove.
- Placeholders left in: `[Professor Name]`, `[University]`. Fix before output.
- Offers to do more at the end ("Would you like me to adjust the tone?") belong in chat to the student, not in the email.

### Fake specifics and guesses
- Do not attribute a view to the professor that you did not read.
- Do not say you "read all" their papers. Name the one or two you read.
- Do not say "I noticed you are looking for students" unless the page says so.
- No claims about the professor's funding as a hook. A neutral mention such as "I saw the lab's GRDC-funded project on X" is fine only if confirmed.

### Wrong reader
- Do not explain the professor's own research back to them. One clause on what you took from it, then your question.

## Voice

- Use the student's real voice. If they gave any sample (an SOP, earlier emails, messages), match its sentence length and word choice. If English is the student's second language, simple correct sentences beat fancy ones. Do not add idioms they would not use.
- Contractions are fine ("I'm", "I'd"). Slightly formal register is right for first contact: "Dear Professor Lastname," and "Best regards," with name.
- Mixed lengths. A five-word sentence next to a twenty-word one.
- One honest limitation is a good thing: "I have not worked with sequencing data yet, but I have used R for field trial analysis."

## Process

1. Draft from the dossier and the student profile only.
2. Run `python3 scripts/slop_check.py email.txt`. Fix every flagged item or confirm it is justified.
3. If a humanizer skill is available, apply it and re-check. It must not add facts.
4. Read once more from the professor's side. Delete the weakest sentence if the email still works without it.
5. Check each fact against the profile or dossier.

## Do not rely on detectors

AI detectors are unreliable. The goal is not to fool a tool. The goal is an email that is specific, true, short and in the student's voice.
