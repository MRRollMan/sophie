import asyncio
import math
import time

from aiogram import types, F
from aiogram.exceptions import TelegramRetryAfter
from aiogram.filters import Command
from aiogram.utils.formatting import Text, Code, TextMention

from src.database import Database
from src.filters import CooldownFilter, IsChat, IsCurrentUser, GamesFilter, BetFilter
from src.handlers.games import games_router
from src.types import Games, BetButtonType, BetCallback, BaseGameCallback, BaseGameEnum
from src.utils import TextBuilder
from src.utils.game_messages import get_message
from src.utils.utils import process_regular_bet


@games_router.message(Command(Games.CASINO), IsChat(), CooldownFilter(Games.CASINO, True), GamesFilter())
async def casino_command(message: types.Message, chat_user):
    tb, kb = get_message(chat_user, message.from_user, Games.CASINO)
    await message.answer(tb.render(), reply_markup=kb)


@games_router.callback_query(BetCallback.filter((F.action == BetButtonType.BET) & (F.game == Games.CASINO)),
                             IsCurrentUser(True), CooldownFilter(Games.CASINO, True), BetFilter())
async def casino_callback_bet(callback: types.CallbackQuery, callback_data: BetCallback, chat_user):
    await process_regular_bet(callback, callback_data, chat_user, BaseGameCallback, "🎰", [2, 10], Games.CASINO)


@games_router.callback_query(BaseGameCallback.filter((F.action == BaseGameEnum.PLAY) & (F.game == Games.CASINO)),
                             IsCurrentUser(True), CooldownFilter(Games.CASINO, True), BetFilter())
async def casino_callback_bet_play(callback: types.CallbackQuery,
                                   callback_data: BaseGameCallback, db: Database, chat_user):
    balance = chat_user[3]
    chat_id = callback.message.chat.id
    current_time = int(time.time())

    await db.chat_user.remove_user_russophobia(chat_id, callback.from_user.id, callback_data.bet)
    await db.cooldown.update_user_cooldown(chat_id, callback.from_user.id, Games.CASINO, current_time)
    await callback.message.edit_text(Text("🎰 Довбаний рот цього казино, блядь! "
                                          "Ти хто такий, сука, щоб це зробити?..").as_markdown())

    balance -= callback_data.bet
    user = TextMention(callback.from_user.first_name, user=callback.from_user)
    casino_value = (await callback.message.reply_dice(emoji='🎰')).dice.value

    tb = TextBuilder(user=user)

    if casino_value == 64:
        bet_won = math.ceil(callback_data.bet * 50)
        balance += bet_won + callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, bet_won + callback_data.bet)
        tb.add("🎰 {user}, ЄЄЄЄЄЄЄЄЄЄБАТЬ 777 МАКС ВІН🤑")
        tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
    elif casino_value in [43, 16, 32, 48]:
        bet_won = math.ceil(callback_data.bet * 10)
        balance += bet_won + callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, bet_won + callback_data.bet)
        tb.add("🎰 {user}, ніхуйово")
        tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
    elif casino_value == 22:
        bet_won = math.ceil(callback_data.bet * 5)
        balance += bet_won + callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, bet_won + callback_data.bet)
        tb.add("🎰 {user}, переміг")
        tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
    elif casino_value in [1, 11, 27, 59]:
        bet_won = math.ceil(callback_data.bet * 2)
        balance += bet_won + callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, bet_won + callback_data.bet)
        tb.add("🎰 {user} переміг")
        tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
    elif casino_value in [4, 6, 8, 12, 17, 20, 24, 28, 33, 36, 38, 40, 44, 49, 52, 54, 56, 60]:
        balance += callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, callback_data.bet)
        tb.add("🎰 {user}, наступного разу пощастить")
        tb.add("↩️ Ти повернув {bet} кг\n", True, bet=Code(callback_data.bet))
    else:
        tb.add("🎰 {user} програв")
        tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))

    tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
    await asyncio.sleep(4)
    try:
        await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
        await callback.message.edit_text(tb.render())
    except TelegramRetryAfter:
        pass
