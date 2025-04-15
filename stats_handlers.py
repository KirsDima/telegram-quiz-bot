# handlers/stats_handlers.py

from aiogram import types, Router
from get_all_stats_module import get_all_stats

stats_router = Router()

@stats_router.message(commands=["stats"])
async def show_all_stats(message: types.Message):
    stats = await get_all_stats()
    if stats:
        text = "📊 Статистика всех игроков:\n\n" + "\n".join(stats[:20])
        await message.answer(text)
    else:
        await message.answer("Пока никто не проходил квиз 😢")
