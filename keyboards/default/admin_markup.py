from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

admin_mark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню пользователя ' + emoji.emojize(':house:')),
        ],
        [
            KeyboardButton(text='Пользователи сайта ' + emoji.emojize(':man:')),
            KeyboardButton(text='Пользователей бота ' + emoji.emojize(':woman:'))
        ],
        [
            KeyboardButton(text='Добавить товар ' + emoji.emojize(':red_circle:')),
            KeyboardButton(text='Тех.Поддержка ' + emoji.emojize(':wrench:'))
        ],
    ],
    resize_keyboard=True
)
