from bot import *

import core


# accessible only for admins
@dp.message_handler(commands=['post', 'get_users', 'get_database'])
async def admin_commands(msg: Message):
    if msg.from_user.id in ADMIN_ID:
        await core.on_start(msg)


@dp.message_handler(commands=['start'])
async def on_start(msg: Message):
    await core.on_start(msg)


@dp.message_handler(content_types=['text'])
async def on_message(msg: Message):
    await core.on_message(msg)


@dp.message_handler(content_types=['phone'])
async def on_phone(msg: Message):
    await core.on_phone(msg)


@dp.callback_query_handler()
async def on_callback(msg: CallbackQuery):
    await core.on_callback(msg)


if __name__ == '__main__':
    print('Started!')
    executor.start_polling(dp)
