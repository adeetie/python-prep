# Week 01 — Make It Yours 🛠️

**The toy:** a real server-log analyzer, `starter.py`. The kind of script living in the
`scripts/` folder of basically every backend repo on earth. The stream-reading loop inside
is the same pattern the `requests` library and CPython's own docs use. You're reading
grown-up code on day one. That's the whole philosophy.

Zero concepts to study first. The program is the teacher. Chalo.

## Step 1 — Speak to it

Run it before reading it:

```bash
cd playgrounds/week-01-make-it-yours
python starter.py server.log
```

Read it top to bottom once, out loud if that helps, then move on. Understanding every
line is next week's problem. Toddlers talk first, grammar files a complaint later.

## Step 2 — Break it

Copy `starter.py` into your `solutions/<you>/` folder as `solution.py`, then hurt it:

- run it with a file that was never born
- run it on `garbage.log` (included, because real logs are always dirty)
- run it on an empty file

Every traceback is the program confessing where it's fragile. Make it survive all three
with a clear human message instead of a crash. How? Your problem entirely. You'll find
the tools. You always do.

## Step 3 — Make it yours

Upgrade it into something you'd actually run. Anything: errors per hour, slowest endpoint,
a `--top N` flag, colored output, a daily summary written to a file, whatever you wish
logs told you. Your version and the rival's should end up different. That difference is
what gets compared, admired, and roasted on the scoreboard.

## Victory conditions

- `python solution.py server.log` runs clean
- `python solution.py garbage.log` and a missing file both end politely, zero tracebacks
- it does at least one thing the starter can only dream of
- you can explain every line of YOUR file with a straight face

## Side dish (after pushing, strictly)

The pros who write this pattern use an operator called the walrus `:=` to shrink that
chunk-reading loop. Once you've pushed, go see how they use it and form an opinion.
After, always after. Alphabet comes after speech.

## When done

```bash
python build_site.py     # from repo root
git add . && git commit -m "week 01: cooked" && git push
```

Then claim the dare in the playground and collect your points. Eyes on your own work
until both have pushed. The rule is older than the repo.
