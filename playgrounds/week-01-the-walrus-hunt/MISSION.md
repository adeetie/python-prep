# Week 01 — The Walrus Hunt 🦭

**Toy of the week:** the walrus operator `:=` and exception handling.

## Where this code comes from

The chunk-reading loop in `starter.py` is the pattern CPython's own docs and the
`requests` library use to read data streams. Real production Python is full of it.
The rest is a tiny log analyzer, the kind of script every backend repo has buried
in a `scripts/` folder.

## Your mission

`starter.py` works — run it first:

```bash
cd playgrounds/week-01-the-walrus-hunt
python starter.py server.log
```

Now, working **only in your own `solutions/<you>/` folder** (copy `starter.py` there first):

1. **Break it, then bulletproof it.** Feed it a file that doesn't exist. Feed it
   `garbage.log` (included — it has lines that don't parse). Make the script survive
   *every* bad input with a clear message instead of a traceback. You'll need
   `try` / `except` — decide *which* exceptions to catch and which to let crash.
2. **Hunt the walruses.** There are at least **3 places** where the walrus operator
   `:=` makes the code shorter or removes a duplicated line. Find them and refactor.
   (Hint: one is in a `while` loop, one in an `if`, one hides in a comprehension.)
3. **One upgrade of your choice.** Add something the script can't do yet. Ideas:
   count errors per hour, find the slowest request, colored output, `--top N` flag.
   Anything. This is the "make the toy yours" step.

## Victory conditions

- `python solution.py server.log` runs clean
- `python solution.py garbage.log` runs clean (no traceback)
- `python solution.py nope.log` prints a human error, exits politely
- At least 3 honest walruses 🦭🦭🦭
- One upgrade the other player didn't think of

## When done

```bash
python ../../build_site.py   # from repo root: python build_site.py
git add . && git commit -m "week 01: walrus hunt solved" && git push
```

No peeking at the other folder until you've pushed.
