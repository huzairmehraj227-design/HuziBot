import sqlite3

conn = sqlite3.connect("huzibot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    memory TEXT
)
""")

conn.commit()


def get_memory(user_id):
    cursor.execute(
        "SELECT memory FROM users WHERE user_id=?",
        (user_id,),
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return ""


def save_memory(user_id, memory):
    cursor.execute("""
    INSERT INTO users(user_id, memory)
    VALUES(?, ?)
    ON CONFLICT(user_id)
    DO UPDATE SET memory=excluded.memory
    """, (user_id, memory))

    conn.commit()