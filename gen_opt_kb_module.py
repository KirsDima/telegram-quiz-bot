from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types


def generate_options_keyboard(answer_options, correct_option_index):
    builder = InlineKeyboardBuilder()

    for idx, option in enumerate(answer_options):
        is_correct = idx == correct_option_index
        callback_data = f"right:{idx}" if is_correct else f"wrong:{idx}"

        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data=callback_data
        ))

    builder.adjust(1)
    return builder.as_markup()