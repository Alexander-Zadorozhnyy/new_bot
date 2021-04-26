import emoji

from data.config import ADMINS
from keyboards.default.admin_markup import admin_mark
from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(equals=['Назад к панели администратора ' + emoji.emojize(':closed_book:'), '/admin']))
async def show_menu(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer('Панель администратора', reply_markup=admin_mark)
    else:
        await message.answer("У вас нет прав на использование этой команды!")