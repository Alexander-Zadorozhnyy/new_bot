from aiogram.dispatcher.filters.state import StatesGroup, State


class AddNewItem(StatesGroup):
    name = State()
    content = State()
    category = State()
    about = State()
    characteristics = State()
    price = State()
    img = State()


class DelQuestion(StatesGroup):
    id = State()