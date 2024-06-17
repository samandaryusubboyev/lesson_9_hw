# ьфшт.py module
import logging
from db import Database
from db import menu_keyboard, addresses_keyboard

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "token"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2(username, full_name, user_id) VALUES('{username}', '{full_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Sizni yana ko'rganimdan xursandman @{username}", reply_markup=menu_keyboard)
    else:
        await Database.connect(query, "insert")
        await message.reply(f"Welcome @{username}", reply_markup=menu_keyboard)

@dp.message_handler(lambda message: message.text == "Menyu")
async def menu(message: types.Message):
    await message.answer("Menyular", reply_markup=addresses_keyboard)

@dp.message_handler(lambda message: message.text == "Back")
async def menu(message: types.Message):
    await message.answer("Menyular", reply_markup=menu_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    old style:
    await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
