from aiogram.utils import executor
from handlers import dp


if __name__ == '__main__':
    print(f'Бот запущен')
    executor.start_polling(dispatcher=dp)
    print(f'Бот остановлен')