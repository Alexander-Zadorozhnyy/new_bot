import emoji
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

question = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Удалить вопрос'),
            KeyboardButton(text='Показать все вопросы')
        ],
[
            KeyboardButton(text='Назад к панели администратора ' + emoji.emojize(':closed_book:')),
        ]
    ],
    resize_keyboard=True
)
