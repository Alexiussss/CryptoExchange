from aiogram import Dispatcher
from aiogram.types import Message

from utils import bot

from keyboards import menu, main_menu



async def check_sub(user_id):
    user_check = await bot.get_chat_member(chat_id=-1002042523636, user_id=user_id)
    return user_check.status in ['member', 'administrator', 'creator']


async def welcome(message: Message):
    await message.answer('Добро пожаловать!\n'  
                         'Текст\n'  
                         'Текст', reply_markup=await menu())


async def menu_check(message: Message):
    if await check_sub(message.from_user.id):
        await message.answer('Вы в главном меню:', reply_markup=await main_menu())
    else:
        await message.answer('Ви не підписались')


def register_user_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(welcome, commands=['start'])

    dp.register_message_handler(menu_check, text='🗃 Меню')