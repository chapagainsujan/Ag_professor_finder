#!/usr/bin/env python3
"""Scan a cold email for common AI-writing tells.

Patterns come from Wikipedia's "Signs of AI writing" guide and related reviews.
Usage:  python3 slop_check.py email.txt        (or pipe text on stdin)
Exit code 0 = clean, 1 = something to fix.
A hit is a prompt to rewrite, not proof of AI text.
"""
import re
import sys

WORDS = [
    "delve", "pivotal", "crucial", "robust", "tapestry", "landscape", "intricate",
    "intricacies", "meticulous", "meticulously", "testament", "underscore",
    "underscores", "showcase", "showcasing", "foster", "fostering", "vibrant",
    "enduring", "groundbreaking", "cutting-edge", "cutting edge", "innovative",
    "passionate", "passion", "profoundly", "deeply", "leverage", "leveraging",
    "align with", "aligns with", "resonate", "resonates", "keen", "esteemed",
    "renowned", "prestigious", "pioneering", "game-changer", "game changer",
    "seamless", "holistic", "synergy", "paradigm", "realm", "plethora",
    "multifaceted", "nuanced", "commitment to", "furthermore", "moreover",
    "additionally", "it is worth noting", "it's important to note",
    "it is important to note", "in today's", "ever-evolving", "rapidly evolving",
    "dive into", "deep dive", "unique opportunity", "perfect fit", "dream",
    "serves as", "stands as", "boasts", "highlighting", "emphasizing",
    "ensuring that", "reflecting my", "symbolizing", "contributing to",
]

PHRASES = [
    (r"\bi hope this (email|message) finds you well\b", "stock opener"),
    (r"\bi am writing to (express|inquire|enquire|apply)\b", "stock opener"),
    (r"\bi('m| am) writing to\b", "stock opener (say who you are first)"),
    (r"\bi (have )?long admired\b", "generic flattery"),
    (r"\bmy (strong )?(passion|interest) for\b", "generic enthusiasm"),
    (r"\bdrawn to your\b", "generic flattery"),
    (r"\bi hope this helps\b", "chatbot residue"),
    (r"\bcertainly!|\bof course!|\bgreat question\b", "chatbot residue"),
    (r"\bas an ai\b", "chatbot residue"),
    (r"\blet me know if you('d| would) like\b", "chatbot residue"),
    (r"\bthat'?s the real\b", "staged emphasis"),
    (r"\bat its core\b|\bthe real question\b|\bwhat really matters\b", "sounds deep"),
    (r"\bhonestly\?", "staged candor"),
    (r"\bto be clear\b|\bdon'?t get me wrong\b|\bi'?m not saying\b", "arguing with no one"),
    (r"\bi know (you('re| are)|how) (very )?busy\b", "arguing with no one"),
    (r"\bi (have )?read (all|every one) of your\b", "overclaim"),
    (r"\bplays? a (key|vital|crucial|pivotal|significant) role\b", "inflated significance"),
    (r"\bthe future of (agriculture|farming|food)\b", "inflated significance"),
    (r"\bin the (heart|realm|world) of\b", "inflated"),
    (r"\bvaluable (insights?|opportunity|experience)\b", "filler"),
    (r"\bcontribute to (the )?(advancement|field)\b", "filler"),
]

NOT_X_BUT_Y = [
    r"\bnot (just|only|merely|simply)\b[^.]{0,80}\bbut\b",
    r"\bit'?s not\b[^.]{0,60}[,;]\s*it'?s\b",
    r"\bthis (isn'?t|is not) (about|just)\b",
    r"\bnot\b[^.]{0,40}\brather than\b",
]


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


def main():
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    # strip a Subject line and signature for word counting
    body = re.sub(r"(?im)^subject:.*$", "", text).strip()
    # drop the sign-off and signature so they do not count as body text
    body = re.split(r"(?im)^\s*(best regards|kind regards|warm regards|regards|sincerely|yours sincerely|best wishes|best),?\s*$", body)[0].strip()
    lower = body.lower()
    issues = []

    wc = len(re.findall(r"\b\w+\b", body))
    if wc > 190:
        issues.append(f"Length: {wc} words. Aim for 110 to 170.")
    elif wc < 70:
        issues.append(f"Length: {wc} words. May be too thin to be specific.")

    for w in WORDS:
        if re.search(r"\b" + re.escape(w) + r"\b", lower):
            issues.append(f"Word/phrase: '{w}'")

    for pat, why in PHRASES:
        m = re.search(pat, lower)
        if m:
            issues.append(f"Phrase: '{m.group(0)}' ({why})")

    for pat in NOT_X_BUT_Y:
        m = re.search(pat, lower)
        if m:
            issues.append(f"Not X but Y contrast: '{m.group(0)[:70]}'. State the point directly.")

    if re.search(r"[—–]|(?<!-)--(?!-)", body):
        issues.append("Dash used as connector (em dash, en dash or --). Use comma, period or parentheses.")
    if re.search(r"[“”‘’]", body):
        issues.append("Curly quotes found. Use straight quotes in plain-text email.")
    if re.search(r"\*\*[^*]+\*\*|__[^_]+__", body):
        issues.append("Bold markup found. Remove.")
    if re.search(r"(?m)^\s*([-*•]|\d+\.)\s+", body):
        issues.append("Bullet or numbered list in an email. Write as sentences.")
    if re.search(r"(?m)^#{1,6}\s", body):
        issues.append("Markdown heading in an email.")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿→]", body):
        issues.append("Emoji or arrow found.")
    if re.search(r"\[[^\]]{2,40}\]", body):
        issues.append("Unfilled [placeholder] still in text.")

    # triads: "a, b, and c" with short items
    triads = re.findall(r"\b[\w-]+(?: [\w-]+)?, [\w-]+(?: [\w-]+)?,? and [\w-]+(?: [\w-]+)?\b", body)
    if triads:
        issues.append(f"{len(triads)} list-of-three pattern(s): '{triads[0]}'. Check each item is a distinct fact.")

    # repeated sentence openings
    sents = sentences(body)
    firsts = [s.split()[0].lower() for s in sents if s.split()]
    run = 1
    for i in range(1, len(firsts)):
        run = run + 1 if firsts[i] == firsts[i - 1] else 1
        if run >= 3:
            issues.append(f"Three sentences in a row start with '{firsts[i]}'. Vary the openings.")
            break
    openers_i = sum(1 for f in firsts if f == "i")
    if len(firsts) >= 5 and openers_i / len(firsts) > 0.6:
        issues.append("More than 60% of sentences start with 'I'.")

    # one-line closer: last sentence short and generic
    if sents:
        last_body = [s for s in sents if not re.match(r"(?i)(best|kind|warm|sincerely|regards|thank)", s)]
        if last_body and len(last_body[-1].split()) <= 6 and not last_body[-1].endswith("?"):
            issues.append(f"Short closing sentence: '{last_body[-1]}'. Cut it unless it adds a fact.")

    # sentence-length variety
    lens = [len(s.split()) for s in sents]
    if len(lens) >= 5 and max(lens) - min(lens) < 6:
        issues.append("Sentence lengths are very even. Mix short and long.")

    if issues:
        print(f"{len(issues)} item(s) to check ({wc} words):")
        for i in issues:
            print(" -", i)
        sys.exit(1)
    print(f"No flagged patterns ({wc} words). Still read it aloud and check every fact.")


if __name__ == "__main__":
    main()
