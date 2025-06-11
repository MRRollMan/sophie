import random

from aiogram import Router, types, F
from aiogram.filters import Command, or_f
from aiogram.utils.formatting import Code, TextMention

from src.database import Database
from src.filters import CooldownFilter, IsChat, IsCurrentUser
from src.types import Games, BetButtonType, BetCallback, BaseGameCallback, BaseGameEnum, GameCallback, GameCellEnum, \
    DiceCallback, DiceParityEnum
from src.utils import TextBuilder, get_time_until_midnight
from src.utils.back_button_process import process_back

games_router = Router(name="Games router")


@games_router.message(Command(Games.KILLRU), IsChat(), CooldownFilter(Games.KILLRU, True))
async def killru_command(message: types.Message, db: Database, chat_user):
    russophobia = 0
    while russophobia == 0:
        russophobia = round(random.uniform(-500, 1500))

    current_time = message.date.timestamp()

    await db.cooldown.update_user_cooldown(message.chat.id, message.from_user.id, Games.KILLRU, current_time)
    await db.chat_user.add_user_russophobia(message.chat.id, message.from_user.id, russophobia)

    tb = TextBuilder(
        user=TextMention(message.from_user.first_name, user=message.from_user),
        ttp=Code(get_time_until_midnight(current_time)),
        new_russophobia=Code(chat_user[3] + russophobia),
        russophobia=Code(abs(russophobia))
    )
    if russophobia > 0:
        tb.add("📈 {user}, +{russophobia} кг")
    else:
        tb.add("📉 {user}, -{russophobia} кг")
    tb.add("\n\n👛 Баланс: {new_russophobia} кг\n⏰ Продовжуй через {ttp}", True)

    await message.answer(tb.render())


@games_router.callback_query(
    or_f(
        BetCallback.filter(F.action == BetButtonType.CANCEL),
        BaseGameCallback.filter(F.action == BaseGameEnum.CANCEL),
        GameCallback.filter(F.cell == GameCellEnum.CANCEL),
        DiceCallback.filter(F.parity == DiceParityEnum.CANCEL)),
    IsCurrentUser(True)
)
async def callback_cancel(callback: types.CallbackQuery, callback_data: BetCallback):
    await callback.bot.answer_callback_query(callback.id, "Хто прочитав той лох")
    await callback.message.edit_text(TextBuilder(f"⚠️ Лох злякався. "
                                                 f"{"{bet} " if callback_data.bet > 0 else ""}кг повернуто",
                                                 bet=callback_data.bet).render())


@games_router.callback_query(
    or_f(
        BaseGameCallback.filter(F.action == BaseGameEnum.BACK),
        GameCallback.filter(F.cell == GameCellEnum.BACK),
        DiceCallback.filter(F.parity == DiceParityEnum.BACK)),
    IsCurrentUser(True)
)
async def callback_cancel(callback: types.CallbackQuery, callback_data: BaseGameCallback, chat_user):
    await process_back(callback, callback_data, chat_user)
