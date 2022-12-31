import random
import calculator

from bot_config import dp, bot
from aiogram import types

CANDIES = 150
MAX_TURN = 28
total = CANDIES
game_flag = False
calc_flag = False


# lucky_flag = False


async def bot_turn(message):
    global total
    global game_flag
    if total > MAX_TURN:
        take = random.randint(1, MAX_TURN)
    else:
        take = total
    total -= take
    if total == 0:
        await bot.send_message(
            message.from_user.id,
            f'Бот победил!'
        )
        game_flag = False
    else:
        await bot.send_message(
            message.from_user.id,
            f'Бот взял со стола {take} конфет. На столе осталось {total}'
        )
        await player_turn(message)
    ## ветка ИИ
    # print(
    #     f'\nХодит {players[first_turn % 2]} '
    #     f'\nНа столе {total}. Берёт: ')
    #
    # if total < MAX_TURN + 1:
    #     step = total
    # else:
    #     if total == AMOUNT:
    #         step = AMOUNT % (MAX_TURN + 1)  # чит-код ИИ
    #         lucky_flag = True
    #     else:
    #         if lucky_flag:
    #             step = MAX_TURN + 1 - step
    #             # ИИ берёт: 29 - взятые игроком прошлом ходу
    #         else:
    #             division = total // MAX_TURN
    #             step = total - (division * MAX_TURN + 1)
    #             if step == -1:
    #                 step = MAX_TURN - 1
    #             if step == 0:
    #                 step = MAX_TURN
    # print(step)


async def player_turn(message):
    await bot.send_message(
        message.from_user.id, text=f'{message.from_user.first_name}, твой ход')


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text=f'Для справки набери /help'
    )
    print(f'{message.from_user.id} - {message.from_user.first_name}')


@dp.message_handler(commands=['help'])
async def help_text(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text=f'Команды:\n'
             f'/help - справка по командам\n'
             f'/game - запуск игры\n'
             f'/calc - вычислить выражение\n'
    )


@dp.message_handler(commands=['calc'])
async def start_calc(message: types.Message):
    global game_flag
    global calc_flag
    game_flag = False
    calc_flag = True
    await bot.send_message(
        message.from_user.id,
        text=f'{message.from_user.first_name} Введи математическое выражение'
             f', которое нужно вычислить:\n'
    )


@dp.message_handler(commands=['game'])
async def start_game(message: types.Message):
    global game_flag
    global total
    global calc_flag
    # global lucky_flag
    game_flag = True
    calc_flag = False
    total = CANDIES
    player_1 = message.from_user.first_name

    await bot.send_message(
        message.from_user.id,
        text=f'{player_1} начнём игру.\n'
             f'На столе {CANDIES} конфет. Играют человек против ИИ. '
             f'Первый ход определяется жеребьёвкой.'
             f'Каждый берёт по очереди не более {MAX_TURN} конфет.'
             f'Все конфеты оппонента достаются сделавшему последний ход.\n'
    )
    # lucky_flag = False  # счастливый флаг ИИ, если ходит первым, то выиграет
    players = [player_1, 'Бот']
    first_turn = random.randint(0, 1)
    await bot.send_message(
        message.from_user.id,
        f'Первым ходит: {players[first_turn]}'
    )
    if players[first_turn] == player_1:
        await player_turn(message)
    else:
        await bot_turn(message)


@dp.message_handler()
async def anything(message: types.Message):
    global total
    global game_flag
    global calc_flag
    # global lucky_flag
    take = message.text
    user = message.from_user.first_name

    if game_flag:
        if message.text.isdigit():
            if 0 < int(take) <= MAX_TURN:
                total -= int(take)
                if total > 0:
                    await bot.send_message(
                        message.from_user.id,
                        f'{user} взял со стола {take} конфет.'
                        f'На столе осталось {total}'
                    )
                    await bot_turn(message)
                else:
                    await bot.send_message(
                        message.from_user.id,
                        f'{user} победил!'
                    )
                    game_flag = False
            else:
                await message.reply(
                    f'{user}, бери от 1 до {MAX_TURN}'
                )
        else:
            await bot.send_message(
                message.from_user.id,
                f'{user}, напиши, сколько будешь брать конфет'
            )
    if calc_flag:
        try:
            result = calculator.evaluation(message.text)
            await bot.send_message(
                message.from_user.id,
                f'Равно: {result}'
            )
            calc_flag = False
        except:
            await bot.send_message(
                message.from_user.id,
                f'{user}, ожидаю ввода формулы'
            )
    await bot.send_message(
        message.from_user.id,
        f'Для справки нажми /help'
    )
