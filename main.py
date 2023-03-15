import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bots_data import BOT_TOKEN

storage = MemoryStorage()

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot, storage=storage)
