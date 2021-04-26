from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline import buy_item
from keyboards.inline.callback_datas import add_item
from states.commands import get_categories, count_items, make_callback_data, get_cat_items


async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    categories = get_categories()['categories']
    for category in categories:
        number_of_items = await count_items(category['name'])
        if number_of_items != 0:
            button_text = f"{category['name']} ({number_of_items} шт)"
        else:
            button_text = f"{category['name']} (нет в наличии)"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category['name'])

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup


async def items_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    items = await get_cat_items(category)
    for item in items:
        button_text = f"{item[0]['name']} - ₽{item[0]['price']}"
        callback_data = make_callback_data(level=CURRENT_LEVEL+1,
                                           category=category,
                                           item_id=item[0]['id'])
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup


def item_keyboard(category, item_id):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row(
        InlineKeyboardButton(text="Купить",
                             callback_data=buy_item.new(item_id=item_id))
    )
    markup.row(
        InlineKeyboardButton(text="Добавить в карзину",
                             callback_data=add_item.new(item_id=item_id))
    )
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             category=category)
        )
    )
    return markup