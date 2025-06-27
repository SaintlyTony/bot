import asyncio
import random
from pathlib import Path
from typing import Dict

import aiosqlite

DB_PATH = Path(__file__).with_name("db.sqlite3")


async def get_user_async(user_id: int) -> Dict:
    async with aiosqlite.connect(DB_PATH) as conn:
        conn.row_factory = aiosqlite.Row
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                goals TEXT,
                level TEXT,
                ad_counter INTEGER DEFAULT 0,
                ad_threshold INTEGER DEFAULT 3
            )
            """
        )
        await conn.commit()
        cur = await conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        row = await cur.fetchone()
        if row is None:
            threshold = random.randint(3, 5)
            await conn.execute(
                "INSERT INTO users(user_id, goals, level, ad_counter, ad_threshold) VALUES (?, '', '', 0, ?)",
                (user_id, threshold),
            )
            await conn.commit()
            cur = await conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
            row = await cur.fetchone()
        return dict(row)


def get_user(user_id: int) -> Dict:
    return asyncio.run(get_user_async(user_id))


async def increment_ad_counter_async(user_id: int) -> bool:
    user = await get_user_async(user_id)
    counter = user["ad_counter"] + 1
    threshold = user["ad_threshold"]
    show_ad = False
    if counter >= threshold:
        counter = 0
        threshold = random.randint(3, 5)
        show_ad = True
    async with aiosqlite.connect(DB_PATH) as conn:
        await conn.execute(
            "UPDATE users SET ad_counter=?, ad_threshold=? WHERE user_id=?",
            (counter, threshold, user_id),
        )
        await conn.commit()
    return show_ad


def increment_ad_counter(user_id: int) -> bool:
    return asyncio.run(increment_ad_counter_async(user_id))
