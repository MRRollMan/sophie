from aiogram import types

from src.types import Games, BaseGameCallback, GameCallback, DiceCallback
from src.utils.game_messages import get_message


async def process_back(
        callback: types.CallbackQuery, callback_data: BaseGameCallback, chat_user,
) -> None:
    user = callback.from_user

    if isinstance(callback_data, GameCallback):
        game = Games.GAME
    elif isinstance(callback_data, DiceCallback):
        game = Games.DICE
    else:
        game = callback_data.game
    tb, kb = get_message(chat_user, user, game)

    await callback.message.edit_text(text=tb.render(), reply_markup=kb)
