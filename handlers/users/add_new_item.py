import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.config import ADMINS
from states.commands import post_item
from loader import dp
from states.state_for_adding_item import AddNewItem


@dp.message_handler(Text(equals=['Добавить товар ' + emoji.emojize(':red_circle:')]), state=None)
async def add_item(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Вы начали процесс добавления нового товара\n"
                             "для отмены пропишите stop \n"
                             "Введите имя товара:")
        await AddNewItem.name.set()
    else:
        await message.answer("У вас нет прав на использование этой команды!")


@dp.message_handler(state=AddNewItem.name)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer != 'stop':
        await state.update_data(name=answer)
        await message.answer('Введите название изображения:')
        await AddNewItem.next()
    else:
        await state.finish()


@dp.message_handler(state=AddNewItem.content)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer != 'stop':
        if '.jpg' in answer or '.jpeg' in answer or '.png' in answer:
            await state.update_data(content=answer)
            await message.answer('Введите категорию вашего товара из списка (Телефоны, Планшеты, Часы, Телевизоры):')
            await AddNewItem.next()
        else:
            await message.answer('Введите корректное название, в формате (###.jpg/jpeg/png)')
            answer = message.text
    else:
        await state.finish()


@dp.message_handler(state=AddNewItem.category)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer != 'stop':
        if answer in ['Телефоны', 'Планшеты', 'Часы', 'Телевизоры']:
            await state.update_data(category=answer)
            await message.answer('Введите информацию о товаре:')
            await AddNewItem.next()
        else:
            await message.answer('Введите корректную категорию!')
            answer = message.text
    else:
        await state.finish()


@dp.message_handler(state=AddNewItem.about)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer != 'stop':
        await state.update_data(about=answer)
        await message.answer('Введите характеристики вашего устройства в формате: \n'
                             '|имя характеристики:сама характеристика%|:')
        await AddNewItem.next()
    else:
        await state.finish()


@dp.message_handler(state=AddNewItem.characteristics)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer != 'stop':
        await state.update_data(characteristics=answer)
        await message.answer('Введите цену товара: ')
        await AddNewItem.next()
    else:
        await state.finish()


@dp.message_handler(state=AddNewItem.price)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer != 'stop':
        await state.update_data(price=answer)
        await message.answer('Загрузите фото в формате 200х300: ')
        await AddNewItem.next()
    else:
        await state.finish()


@dp.message_handler(state=AddNewItem.img, content_types=['photo'])
async def answer_q2(message, state: FSMContext):
    answer = await message.photo[-1].download('test.jpg')
    with open('test.jpg', 'rb') as f:
        a = f.read()
    answer = a.decode('latin1')
    if answer != 'stop':
        data = await state.get_data()
        await post_item(name=data.get("name"), content=data.get("content"),
                        category=str(data.get("category")[0]).upper() + str(data.get("category")[1:]).lower(),
                        about=data.get("about"),
                        characteristics=data.get("characteristics"), price=data.get("price"), img=answer)
        await message.answer(f"Ваш товар успешно добавлен")
        await state.finish()
    else:
        await state.finish()
