import asyncio
import math
import time

from aiogram import types, F
from aiogram.exceptions import TelegramRetryAfter
from aiogram.filters import Command
from aiogram.utils.formatting import Text, Code, TextMention

from src.database import Database
from src.filters import CooldownFilter, IsChat, IsCurrentUser, GamesFilter
from src.handlers.games import games_router
from src.types import Games, BetButtonType, BetCallback, BaseGameCallback, BaseGameEnum
from src.utils import TextBuilder
from src.utils.game_messages import get_casino_message
from src.utils.utils import process_regular_bet


@games_router.message(Command(Games.CASINO), IsChat(), CooldownFilter(Games.CASINO, True), GamesFilter())
async def casino_command(message: types.Message, chat_user):
    tb, kb = get_casino_message(chat_user, message.from_user)
    await message.answer(tb.render(), reply_markup=kb.as_markup())


@games_router.callback_query(BetCallback.filter((F.action == BetButtonType.BET) & (F.game == Games.CASINO)),
                             IsCurrentUser(True), CooldownFilter(Games.CASINO, True))
async def casino_callback_bet(callback: types.CallbackQuery, callback_data: BetCallback, chat_user):
    await process_regular_bet(callback, callback_data, chat_user, BaseGameCallback, "🎰", [2, 10], Games.CASINO)


@games_router.callback_query(BaseGameCallback.filter((F.action == BaseGameEnum.PLAY) & (F.game == Games.CASINO)),
                             IsCurrentUser(True), CooldownFilter(Games.CASINO, True))
async def casino_callback_bet_play(callback: types.CallbackQuery,
                                   callback_data: BaseGameCallback, db: Database, chat_user):
    balance = chat_user[3]
    chat_id = callback.message.chat.id
    current_time = int(time.time())

    await db.cooldown.update_user_cooldown(chat_id, callback.from_user.id, Games.CASINO, current_time)
    await callback.message.edit_text(Text("🎰 Довбаний рот цього казино, блядь! "
                                          "Ти хто такий, сука, щоб це зробити?..").as_markdown())

    user = TextMention(callback.from_user.first_name, user=callback.from_user)
    casino_value = (await callback.message.reply_dice(emoji='🎰')).dice.value

    tb = TextBuilder(user=user)

    if casino_value == 64:
        bet_won = math.ceil(callback_data.bet * 50)
        new_balance = balance + bet_won
        tb.add("🏆 {user}, ну ніхуя собі")
        tb.add("🎰 Ти виграв: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    elif casino_value in [43, 16, 32, 48]:
        bet_won = math.ceil(callback_data.bet * 10)
        new_balance = balance + bet_won
        tb.add("🏆 {user}, пєрємога")
        tb.add("🎰 Ти виграв: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    elif casino_value == 22:
        bet_won = math.ceil(callback_data.bet * 5)
        new_balance = balance + bet_won
        tb.add("🏆 {user}, пєрємога")
        tb.add("🎰 Ти виграв: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    elif casino_value in [1, 11, 27, 59]:
        bet_won = math.ceil(callback_data.bet * 2)
        new_balance = balance + bet_won
        tb.add("🏆 {user} пєрємога")
        tb.add("🎰 Ти виграв: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    elif casino_value in [4, 6, 8, 12, 17, 20, 24, 28, 33, 36, 38, 40, 44, 49, 52, 54, 56, 60]:
        bet_won = math.ceil(callback_data.bet)
        new_balance = balance
        tb.add("🏆 {user} бля шо за рахіт грає")
        tb.add("🎰 Ти повернув: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    else:
        new_balance = balance - callback_data.bet
        tb.add("😔 {user} відсмоктав")
        tb.add("🎰 Пройоб: {bet} кг\n", True, bet=Code(callback_data.bet))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    await asyncio.sleep(4)
    try:
        await callback.bot.answer_callback_query(callback.id, "Шишки шишки шишки шишки шишки")
        await callback.message.edit_text(tb.render())
    except TelegramRetryAfter:
        pass
    else:
        await db.chat_user.update_user_russophobia(chat_id, callback.from_user.id, new_balance)
