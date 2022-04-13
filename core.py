from resources import messages as msgz, keyboards as kybrdz
from bot import *

from aiogram.types import InputFile
from datetime import datetime


async def admin_commands(msg: Message):
    text = msg.text
    user_id = msg.from_user.id

    if text.startswith('/post'):
        ad_msg_id = text.split()[-1]

        sent_count = 0
        blocked_count = 0

        for __user_id in await userDb.get_all_user_ids():
            try:
                await bot.copy_message(__user_id[0], PRIVATE_CHAT_ID, ad_msg_id)
                sent_count += 1
            except:
                blocked_count += 1

        await msg.reply(f"👤 Sent count - {sent_count}\n⭕ Blocked users count - {blocked_count}")

    elif text.startswith('/get_database'):

        now = str(datetime.now().strftime("%d%B"))

        file_name = f"database{now}file.db"

        file = InputFile(DATABASE_PATH, file_name)

        await bot.send_document(user_id, file)

    elif text.startswith('/get_users'):

        count = await userDb.get_count_of_users()

        await bot.send_message(user_id, f"👤 <b>Total: {count[0][0]}</b>")


async def on_start(msg: Message):
    user_id = msg.from_user.id
    users_name = msg.from_user.full_name

    user = await userDb.get(user_id)

    if user:
        await bot.send_message(user_id, f"Hi {users_name}")

    else:
        await userDb.add(user_id)
        await bot.send_message(user_id, f"Hi {users_name}")


async def on_message(msg: Message):
    pass


async def on_phone(msg: Message):
    pass


async def on_callback(msg: CallbackQuery):
    pass