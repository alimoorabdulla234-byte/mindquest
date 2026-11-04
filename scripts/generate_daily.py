#!/usr/bin/env python3
"""Select a prepared MindQuest challenge for the current UTC day."""
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
bank = json.loads((ROOT / "question-bank.json").read_text(encoding="utf-8"))
today = datetime.datetime.now(datetime.timezone.utc).date()
challenges = bank["challenges"]
challenge = challenges[today.toordinal() % len(challenges)]
payload = {
    "date": today.isoformat(),
    "name": challenge["name"],
    "category": challenge["category"],
    "reward": challenge["reward"],
    "tip": challenge["tip"],
    "questions": challenge["questions"],
}
(ROOT / "daily-content.json").write_text(
    json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Prepared {payload['name']} for {payload['date']}")
