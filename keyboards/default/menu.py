from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Chicken')
        ],
        [
            KeyboardButton(text='Potato'),
            KeyboardButton(text='Sandwich')
        ],
    ],
    resize_keyboard=True
)
