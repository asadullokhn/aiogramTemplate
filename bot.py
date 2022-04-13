from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

from config import *
from database.database import UserDatabase

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
userDb = UserDatabase()
