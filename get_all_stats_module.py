# modules/get_stats_module.py

import aiosqlite

async def get_all_stats():
    async with aiosqlite.connect('quiz_bot.db') as db:
        cursor = await db.execute('''SELECT username, score, timestamp FROM results ORDER BY timestamp DESC''')
        rows = await cursor.fetchall()

    stats = []
    for row in rows:
        username = row[0] or "Без имени"
        stats.append(f"{username}: {row[1]} баллов ({row[2][:19].replace('T', ' ')})")

    return stats
