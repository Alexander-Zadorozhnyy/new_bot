import emoji
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_mark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emoji.emojize(':black_circle:') + ' Начать ' + emoji.emojize(':red_circle:')),
        ]
    ],
    resize_keyboard=True
)
