from aiogram import types, Dispatcher
from config import bot, ADMIN
from database.bot_db import sql_commands_get_all_id


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer("Ты не мой БОСС!!!")
        elif not message.reply_to_message:
            await message.answer("Комманда должна быть ответом на сообщение!")
        else:
            await message.bot.kick_chat_member(message.chat.id,
                                               user_id=message.reply_to_message.from_user.id)
            await message.answer(f"Пользователь {message.reply_to_message.from_user.full_name} "
                                 f"был забанен по воле {message.from_user.full_name}")
    else:
        await message.answer("Это работает только в группах")


async def reklama(message: types.Message):
    if message.from_user.id in ADMIN:
        result = await sql_commands_get_all_id()
        for id in result:
            await bot.send_message(id[0], message.text[3:])
    else:
        await message.answer("Ты не мой БОСС!!!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix="!/")
    dp.register_message_handler(reklama, commands=['R'])
