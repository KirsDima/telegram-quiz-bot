import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types
from aiogram import F
from cr_table import create_table
from conf import API_TOKEN, quiz_data, DB_NAME, user_scores
from get_question_module import get_question
from get_quiz_index_module import get_quiz_index
from new_quiz_module import new_quiz
from save_result_module import save_result
from update_quiz_index_module import update_quiz_index
from quiz_handlers import quiz_router

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

dp.include_router(quiz_router)

# Запуск процесса поллинга новых апдейтов
async def main():

    # Запускаем создание таблицы базы данных
    await create_table()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

