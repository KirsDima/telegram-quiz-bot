import aiosqlite
from datetime import datetime

async def save_result(user_id, username, score):
    async with aiosqlite.connect('quiz_bot.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS results (user_id INTEGER, username TEXT, score INTEGER, timestamp TEXT)''')
        await db.execute('''INSERT INTO results (user_id, username, score, timestamp) VALUES (?, ?, ?, ?)''', (user_id, username, score, datetime.now().isoformat()))
        await db.commit()