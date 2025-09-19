from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token="8472269756:AAGgUkABIdYAIE7VFaclNAm8Kz40NEIVZk4")
dp = Dispatcher(bot, storage=MemoryStorage())