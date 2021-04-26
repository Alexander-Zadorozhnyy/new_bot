from aiogram import types
from aiogram.dispatcher.filters import Command
from asyncio import sleep
from loader import dp, bot


@dp.message_handler(Command('dice'))
async def dice_game(message: types.Message):
    await message.answer('Bot turn: ')
    await sleep(1)
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer('Your turn: ')
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)
    if bot_data > user_data:
        await message.answer('You lost :(')
    elif bot_data < user_data:
        await message.answer('You WIN! :)')
    else:
        await message.answer('-Nobody win- :0')
