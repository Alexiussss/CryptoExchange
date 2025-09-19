from aiogram import Dispatcher
from .msg import register_user_handler

def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handler(dp)