import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot)
