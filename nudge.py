"""The daily nudge. The repo checks on both of us and says something about it.

Runs on GitHub's own machines every evening (see .github/workflows/nudge.yml),
reads the shared notebook, and pushes a note to each player's phone via ntfy.sh.

Phone setup, once, two minutes:
1. Install the ntfy app (iOS/Android), or open ntfy.sh in a browser.
2. Subscribe to your topic below. Pick weird topic names, they're public radio
   frequencies: whoever knows the name can listen. Weird = private enough.
3. Done. The repo now knows where you live (spiritually).

Standard library only. Reading this file is, of course, also a mission:
json, datetime, urllib, and the ancient art of minding someone's business.
"""

import json
import urllib.request
from datetime import date
from pathlib import Path

TOPICS = {
    "aditi": "speak-then-spell-cat-overlord",
    "ayush": "speak-then-spell-moai-man",
}

QUIET_ROASTS = [
    "Zero points today. The streak is writing its will.",
    "The terminal misses you. It said so. In writing.",
    "Aaj nahi toh kab? The leaderboard already knows your answer.",
    "One mission. Twenty minutes. Or lose the week over chai you'll have to buy.",
    "Your rival's commit graph is greener. Bas keh raha hoon.",
]

AHEAD_PRAISE = [
    "You lead the week. Defend it like it owes you money.",
    "Winning. Insufferable and correct, keep going.",
    "Top of the board. The dare you'll write is already smiling.",
]


def send(topic: str, title: str, message: str) -> None:
    req = urllib.request.Request(
        f"https://ntfy.sh/{topic}",
        data=message.encode(),
        headers={"Title": title, "Tags": "snake,fire"},
    )
    urllib.request.urlopen(req, timeout=10)


def main() -> None:
    state = json.loads(Path("docs/state.json").read_text())
    week = state.get("week", {})
    seed = date.today().toordinal()
    for player, topic in TOPICS.items():
        mine = week.get(player, 0)
        theirs = max(v for k, v in week.items() if k != player) if len(week) > 1 else 0
        if mine > theirs:
            note = AHEAD_PRAISE[seed % len(AHEAD_PRAISE)]
        else:
            note = QUIET_ROASTS[seed % len(QUIET_ROASTS)]
        send(topic, f"speak-then-spell · {mine} pts this week", note)
        print(f"nudged {player} → {topic}")


if __name__ == "__main__":
    main()
