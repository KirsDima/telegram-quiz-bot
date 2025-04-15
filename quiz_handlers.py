import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types
from aiogram import F
from cr_table import create_table
from conf import API_TOKEN, quiz_data, DB_NAME, user_scores
import get_all_stats_module
from get_question_module import get_question
from get_quiz_index_module import get_quiz_index
from new_quiz_module import new_quiz
from save_result_module import save_result
from update_quiz_index_module import update_quiz_index
from get_all_stats_module import get_all_stats

quiz_router = Router()

@quiz_router.message(F.text=="Начать игру")
@quiz_router.message(Command("quiz"))
async def cmd_quiz(message: types.Message):

    await message.answer(f"Давайте начнем квиз!")
    await new_quiz(message)

@quiz_router.callback_query(F.data.startswith("right:"))
@quiz_router.callback_query(F.data.startswith("wrong:"))
async def handle_answer(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )

    user_id = callback.from_user.id
    current_question_index = await get_quiz_index(user_id)
    question = quiz_data[current_question_index]
    correct_option_text = question['options'][question['correct_option']]

    selected_index = int(callback.data.split(":")[1])
    selected_option_text = question['options'][selected_index]

    if user_id not in user_scores:
        user_scores[user_id] = 0

    if callback.data.startswith("right:"):
        user_scores[user_id] += 1
        await callback.message.answer(f"✅ Верно! Вы выбрали: *{selected_option_text}*", parse_mode="Markdown")
    else:
        await callback.message.answer(
            f"❌ Неправильно. Вы выбрали: *{selected_option_text}*\n"
            f"Правильный ответ: *{correct_option_text}*",
            parse_mode="Markdown"
        )

    current_question_index += 1
    await update_quiz_index(user_id, current_question_index)

    if current_question_index < len(quiz_data):
        await get_question(callback.message, user_id)
    else:
        score = user_scores.get(user_id, 0)
        await callback.message.answer(f"🎉 Квиз завершен! Ваш результат: *{score} из {len(quiz_data)}*", parse_mode="Markdown")
        await save_result(user_id, callback.from_user.username or "Unknown", score)
        user_scores.pop(user_id)  # Очистим результат


# Хэндлер на команду /start
@quiz_router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))

# Хэндлер на команду /stats
@quiz_router.message(Command("stats"))
async def show_all_stats(message: types.Message):
    stats = await get_all_stats()
    if stats:
        text = "📊 Статистика всех игроков:\n\n" + "\n".join(stats[:20])
        await message.answer(text)
    else:
        await message.answer("Пока никто не проходил квиз 😢")





