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
        return tb.add("Пішов нахуй бомжара. Зароби спочатку русофобію"), None

    if game in game_messages:
        return game_messages[game](chat_user, from_user, tb), kb.as_markup()
    else:
        raise ValueError(f"Unsupported game type: {game}")


def get_basketball_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🏀 {user} якщо не виграєш трахну твою маму\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_bowling_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎳 {user} а тебе випадково в дитинстві не кидали?\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_casino_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎰 {user} шо ти, лудоман спідозний\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_darts_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎯 {user}сідай на пляшку\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_dice_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🎲 {user}, якщо програєш,\nто заплатиш адміну через /shop\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_football_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("⚽ {user} я знав що ти гей\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb


def get_game_message(chat_user, from_user, tb) -> TextBuilder:
    tb.add("🧟‍♂️ {user} бля дивлюся на тебе і ригати хочеться\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))
    return tb
