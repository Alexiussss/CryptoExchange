from aiogram.utils import executor
from utils import dp


def on_startup(dp):
    print('Bot is running...')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup(dp))