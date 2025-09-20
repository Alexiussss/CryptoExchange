from aiogram import Dispatcher
from aiogram.types import Message

from keyboards import menu


async def check_sub(user_id):
    user_check = bot.get_chat_member(user_id=user_id)


async def welcome(message: Message):
    await message.answer('Добро пожаловать!\n'  
                         'Текст\n'  
                         'Текст', reply_markup=await menu())


def register_user_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(welcome, commands=['start'])