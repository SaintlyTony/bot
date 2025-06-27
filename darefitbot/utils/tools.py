import json
import random
from pathlib import Path

import aiofiles

from ..database import models

BASE_DIR = Path(__file__).resolve().parent.parent
WORKOUTS_FILE = BASE_DIR / "data" / "workouts.json"
ADS_FILE = BASE_DIR / "data" / "ads.json"


async def _load_json(path: Path):
    async with aiofiles.open(path, "r", encoding="utf-8") as f:
        data = await f.read()
    return json.loads(data)


async def select_workout(goal: str, level: str) -> dict:
    workouts = await _load_json(WORKOUTS_FILE)
    filtered = [w for w in workouts if (not goal or w.get("goal") == goal) and (not level or w.get("level") == level)]
    if not filtered:
        filtered = workouts
    return random.choice(filtered) if filtered else None


async def select_ad() -> dict:
    ads = await _load_json(ADS_FILE)
    return random.choice(ads) if ads else None


async def should_send_ad(user_id: int) -> bool:
    return await models.increment_ad_counter_async(user_id)
