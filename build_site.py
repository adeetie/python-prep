"""Generate the GitHub Pages site in docs/ from the playgrounds folder.

Run from the repo root after solving a mission:

    python build_site.py

Stdlib only, on purpose — reading this script is itself a mini-lesson
(pathlib, f-strings, html.escape, sorting).
"""

import html
from pathlib import Path

ROOT = Path(__file__).parent
PLAYGROUNDS = ROOT / "playgrounds"
DOCS = ROOT / "docs"

PAGE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>speak-then-spell</title>
<style>
  :root { --ink:#1a1a1a; --paper:#faf7f2; --accent:#0e7c66; --card:#ffffff; }
  * { box-sizing: border-box; }
  body { margin:0; font-family: Georgia, 'Times New Roman', serif;
         background:var(--paper); color:var(--ink); line-height:1.6; }
  header { padding:3rem 1.5rem 2rem; text-align:center; }
  header h1 { font-size:2.2rem; margin:0; }
  header p { color:#666; font-style:italic; }
  main { max-width:1100px; margin:0 auto; padding:0 1.5rem 4rem; }
  .week { background:var(--card); border:1px solid #e5e0d8; border-radius:12px;
          padding:1.5rem; margin-bottom:2rem; }
  .week h2 { margin-top:0; color:var(--accent); }
  .solutions { display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));
               gap:1rem; }
  .player { min-width:0; }
  .player h3 { margin:0.5rem 0; font-family:-apple-system, sans-serif;
               font-size:0.9rem; text-transform:uppercase; letter-spacing:0.08em; }
  pre { background:#0f1a17; color:#d7e6e0; padding:1rem; border-radius:8px;
        overflow-x:auto; font-size:0.8rem; max-height:480px; }
  .empty { color:#999; font-style:italic; padding:1rem;
           border:2px dashed #ddd6ca; border-radius:8px; text-align:center; }
  footer { text-align:center; color:#999; padding:2rem; font-size:0.85rem; }
</style>
</head>
<body>
<header>
  <h1>speak-then-spell 🗣️→🔤</h1>
  <p>learn to speak Python before learning its alphabet</p>
</header>
<main>
"""

PAGE_BOTTOM = """</main>
<footer>two players, one repo, no peeking</footer>
</body>
</html>
"""


def code_block(path):
    return f"<pre><code>{html.escape(path.read_text())}</code></pre>"


def render_player(player_dir):
    files = sorted(p for p in player_dir.rglob("*.py"))
    body = "".join(f"<p><em>{html.escape(f.name)}</em></p>{code_block(f)}" for f in files)
    if not body:
        body = '<div class="empty">not pushed yet… 👀</div>'
    return f'<div class="player"><h3>{html.escape(player_dir.name)}</h3>{body}</div>'


def render_week(week_dir):
    title = week_dir.name.replace("-", " ").title()
    players = sorted(p for p in (week_dir / "solutions").iterdir() if p.is_dir())
    cols = "".join(render_player(p) for p in players)
    return f'<section class="week"><h2>{html.escape(title)}</h2><div class="solutions">{cols}</div></section>'


def main():
    weeks = sorted(d for d in PLAYGROUNDS.iterdir() if (d / "solutions").is_dir())
    DOCS.mkdir(exist_ok=True)
    page = PAGE_TOP + "".join(render_week(w) for w in weeks) + PAGE_BOTTOM
    (DOCS / "index.html").write_text(page)
    print(f"site rebuilt → docs/index.html ({len(weeks)} week(s))")


if __name__ == "__main__":
    main()
