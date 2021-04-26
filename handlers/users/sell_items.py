import logging

from keyboards.inline import buy_callback, apple_keyboard
from keyboards.inline.choice_buttons import choice, pear_keyboard
from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text='You can buy: Apples or Pears\n To exit press -Go Back-', reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'call = {callback_data}')
    await call.message.answer('You choice apple. You bought it', reply_markup=apple_keyboard)


@dp.callback_query_handler(text_contains='pear')
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f'call = {callback_data}')
    await call.message.answer('You choice pear. You bought it', reply_markup=pear_keyboard)


@dp.callback_query_handler(text='cancel')
async def calcel_buying(call: CallbackQuery):
    await call.answer('You are going back.', show_alert=True)
    await call.message.edit_reply_markup()
