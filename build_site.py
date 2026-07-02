"""Write the weekly-mission scoreboard page (docs/scoreboard.html).

Run from the repo root after solving a mission:

    python build_site.py

Standard library only, on purpose. Reading this file is itself a mission:
pathlib, f-strings, html.escape, json embedding. Bonus twist: the page it
writes can RUN the Python it displays, right in the browser, via Pyodide.
"""

import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
PLAYGROUNDS = ROOT / "playgrounds"
DOCS = ROOT / "docs"
DATA_SUFFIXES = {".log", ".txt", ".csv", ".json"}

PAGE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>speak-then-spell — weekly missions</title>
<link href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Serif:ital,wght@1,300&display=swap" rel="stylesheet">
<style>
  :root{color-scheme:dark;--bg:#000000;--card:#000604;--surface:#000403;--text:#FAF9F7;--muted:#D4F0E8;
        --green:#0C5530;--gold:#C2A455;--maroon:#5E1A21;--border:rgba(212,240,232,.24);
        --neu:8px 8px 18px rgba(0,0,0,.75),-6px -6px 14px rgba(18,112,62,.04)}
  *{box-sizing:border-box;margin:0}
  body{background:var(--bg);color:var(--text);font-family:'Courier Prime','Courier New',monospace;line-height:1.6}
  header{padding:3rem 1.5rem 1.5rem;text-align:center}
  header h1{font-size:2rem}
  header p{color:var(--muted);font-family:'IBM Plex Serif',serif;font-style:italic}
  header a{color:var(--green)}
  main{width:100%;margin:0 auto;padding:0 1.75rem 4rem}
  .week{background:var(--card);border:1px solid var(--border);border-radius:24px;
        padding:1.5rem;margin-bottom:2rem;box-shadow:var(--neu)}
  .week h2{color:var(--green);margin-bottom:1rem}
  .solutions{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1rem}
  .player{min-width:0}
  .player h3{font-family:'Courier Prime',monospace;font-size:.8rem;text-transform:uppercase;
             letter-spacing:.1em;color:var(--gold);margin-bottom:.5rem}
  pre{background:#000302;color:#CFE8DB;padding:1rem;border-radius:12px;overflow-x:auto;
      font-family:'Courier Prime',monospace;font-size:.75rem;max-height:480px;border:1px solid var(--border)}
  .empty{color:var(--muted);font-style:italic;padding:1.2rem;border:2px dashed var(--maroon);
         border-radius:12px;text-align:center;font-family:'IBM Plex Serif',serif}
  .btnrow{display:flex;gap:8px;flex-wrap:wrap;margin:.5rem 0 1rem}
  .run{background:var(--green);color:var(--text);border:0;border-radius:10px;padding:8px 16px;
       font-weight:700;font-size:.8rem;cursor:pointer;font-family:'Courier Prime',monospace;
       transition:transform .12s ease}
  .run:hover{transform:translateY(-2px)}
  .out{background:#000;color:#9fe8c3;min-height:2rem}
  .out[hidden]{display:none}
  footer{text-align:center;color:var(--muted);padding:2rem;font-size:.85rem;
         font-family:'Courier Prime',monospace}
</style>
</head>
<body>
<header>
  <h1>weekly missions ⚔️</h1>
  <p>both solve alone. both push. then we talk. eyes on your own work until then, the rule is older than the repo.</p>
  <p>every solution below runs LIVE in this page. press ▶ and watch the rival's code breathe.</p>
  <p><a href="index.html">← back to the playground</a></p>
</header>
<main>
"""

PAGE_BOTTOM = """</main>
<footer>two coders · one repo · loser owes the winner</footer>
<script>
const CODES = __CODES__;
const FILES = __FILES__;
let pyodideReady = null;
function wakeTheSnake() {
  if (!pyodideReady) {
    pyodideReady = new Promise(resolve => {
      const s = document.createElement("script");
      s.src = "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js";
      s.onload = async () => resolve(await loadPyodide());
      document.head.appendChild(s);
    });
  }
  return pyodideReady;
}
async function runSol(btn) {
  const out = btn.closest(".player").querySelector('[data-out="' + btn.dataset.code + '"]');
  out.hidden = false;
  out.textContent = "waking the snake… (first time takes a few seconds, worth it)";
  try {
    const py = await wakeTheSnake();
    const files = FILES[btn.dataset.week] || {};
    for (const [name, content] of Object.entries(files)) py.FS.writeFile(name, content);
    py.globals.set("__code__", CODES[btn.dataset.code]);
    py.globals.set("__arg__", btn.dataset.arg || "");
    const result = await py.runPythonAsync(`
import sys, io, traceback
sys.argv = ["solution.py"] + ([__arg__] if __arg__ else [])
_buf = io.StringIO()
_so, _se = sys.stdout, sys.stderr
sys.stdout = sys.stderr = _buf
try:
    exec(compile(__code__, "solution.py", "exec"), {"__name__": "__main__"})
except SystemExit:
    pass
except BaseException:
    traceback.print_exc()
sys.stdout, sys.stderr = _so, _se
_buf.getvalue()
`);
    out.textContent = result || "(finished, quietly. very zen.)";
  } catch (e) {
    out.textContent = "this one wants a real terminal (probably input() or a library). run it locally.\\n" + e;
  }
}
</script>
</body>
</html>
"""


def render_player(player_dir, week_key, data_files, codes):
    parts = []
    for f in sorted(player_dir.rglob("*.py")):
        code_id = f"c{len(codes)}"
        codes[code_id] = f.read_text()
        buttons = "".join(
            f'<button class="run" data-code="{code_id}" data-week="{week_key}" '
            f'data-arg="{html.escape(name)}" onclick="runSol(this)">▶ run with {html.escape(name)}</button>'
            for name in sorted(data_files)
        ) or f'<button class="run" data-code="{code_id}" data-week="{week_key}" onclick="runSol(this)">▶ run it</button>'
        parts.append(
            f"<p><em>{html.escape(f.name)}</em></p>"
            f"<pre><code>{html.escape(codes[code_id])}</code></pre>"
            f'<div class="btnrow">{buttons}</div>'
            f'<pre class="out" data-out="{code_id}" hidden></pre>'
        )
    body = "".join(parts) or '<div class="empty">still cooking, apparently. the silence says plenty. 👀</div>'
    return f'<div class="player"><h3>{html.escape(player_dir.name)}</h3>{body}</div>'


def render_week(week_dir, files_map, codes):
    title = week_dir.name.replace("-", " ").title()
    week_key = week_dir.name
    data_files = {
        p.name: p.read_text()
        for p in week_dir.iterdir()
        if p.suffix in DATA_SUFFIXES and p.is_file()
    }
    files_map[week_key] = data_files
    players = sorted(p for p in (week_dir / "solutions").iterdir() if p.is_dir())
    cols = "".join(render_player(p, week_key, data_files, codes) for p in players)
    return f'<section class="week"><h2>{html.escape(title)}</h2><div class="solutions">{cols}</div></section>'


def main():
    weeks = sorted(d for d in PLAYGROUNDS.iterdir() if (d / "solutions").is_dir())
    files_map, codes = {}, {}
    middle = "".join(render_week(w, files_map, codes) for w in weeks)
    page = (
        PAGE_TOP
        + middle
        + PAGE_BOTTOM.replace("__CODES__", json.dumps(codes)).replace("__FILES__", json.dumps(files_map))
    )
    DOCS.mkdir(exist_ok=True)
    (DOCS / "scoreboard.html").write_text(page)
    print(f"scoreboard rebuilt → docs/scoreboard.html ({len(weeks)} week(s), {len(codes)} runnable file(s))")


if __name__ == "__main__":
    main()
