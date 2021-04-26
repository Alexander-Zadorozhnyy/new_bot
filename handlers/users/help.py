from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/menu - Меню",
            "/items - тест кнопок",
            "/test - тест вопросы",
            "/dice - кубик",)
    
    await message.answer("\n".join(text))
