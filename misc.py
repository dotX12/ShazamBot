import logging
from aiogram import Bot, Dispatcher
from shazamio import Shazam

API_TOKEN = 'TOKEN'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
shazam = Shazam()
