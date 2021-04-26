from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import PEAR_URL, APPLE_URL
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy Apples', callback_data=buy_callback.new(
                item_name='apple', quantity=1
            )),
            InlineKeyboardButton(text='Buy Pears', callback_data=buy_callback.new(
                item_name='pear', quantity=5
            )),
        ],
        [
            InlineKeyboardButton(text='<Go Back>', callback_data='cancel')
        ]
    ]
)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Bought there: ', url=PEAR_URL)
        ]
    ]
)

apple_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Bought there: ', url=APPLE_URL)
        ]
    ]
)