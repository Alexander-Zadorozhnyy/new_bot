import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.question_markup import question
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from loader import dp
from states.commands import get_quest, del_question
from states.state_for_adding_item import DelQuestion


@dp.message_handler(Text(equals=['Тех.Поддержка ' + emoji.emojize(':wrench:')]))
async def show_menu(message: Message):
    await message.answer('Выберете нужный раздел: ', reply_markup=question)


@dp.message_handler(Text(equals=['Показать все вопросы']))
async def show_users(message: types.Message):
    await message.answer("Список вопросов задаваемых пользователями на сайте: \n")
    users = await get_quest()
    print(users)
    for i in range(len(users)):
        quests = f'id - {users[i]["id"]} \n имя - {users[i]["name"]} \n email - {users[i]["email"]} \n ' \
             f'тема вопроса - {users[i]["theme"]} \n вопрос - {users[i]["question"]}'
        await message.answer(quests)


@dp.message_handler(Text(equals=['Удалить вопрос']), state=None)
async def del_question_db(message: types.Message):
    await DelQuestion.id.set()
    await message.answer('Введите id вопроса, который нужно удалить')


@dp.message_handler(state=DelQuestion.id)
async def id_q1(message: types.Message, state: FSMContext):
    answer = message.text
    users = await get_quest()
    print([users[i]["id"] for i in range(len(users))])
    if int(answer) in [users[i]["id"] for i in range(len(users))]:
        await del_question(answer)
        await message.answer('Вопрос удален')
    else:
        await message.answer('Вопроса с таким id не существует!')
    await state.finish()
