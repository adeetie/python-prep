# Game-master notes 🎲

How to keep new missions dropping every week. (Either player can be game-master;
the game-master still solves the mission too.)

## Where to mine real code

Small, readable, famous — in rough order of friendliness:

| Repo | Good hunting grounds | Toys hiding inside |
|------|---------------------|--------------------|
| `psf/requests` | `models.py`, `utils.py` | exceptions, properties, streams |
| `tqdm/tqdm` | `std.py` | generators, `__iter__`, formatting |
| `Textualize/rich` | `rich/color.py`, `rich/markup.py` | regex, dataclasses, enums |
| `pallets/flask` | `helpers.py` | decorators, context managers |
| `pallets/click` | `types.py` | classes, inheritance, error messages |
| `python/cpython` | `Lib/statistics.py`, `Lib/textwrap.py` | pure stdlib, superbly commented |

**Recipe:** find a function under ~60 lines that does one visible thing → simplify it
into a `starter.py` that runs standalone with sample data → hide 2–3 "toys of the week"
in it → write the mission as *break it / refactor it / upgrade it*.

## Mission template

Every `MISSION.md` has the same skeleton:

1. **Where this code comes from** — always name the real repo. Reading pro code should feel normal.
2. **Run it first** — an exact command that works before any thinking is required.
3. **Break it** — an input that crashes it (this is where error handling gets learned).
4. **Refactor it** — the toy of the week, with a count ("at least 3 walruses") not a how-to.
5. **Upgrade it** — open-ended, so the two solutions diverge and there's something to compare.
6. **Victory conditions** — checkable by running commands, never by opinion.

## Toy roadmap (one per week, roughly in order)

`:=` walrus → exceptions & `raise` → f-string tricks → comprehensions →
generators & `yield` → `pathlib` → decorators → context managers (`with`) →
dataclasses → `argparse` → regex → `functools` → async (much later).

## Keeping momentum (the actual point)

- **Drop the mission on a fixed day.** Rhythm beats motivation.
- **Push something ugly early.** An empty `solutions/` column on the site is the nudge —
  nobody wants to be the dashed box that says "not pushed yet… 👀".
- **After both push: one call/chat to compare diffs.** Ask "why did you do it that way?"
  — that conversation is the real lesson, and the real time spent together.
- **Alternate game-masters.** Designing a mission teaches more than solving one.
- **Never explain a concept before the mission.** Toddler rule: they speak first,
  grammar comes later. The PDFs are for *after* they've fought the code.
