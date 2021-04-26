from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from db import db_session

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
db_session.global_init("db/user_info.db")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)