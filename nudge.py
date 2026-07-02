"""The daily check-in. The repo takes attendance and your phone hears about it.

Runs on GitHub's machines every evening (see .github/workflows/nudge.yml),
reads the shared notebook, and pushes a note to each player via ntfy.sh.

Phone setup, once, two minutes:
1. Install the ntfy app (iOS/Android), or open ntfy.sh in a browser.
2. Subscribe to your topic below. Pick weird names, topics are public radio
   frequencies: whoever knows the name can listen. Weird = private enough.
3. Done. The repo now knows where you live (spiritually).

Standard library only. Reading this file is, obviously, also a mission.
"""

import json
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TOPICS = {
    "aditi": "speak-then-spell-cat-overlord",
    "ayush": "speak-then-spell-moai-man",
}

# Optional WhatsApp via callmebot.com, free for personal use. One-time setup each:
# save +34 644 71 81 99 as a contact, WhatsApp it "I allow callmebot to send me messages",
# it replies with your apikey. Fill in below. Empty = skipped, ntfy still fires.
WHATSAPP = {
    "aditi": {"phone": "", "apikey": ""},
    "ayush": {"phone": "", "apikey": ""},
}

MISSED_CONTRACT = [
    "You picked today yourself. The contract remembers. So do I.",
    "Promised day, empty ledger. Ye baat kuch hazam nahi hui.",
    "Today was YOUR day. The terminal waited. It deserves better.",
]
QUIET = [
    "Zero points today. The streak is drafting its will.",
    "Aaj nahi toh kab? The leaderboard already knows your answer.",
    "One mission. Twenty minutes. Or lose the week and owe a whole day out.",
]
AHEAD = [
    "You lead the week. Defend it like it owes you money.",
    "Winning. Insufferable and correct. Keep going.",
    "Top of the board. The dare you get to write is already smiling.",
]
KEPT = [
    "Contract honored today. Noted, witnessed, quietly respected.",
    "Showed up on your promised day. The clock has nothing on you. Today.",
]
OVERDUE = "A dare is past its deadline: {title}. The clock saw everything. So did the ledger."


def send_whatsapp(phone: str, apikey: str, message: str) -> None:
    q = urllib.parse.urlencode({"phone": phone, "text": message, "apikey": apikey})
    urllib.request.urlopen(f"https://api.callmebot.com/whatsapp.php?{q}", timeout=15)


def send(topic: str, title: str, message: str) -> None:
    req = urllib.request.Request(
        f"https://ntfy.sh/{topic}",
        data=message.encode(),
        headers={"Title": title, "Tags": "snake,fire"},
    )
    urllib.request.urlopen(req, timeout=10)


def main() -> None:
    state = json.loads(Path("docs/state.json").read_text())
    now = datetime.now(ZoneInfo("Asia/Kolkata"))
    today = now.date().isoformat()
    weekday = (now.weekday() + 1) % 7  # JS-style: Sunday = 0
    seed = now.date().toordinal()
    week = state.get("week", {})

    for player, topic in TOPICS.items():
        p = state["players"].get(player, {})
        mine = week.get(player, 0)
        theirs = max((v for k, v in week.items() if k != player), default=0)
        promised = weekday in (p.get("planDays") or [])
        showed = p.get("lastEarned") == today
        late = [
            c for c in state.get("challenges", [])
            if c.get("to") == player and c.get("status") == "open"
            and c.get("when") and c["when"][:10] < today
        ]

        if late:
            note = OVERDUE.format(title=late[0].get("title", "unnamed"))
        elif promised and not showed:
            note = MISSED_CONTRACT[seed % len(MISSED_CONTRACT)]
        elif promised and showed:
            note = KEPT[seed % len(KEPT)]
        elif mine > theirs:
            note = AHEAD[seed % len(AHEAD)]
        else:
            note = QUIET[seed % len(QUIET)]

        send(topic, f"speak-then-spell · {mine} pts this week", note)
        wa = WHATSAPP.get(player, {})
        if wa.get("phone") and wa.get("apikey"):
            try:
                send_whatsapp(wa["phone"], wa["apikey"], f"speak-then-spell · {mine} pts this week · {note}")
            except Exception as e:
                print(f"whatsapp skipped for {player}: {e}")
        print(f"nudged {player} → {topic}")


if __name__ == "__main__":
    main()
