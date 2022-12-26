from aiogram import Bot, Dispatcher

PATH = 'token.secret'
with open(PATH, 'r', encoding='utf-8') as file:
    token_txt = file.read()

bot = Bot(token=token_txt)
dp = Dispatcher(bot)
