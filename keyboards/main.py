from aiogram import types

async def menu():
    inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    inline.add(types.KeyboardButton('🗃 Меню'))
    return inline


# async def main_menu():
