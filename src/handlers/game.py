import asyncio
import math
import random
import time

from aiogram import types, F
from aiogram.exceptions import TelegramRetryAfter
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton
from aiogram.utils.formatting import Code, TextMention
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.config import config
from src.database import Database
from src.filters import CooldownFilter, IsChat, IsCurrentUser, GamesFilter
from src.handlers.games import games_router
from src.types import Games, BetButtonType, BetCallback, GameCallback, GameCellEnum
from src.utils import TextBuilder, is_can_play
from src.utils.game_messages import get_game_message


@games_router.message(Command(Games.GAME), IsChat(), CooldownFilter(Games.GAME, True), GamesFilter())
async def game_command(message: types.Message, chat_user):
    tb, kb = get_game_message(chat_user, message.from_user)
    await message.answer(tb.render(), reply_markup=kb.as_markup())


@games_router.callback_query(BetCallback.filter((F.action == BetButtonType.BET) & (F.game == Games.GAME)),
                             IsCurrentUser(True), CooldownFilter(Games.GAME, True))
async def game_callback_bet(callback: types.CallbackQuery, callback_data: BetCallback, chat_user):
    balance = chat_user[3]
    bet = callback_data.bet
    potential_win = math.ceil(bet * 2)
    user = callback.from_user

    if not await is_can_play(balance, bet, callback):
        return

    tb, kb = TextBuilder(), InlineKeyboardBuilder()
    cells = [GameCallback(user_id=user.id, bet=bet, cell=GameCellEnum.CELL) for _ in range(9)]
    back = GameCallback(user_id=user.id, bet=bet, cell=GameCellEnum.BACK)
    cancel = GameCallback(user_id=user.id, bet=bet, cell=GameCellEnum.CANCEL)

    kb.row(*[InlineKeyboardButton(text="🧌", callback_data=cell.pack()) for cell in cells], width=3)
    kb.row(InlineKeyboardButton(text="⬅️️ Назад", callback_data=back.pack()),
           InlineKeyboardButton(text="❌ Нахуй", callback_data=cancel.pack()), width=1)

    tb.add("🧟‍♂️ {user} а може ти москаль?\n", user=TextMention(user.first_name, user=user))
    tb.add("🏷️ Твоя ставка: {bet} кг", True, bet=Code(bet))
    tb.add("💰 Можливий виграш: {potential_win} кг", True, potential_win=Code(potential_win))

    await callback.message.edit_text(text=tb.render(), reply_markup=kb.as_markup())


@games_router.callback_query(GameCallback.filter(F.cell == GameCellEnum.CELL), IsCurrentUser(True),
                             CooldownFilter(Games.GAME, True))
async def game_callback_bet_play(callback: types.CallbackQuery, callback_data: GameCallback, db: Database, chat_user):
    balance = chat_user[3]
    chat_id = callback.message.chat.id
    current_time = int(time.time())

    await db.cooldown.update_user_cooldown(chat_id, callback.from_user.id, Games.GAME, current_time)
    user = TextMention(callback.from_user.first_name, user=callback.from_user)
    win = random.random() < config.RANDOMGAMES

    tb = TextBuilder(user=user)

    if win:
        bet_won = math.ceil(callback_data.bet * 2)
        new_balance = balance + bet_won
        tb.add("🏆 {user}, пєрємога")
        tb.add("🧟‍♂️ Ти виграв: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    else:
        new_balance = balance - callback_data.bet
        tb.add("😔 {user} відсмоктав")
        tb.add("🧟‍♂️ Пройоб: {bet} кг\n", True, bet=Code(callback_data.bet))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))

    try:
        await callback.message.edit_text("🧌 Був до речі вночі в твоїй шафі\\.\\.")
        await asyncio.sleep(4)
        await callback.bot.answer_callback_query(callback.id, "Хапати і вбиває насправді весело")
        await callback.message.edit_text(tb.render())
    except TelegramRetryAfter:
        pass
    else:
        await db.chat_user.update_user_russophobia(chat_id, callback.from_user.id, new_balance)
