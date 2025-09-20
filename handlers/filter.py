# from aiogram import types
# from aiogram.dispatcher.filters import BoundFilter
# from database import select_user, add_user
#
#
# class IsUser(BoundFilter):
#     async def check(self, message: types.Message):
#         user_info = await select_user(message.chat.id)
#
#         if not user_info:
#             await add_user(message.chat.id)
#
#         return False