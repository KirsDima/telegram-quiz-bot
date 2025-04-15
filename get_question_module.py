from gen_opt_kb_module import generate_options_keyboard
from get_quiz_index_module import get_quiz_index
from conf import quiz_data

async def get_question(message, user_id):

    # Получение текущего вопроса из словаря состояний пользователя
    current_question_index = await get_quiz_index(user_id)
    question = quiz_data[current_question_index]
    kb = generate_options_keyboard(question['options'], question['correct_option'])
    await message.answer(f"{question['question']}", reply_markup=kb)