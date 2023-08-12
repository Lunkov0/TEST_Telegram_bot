from aiogram import types, Dispatcher
from create_bot import bot, dp
from data_base import sqlite_db
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личные сообщения: \nhttps://t.me/lunkovBot')


# Выгружаем данные из базы
@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


# Таким образом мы пробрасываем функции в файл bot_telegram
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])





















