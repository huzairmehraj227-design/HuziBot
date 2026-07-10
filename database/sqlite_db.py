import sqlite3
import json

conn = sqlite3.connect("huzibot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    profile TEXT DEFAULT '{}',
    history TEXT DEFAULT ''
)
""")

conn.commit()


def get_profile(user_id):
    cursor.execute(
        "SELECT profile FROM users WHERE user_id=?",
        (user_id,),
    )

    row = cursor.fetchone()

    if row and row[0]:
        return json.loads(row[0])

    return {}


def save_profile(user_id, profile):
    cursor.execute("""
        INSERT INTO users (user_id, profile)
        VALUES (?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET profile=excluded.profile
    """, (user_id, json.dumps(profile)))

    conn.commit()


def get_history(user_id):
    cursor.execute(
        "SELECT history FROM users WHERE user_id=?",
        (user_id,),
    )

    row = cursor.fetchone()

    if row:
        return row[0] or ""

    return ""


def save_history(user_id, history):
    cursor.execute("""
        INSERT INTO users (user_id, history)
        VALUES (?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET history=excluded.history
    """, (user_id, history))

    conn.commit()


def clear_history(user_id):
    cursor.execute("""
        UPDATE users
        SET history=''
        WHERE user_id=?
    """, (user_id,))

    conn.commit()


def clear_profile(user_id):
    cursor.execute("""
        UPDATE users
        SET profile='{}'
        WHERE user_id=?
    """, (user_id,))

    conn.commit()