from typing import Callable

from aiogram.types import InlineKeyboardMarkup, User
from aiogram.utils.formatting import TextMention, Code

from src.types import Games
from src.utils import TextBuilder, get_bet_buttons


def get_message(chat_user, from_user, game: Games) -> tuple[TextBuilder, InlineKeyboardMarkup | None]:
    game_messages: dict[str, Callable[[tuple, User, TextBuilder], TextBuilder]] = {
        Games.BASKETBALL: get_basketball_message,
        Games.BOWLING: get_bowling_message,
        Games.CASINO: get_casino_message,
        Games.DARTS: get_darts_message,
        Games.DICE: get_dice_message,
        Games.FOOTBALL: get_football_message,
        Games.GAME: get_game_message
    }

    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, game, chat_user[3])

    if chat_user[3] <= 0:
        return tb.add("🫵😂 Пішов нахуй, бомж. Зароби спочатку русофобію"), None

    if game in game_messages:
        return game_messages[game](chat_user, from_user, tb), kb.as_markup()
    else:
        raise ValueError(f"Непідтримуваний тип гри: {game}")


def get_basketball_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🏀 Баскетбол. Влуч м'ячем в кільце\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_bowling_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎳 Боулінг. Вибий всі кеглі\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_casino_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎰 Казіно. Постарайся вибити 777\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_darts_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎯Дартс. Влуч у центр\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_dice_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎲 Кістки. Вгадай парне чи непарне\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_football_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("⚽ Футбол. Влуч у ворота\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_game_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🧌 Вбий кацапа. Якщо вгадаєш де кацап, вб'єш його та отримаєш винагороду\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb
