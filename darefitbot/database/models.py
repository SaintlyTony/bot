import random
import sqlite3
from pathlib import Path
from typing import Dict

DB_PATH = Path(__file__).with_name("db.sqlite3")

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

with conn:
    conn.execute(
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


def get_user(user_id: int) -> Dict:
    cur = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    if row is None:
        threshold = random.randint(3, 5)
        conn.execute(
            "INSERT INTO users(user_id, goals, level, ad_counter, ad_threshold) VALUES (?, '', '', 0, ?)",
            (user_id, threshold),
        )
        cur = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        row = cur.fetchone()
    return dict(row)


def increment_ad_counter(user_id: int) -> bool:
    user = get_user(user_id)
    counter = user["ad_counter"] + 1
    threshold = user["ad_threshold"]
    show_ad = False
    if counter >= threshold:
        counter = 0
        threshold = random.randint(3, 5)
        show_ad = True
    with conn:
        conn.execute(
            "UPDATE users SET ad_counter=?, ad_threshold=? WHERE user_id=?",
            (counter, threshold, user_id),
        )
    return show_ad
