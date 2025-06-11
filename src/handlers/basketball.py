import asyncio
import math
import time
from types import new_class

from aiogram import types, F
from aiogram.exceptions import TelegramRetryAfter
from aiogram.filters import Command
from aiogram.utils.formatting import Text, Code, TextMention

from src.database import Database
from src.filters import CooldownFilter, IsChat, IsCurrentUser, GamesFilter, BetFilter
from src.handlers.games import games_router
from src.types import Games, BetButtonType, BetCallback, BaseGameEnum, BaseGameCallback
from src.utils import TextBuilder
from src.utils.game_messages import get_message
from src.utils.utils import process_regular_bet


@games_router.message(Command(Games.BASKETBALL), IsChat(), CooldownFilter(Games.BASKETBALL, True), GamesFilter())
async def basketball_command(message: types.Message, chat_user):
    tb, kb = get_message(chat_user, message.from_user, Games.BASKETBALL)
    await message.answer(tb.render(), reply_markup=kb)


@games_router.callback_query(BetCallback.filter((F.action == BetButtonType.BET) & (F.game == Games.BASKETBALL)),
                             IsCurrentUser(True), CooldownFilter(Games.BASKETBALL, True), BetFilter())
async def basketball_callback_bet(callback: types.CallbackQuery, callback_data: BetCallback, chat_user):
    await process_regular_bet(callback, callback_data, chat_user, BaseGameCallback, "🏀", 1.5, Games.BASKETBALL)


@games_router.callback_query(BaseGameCallback.filter((F.action == BaseGameEnum.PLAY) & (F.game == Games.BASKETBALL)),
                             IsCurrentUser(True), CooldownFilter(Games.BASKETBALL, True), BetFilter())
async def basketball_callback_bet_play(callback: types.CallbackQuery,
                                       callback_data: BaseGameCallback, db: Database, chat_user):
    balance = chat_user[3]
    chat_id = callback.message.chat.id
    current_time = int(time.time())

    await db.chat_user.remove_user_russophobia(chat_id, callback.from_user.id, callback_data.bet)
    await db.cooldown.update_user_cooldown(chat_id, callback.from_user.id, Games.BASKETBALL, current_time)
    await callback.message.edit_text(Text("🏀 Кидаю м'яч..").as_markdown())

    balance -= callback_data.bet
    user = TextMention(callback.from_user.first_name, user=callback.from_user)
    basketball_value = (await callback.message.reply_dice(emoji='🏀')).dice.value

    tb = TextBuilder(user=user)

    if basketball_value in [4, 5]:
        bet_won = math.ceil(callback_data.bet * 2)
        balance += bet_won + callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, bet_won + callback_data.bet)
        tb.add("🏀 {user} переміг")
        tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
    elif basketball_value == 3:
        balance += callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, callback_data.bet)
        tb.add("🏀 {user}, бля, ну майже")
        tb.add("↩️ Ти повернув {bet} кг\n", True, bet=Code(callback_data.bet))
    else:
        tb.add("🏀 {user} програв")
        tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))

    tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
    await asyncio.sleep(4)
    try:
        await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
        await callback.message.edit_text(tb.render())
    except TelegramRetryAfter:
        pass
