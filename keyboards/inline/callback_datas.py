from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData('buy', 'item_name', 'quantity')

menu_cd = CallbackData("show_menu", "level", "category", "item_id")
buy_item = CallbackData("buy", "item_id")
add_item = CallbackData("add", "item_id")
