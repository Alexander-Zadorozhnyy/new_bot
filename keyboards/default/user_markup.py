import emoji
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Список товаров ' + emoji.emojize(':credit_card:')),
        ],
[
            KeyboardButton(text='Корзина ' + emoji.emojize(':basketball:')),
            KeyboardButton(text='Задать вопрос в тех.поддержку ' + emoji.emojize(':speech_balloon:'))
        ]
    ],
    resize_keyboard=True
)
