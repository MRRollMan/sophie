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
from src.utils.game_messages import get_darts_message
from src.utils.utils import process_regular_bet


@games_router.message(Command(Games.DARTS), IsChat(), CooldownFilter(Games.DARTS, True), GamesFilter())
async def darts_command(message: types.Message, chat_user):
    tb, kb = get_darts_message(chat_user, message.from_user)
    await message.answer(tb.render(), reply_markup=kb.as_markup())


@games_router.callback_query(BetCallback.filter((F.action == BetButtonType.BET) & (F.game == Games.DARTS)),
                             IsCurrentUser(True))
async def darts_callback_bet(callback: types.CallbackQuery, callback_data: BetCallback, chat_user):
    await process_regular_bet(callback, callback_data, chat_user, BaseGameCallback, "🎯", 2, Games.DARTS)


@games_router.callback_query(BaseGameCallback.filter((F.action == BaseGameEnum.PLAY) & (F.game == Games.DARTS)),
                             IsCurrentUser(True))
async def darts_callback_bet_play(callback: types.CallbackQuery, callback_data: BaseGameCallback, db: Database, chat_user):
    balance = chat_user[3]
    chat_id = callback.message.chat.id
    current_time = int(time.time())
    await callback.message.edit_text(Text("🎯 У твоєї сестри такий солодкий вареник").as_markdown())

    user = TextMention(callback.from_user.first_name, user=callback.from_user)
    darts_value = (await callback.message.reply_dice(emoji='🎯')).dice.value

    tb = TextBuilder(user=user)

    if darts_value == 6:
        bet_won = math.ceil(callback_data.bet * 2)
        new_balance = balance + bet_won
        tb.add("🏆 {user}, пєрємога")
        tb.add("🎯 Ти виграв: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    elif darts_value in [4, 5]:
        bet_won = math.ceil(callback_data.bet)
        new_balance = balance
        tb.add("🏆 {user} бля шо за рахіт грає")
        tb.add("🎯 Ти повернув: {bet_won} кг\n", True, bet_won=Code(bet_won))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    else:
        new_balance = balance - callback_data.bet
        tb.add("😔 {user} відсмоктав")
        tb.add("🎯 Пройоб: {bet} кг\n", True, bet=Code(callback_data.bet))
        tb.add("🏷️ В тебе: {new_balance} кг", True, new_balance=Code(new_balance))
    await asyncio.sleep(4)
    try:
        await callback.bot.answer_callback_query(callback.id, "Кана́біс (лат. Cánnabis) — узагальнена назва, що об'єднує низку психоактивних речовин, одержуваних з частин квітучих рослин роду коноплі. Марихуа́на, гашиш і гашишне масло є прикладами таких засобів")
        await callback.message.edit_text(tb.render())
    except TelegramRetryAfter:
        pass
    else:
        await db.cooldown.update_user_cooldown(chat_id, callback.from_user.id, Games.DARTS, current_time)
        await db.chat_user.update_user_russophobia(chat_id, callback.from_user.id, new_balance)
