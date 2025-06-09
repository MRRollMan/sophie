from aiogram import types
from src.utils.game_messages import get_bowling_message, get_basketball_message, get_casino_message, \
    get_darts_message, get_dice_message, get_football_message, get_game_message
from src.types import Games, BaseGameCallback, GameCallback, DiceCallback


async def process_back(
        callback: types.CallbackQuery, callback_data: BaseGameCallback, chat_user,
) -> None:
    balance = chat_user[3]
    user = callback.from_user

    if isinstance(callback_data, GameCallback):
        func = get_game_message
    elif isinstance(callback_data, DiceCallback):
        func = get_dice_message
    else:
        match callback_data.game:
            case Games.BASKETBALL:
                func = get_basketball_message
            case Games.BOWLING:
                func = get_bowling_message
            case Games.CASINO:
                func = get_casino_message
            case Games.DARTS:
                func = get_darts_message
            case Games.FOOTBALL:
                func = get_football_message
            case _:
                await callback.answer("Ця гра не підтримується")
                return

    tb, kb = func(chat_user, user)
    await callback.message.edit_text(text=tb.render(), reply_markup=kb.as_markup())