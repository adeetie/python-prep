# speak-then-spell 🗣️→🔤

> Toddlers learn to speak years before anyone shows them the alphabet.
> Same rules here: **play with real, living code first. Grammar arrives later, uninvited.**

Two coders. One repo. A points war, weekly battles, dares with deadlines, real rupees
on the line, and a ladder that ends at God of Python. Ye repo nahi hai, dawai hai.

**The playground lives here → `docs/index.html`** (on GitHub Pages once enabled, see below).
Missions, standings, dares, the meme wall, the vault. Everything.

## How the week works

1. **Pick missions** in the playground, or throw a dare, or cook your own in The Kitchen.
2. **Solve alone.** Weekly mission code goes in `playgrounds/week-XX-name/solutions/<you>/`.
   Eyes on your own work until both have pushed. The rule is older than the repo.
3. **Push it:**
   ```bash
   git add .
   git commit -m "week 01: cooked"
   git push
   python build_site.py     # refreshes docs/scoreboard.html, both solutions side by side
   ```
4. **Compare, roast, learn.** One question over chai: "why did you do it that way?"
   That conversation is the actual course material.
5. **Close the week** in the playground. Winner writes one dare. Loser completes it.
   The constitution is one sentence long and it is merciless.

## The stakes

- Points become rupees: 1 point = ₹2.5, cashed in via the Vault, gift or straight UPI,
  ₹3,000 cap per cash-in. The house always pays.
- Broken streaks and lost dares become forfeits, written by the winner, savored by the winner.

## First-time setup (Ayush, this means you)

```bash
git clone https://github.com/adeetie/python-prep.git
cd python-prep
```
Open the playground link, claim your name, pick your face. Your solutions folder
is already waiting for you. It has been waiting a while, actually.

## Turning on the live site (one time, on GitHub)

Repo **Settings → Pages → Deploy from a branch → `main`, folder `/docs` → Save.**
The playground then lives at `https://adeetie.github.io/python-prep/` and updates on every push.

## House documents

| File | What it is |
|------|-----------|
| `docs/index.html` | The playground itself. One file, readable on purpose. |
| `build_site.py` | Writes the weekly scoreboard. Pure standard library, secretly a mission. |
| `VOICE.md` | The language laws. Read before writing a single user-facing word. |
| `GAME-MASTER.md` | How to design new missions and keep the fire lit. |
| `playgrounds/` | Weekly missions and both players' solutions. |

## The reference shelf

The CodeWithHarry Handbook and Cheatsheet PDFs stay outside this repo. They're the
dictionary. Dictionaries are for after you've tried talking.
[CodeWithHarry on YouTube](https://www.youtube.com/@CodeWithHarry/videos)
