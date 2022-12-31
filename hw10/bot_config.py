import asyncio
import logging
from config_reader import config
from aiogram import Bot, Dispatcher

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)
