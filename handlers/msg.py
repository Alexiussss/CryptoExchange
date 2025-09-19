from aiogram import Dispatcher
from aiogram.types import Message

from keyboards import menu


async def welcome(message: Message):
    await message.answer('Добро пожаловать!\n'  
                         'Текст\n'  
                         'Текст', reply_markup=await menu())


def register_user_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(welcome, commands=['start'])