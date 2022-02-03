from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import *

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
