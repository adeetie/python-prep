# Game-master notes 🎲

Either player can run a week. The game-master still plays, still sweats, still owes whatever the winner decides when losing. Current going rate: one ride.

## Where to mine real code for missions

Small, readable, famous. Roughly friendliest first:

| Repo | Good hunting grounds | Hidden treasure |
|------|---------------------|-----------------|
| `python/cpython` | `Lib/statistics.py`, `Lib/textwrap.py` | pure stdlib, superbly commented |
| `psf/requests` | `models.py`, `utils.py` | exceptions, properties, streams |
| `tqdm/tqdm` | `std.py` | generators, `__iter__`, formatting |
| `Textualize/rich` | `rich/color.py`, `rich/markup.py` | regex, dataclasses, enums |
| `pallets/flask` | `helpers.py` | decorators, context managers |
| `pallets/click` | `types.py` | classes, inheritance, kind error messages |

**Recipe:** find a function under ~60 lines that does one visible thing → simplify it into
a `starter.py` that runs standalone with sample data → hide two or three ideas inside →
write the mission as *run it, break it, make it yours*.

## Mission anatomy (every `MISSION.md`)

1. **Where the code comes from.** Always name the real repo. Reading pro code should feel routine.
2. **Run it first.** An exact command that works before any thinking is required.
3. **Break it.** An input that crashes it. The tracebacks are the teacher.
4. **Make it yours.** Open-ended upgrade, so the two solutions diverge. The difference is the lesson.
5. **Victory conditions.** Checkable by running commands. Opinions stay in the group chat.
6. **A trail, never an answer.** Point at the doc, the chapter, the video. The hunt is the training.

## Voice

Every word follows `VOICE.md`. Witty, warm, Indian meme fluent, best-friend-level teasing,
strictly platonic, and instructions stay crystal even when the joke lands.

## Keeping the fire lit

- **Missions drop on a fixed day.** Rhythm beats motivation, every single week.
- **Push something ugly early.** The empty scoreboard column does the nagging for you.
- **After both push: one call, one question.** "Why did you do it that way?" Repeat weekly, get rich slowly.
- **Alternate game-masters.** Designing a mission teaches more than solving one.
- **Grammar after speech, always.** The PDFs open after the fight with the code, never before.
