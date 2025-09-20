from aiogram import types

async def menu():
    inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    inline.add(types.KeyboardButton(text='🗃 Меню'))
    return inline


async def main_menu():
    inline = types.InlineKeyboardMarkup()
    inline.add(types.InlineKeyboardButton(text='Купить криптовалюту', callback_data='buy'))
    inline.add(types.InlineKeyboardButton(text='Обмен криптовалют', callback_data='exchange'))
    inline.add(types.InlineKeyboardButton(text='Пополнить баланс', callback_data='deposit'))
    inline.add(types.InlineKeyboardButton(text='Кабинет', callback_data='profile'))
    return inline