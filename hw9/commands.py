import random

from bot_config import dp, bot
from aiogram import types

CANDIES = 150
MAX_TURN = 28
total = CANDIES
game_flag = False
lucky_flag = False


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
        message.from_user.id, text=f'{message.from_user.first_name} твой ход')
    # else:
    # # ветка игрока
    # step = int(input(
    #     f'\nХодит {players[first_turn % 2]} \nНа столе {total} Бери: '))
    # while step > MAX_TURN or step > total:
    #     step = int(input(
    #         f'\nЗа один ход можно взять {MAX_TURN} конфет, '
    #         f'попробуй еще раз: '))

    # total = total - step
    # first_turn += 1


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text=f'Для справки набери /help'
    )


@dp.message_handler(commands=['help'])
async def help_text(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text=f'Команды:\n'
             f'/help - справка по командам\n'
             f'/game - запуск игры'
    )


@dp.message_handler(commands=['game'])
async def start_game(message: types.Message):
    global game_flag
    global total
    global lucky_flag
    game_flag = True
    total = CANDIES
    player_1 = message.from_user.first_name
    player_2 = 'PC'
    lucky_flag = False  # счастливый флаг ИИ, если ходит первым, то выиграет
    players = [player_1, player_2]
    first_turn = random.randint(0, 1)
    await bot.send_message(
        message.from_user.id,
        f'первым ходит: {players[first_turn]}'
    )
    await bot.send_message(
        message.from_user.id,
        text=f'{message.from_user.first_name} начнём игру.\n'
             f'На столе {CANDIES} конфет. Играют человек против ИИ. '
             # f'Первый ход определяется жеребьёвкой.'
             f'Каждый берёт по очереди не более {MAX_TURN} конфет.'
             f'Все конфеты оппонента достаются сделавшему последний ход.\n'
    )
    await player_turn(message)



@dp.message_handler()
async def anything(message: types.Message):
    global total
    global game_flag
    global lucky_flag
    take = message.text
    player_1 = message.from_user.first_name
    player_2 = 'PC'

    if game_flag:
        if message.text.isdigit():

            if 0 < int(take) <= MAX_TURN:
                total -= int(take)
                if total > 0:
                    await bot.send_message(
                        message.from_user.id,
                        f'{player_1} взял со стола {take} конфет.'
                        f'На столе осталось {total}'
                    )
                    await bot_turn(message)
                    await player_turn(message)
                else:
                    await bot.send_message(
                        message.from_user.id,
                        f'{player_1} победил!'
                    )
            else:
                await message.reply(
                    f'{player_1} да ты жадина, '
                    f'не хочешь ли взять поменьше?'
                )
        else:
            await bot.send_message(
                message.from_user.id,
                f'{player_1} напиши, сколько будешь брать конфет'
            )

        # return f'На столе осталось {total} конфет ' \
        #        f'\nПобедил {players[(first_turn % 2) - 1]}'
