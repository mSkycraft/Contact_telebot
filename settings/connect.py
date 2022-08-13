from aiogram import Bot,Dispatcher,types
from settings.config import API

bot = Bot(token=API)
dp = Dispatcher(bot)
