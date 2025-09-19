from aiogram.utils import executor
from utils import dp
from handlers import register_all_handlers


def on_startup(dp):
    register_all_handlers(dp)
    print('Bot is running...')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup(dp))