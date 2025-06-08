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
from src.utils.game_messages import get_football_message
from src.utils.utils import process_regular_bet


@games_router.message(Command(Games.FOOTBALL), IsChat(), CooldownFilter(Games.FOOTBALL, True), GamesFilter())
async def football_command(message: types.Message, chat_user):
    tb, kb = get_football_message(chat_user, message.from_user)
    await message.answer(tb.render(), reply_markup=kb.as_markup())


@games_router.callback_query(BetCallback.filter((F.action == BetButtonType.BET) & (F.game == Games.FOOTBALL)),
                             IsCurrentUser(True))
async def football_callback_bet(callback: types.CallbackQuery, callback_data: BetCallback, chat_user):
    await process_regular_bet(callback, callback_data, chat_user, BaseGameCallback, "⚽", 1.5, Games.FOOTBALL)


@games_router.callback_query(BaseGameCallback.filter((F.action == BaseGameEnum.PLAY) & (F.game == Games.FOOTBALL)),
                             IsCurrentUser(True))
async def football_callback_bet_play(callback: types.CallbackQuery,
                                     callback_data: BaseGameCallback, db: Database, chat_user):
    balance = chat_user[3]
    chat_id = callback.message.chat.id
    current_time = int(time.time())
    await callback.message.edit_text(Text("⚽ Який шанс того, що цей м'яч був у твоїй мамі?").as_markdown())

    user = TextMention(callback.from_user.first_name, user=callback.from_user)
    football_value = (await callback.message.reply_dice(emoji='⚽')).dice.value

    tb = TextBuilder(user=user)

    if football_value in [3, 4, 5]:
        bet_won = math.ceil(callback_data.bet * 1.5)
        new_balance = balance + bet_won
        tb.add("🏆 {user}, пєрємога")
        tb.add("⚽ Ти виграв: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    else:
        new_balance = balance - callback_data.bet
        tb.add("😔 {user} відсмоктав")
        tb.add("⚽ Пройоб: {bet} кг\n", True, bet=Code(callback_data.bet))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    await asyncio.sleep(4)
    try:
        await callback.bot.answer_callback_query(callback.id, "Не хапав, значить не жив")
        await callback.message.edit_text(tb.render())
    except TelegramRetryAfter:
        pass
    else:
        await db.cooldown.update_user_cooldown(chat_id, callback.from_user.id, Games.FOOTBALL, current_time)
        await db.chat_user.update_user_russophobia(chat_id, callback.from_user.id, new_balance)
