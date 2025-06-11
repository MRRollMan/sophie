import asyncio
import math
import time

from aiogram import types, F
from aiogram.exceptions import TelegramRetryAfter
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton
from aiogram.utils.formatting import Text, Code, TextMention
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.database import Database
from src.filters import CooldownFilter, IsChat, IsCurrentUser, GamesFilter, BetFilter
from src.handlers.games import games_router
from src.types import Games, BetButtonType, BetCallback, DiceCallback, DiceParityEnum
from src.utils import TextBuilder, is_can_play
from src.utils.game_messages import get_message


@games_router.message(Command(Games.DICE), IsChat(), CooldownFilter(Games.DICE, True), GamesFilter())
async def dice_command(message: types.Message, chat_user):
    tb, kb = get_message(chat_user, message.from_user, Games.DICE)
    await message.answer(tb.render(), reply_markup=kb)


@games_router.callback_query(BetCallback.filter((F.action == BetButtonType.BET) & (F.game == Games.DICE)),
                             IsCurrentUser(True), CooldownFilter(Games.DICE, True), BetFilter())
async def dice_callback_bet(callback: types.CallbackQuery, callback_data: BetCallback, chat_user):
    balance = chat_user[3]
    bet = callback_data.bet
    potential_win = math.ceil(bet * 2)
    user = callback.from_user

    if not await is_can_play(balance, bet, callback):
        return

    tb, kb = TextBuilder(), InlineKeyboardBuilder()
    even = DiceCallback(user_id=user.id, bet=bet, parity=DiceParityEnum.EVEN)
    odd = DiceCallback(user_id=user.id, bet=bet, parity=DiceParityEnum.ODD)
    back = DiceCallback(user_id=user.id, bet=bet, parity=DiceParityEnum.BACK)
    cancel = DiceCallback(user_id=user.id, bet=bet, parity=DiceParityEnum.CANCEL)

    kb.row(InlineKeyboardButton(text="➗ Парне", callback_data=even.pack()),
           InlineKeyboardButton(text="✖️ Непарне", callback_data=odd.pack()), width=2)
    kb.row(InlineKeyboardButton(text="↩️ Назад", callback_data=back.pack()),
           InlineKeyboardButton(text="⛔️ Нахуй", callback_data=cancel.pack()), width=1)

    tb.add("🎲 {user} граємо?\n", user=TextMention(user.first_name, user=user))
    tb.add("🪙 Ставка: {bet} кг", True, bet=Code(bet))
    tb.add("💰 Можливий виграш: {potential_win} кг", True, potential_win=Code(potential_win))

    await callback.message.edit_text(text=tb.render(), reply_markup=kb.as_markup())


@games_router.callback_query(DiceCallback.filter(F.parity.in_({DiceParityEnum.EVEN, DiceParityEnum.ODD})),
                             IsCurrentUser(True), CooldownFilter(Games.DICE, True), BetFilter())
async def dice_callback_bet_play(callback: types.CallbackQuery, callback_data: DiceCallback, db: Database, chat_user):
    balance = chat_user[3]
    chat_id = callback.message.chat.id
    current_time = int(time.time())

    await db.chat_user.remove_user_russophobia(chat_id, callback.from_user.id, callback_data.bet)
    await db.cooldown.update_user_cooldown(chat_id, callback.from_user.id, Games.DICE, current_time)
    await callback.message.edit_text(Text("🎲 Кидаю кістки..").as_markdown())

    balance -= callback_data.bet
    user = TextMention(callback.from_user.first_name, user=callback.from_user)
    dice_value = (await callback.message.reply_dice()).dice.value
    parity = 0 if callback_data.parity == DiceParityEnum.EVEN else 1

    tb = TextBuilder(user=user, dice_value=Code(dice_value), parity='парне' if not dice_value % 2 else 'непарне')

    if dice_value % 2 == parity:
        bet_won = math.ceil(callback_data.bet * 2)
        balance += bet_won + callback_data.bet
        await db.chat_user.add_user_russophobia(chat_id, callback.from_user.id, bet_won + callback_data.bet)
        tb.add("🎲 {dice_value}, {parity}. {user} переміг")
        tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
    else:
        tb.add("🎲 {dice_value}, {parity}. {user} програв")
        tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))

    tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
    await asyncio.sleep(4)
    try:
        await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
        await callback.message.edit_text(tb.render())
    except TelegramRetryAfter:
        pass
