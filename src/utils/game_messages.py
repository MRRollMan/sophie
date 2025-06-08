from aiogram.utils.formatting import TextMention, Code
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.types import Games
from src.utils import TextBuilder, get_bet_buttons


def get_basketball_message(chat_user, from_user):
    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, Games.BASKETBALL, chat_user[3])
    tb.add("🏀 {user} якщо не виграєш трахну твою маму\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))

    return tb, kb


def get_bowling_message(chat_user, from_user):
    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, Games.BOWLING, chat_user[3])
    tb.add("🎳 {user} а тебе випадково в дитинстві не кидали?\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))

    return tb, kb


def get_casino_message(chat_user, from_user):
    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, Games.CASINO, chat_user[3])
    tb.add("🎰 {user} шо ти, лудоман спідозний\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))

    return tb, kb


def get_darts_message(chat_user, from_user):
    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, Games.DARTS, chat_user[3])
    tb.add("🎯 {user}сідай на пляшку\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))

    return tb, kb


def get_dice_message(chat_user, from_user):
    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, Games.DICE, chat_user[3])
    tb.add("🎲 {user}, якщо програєш,\nто заплатиш адміну через /shop\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))

    return tb, kb


def get_football_message(chat_user, from_user):
    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, Games.FOOTBALL, chat_user[3])
    tb.add("⚽ {user} я знав що ти гей\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))

    return tb, kb


def get_game_message(chat_user, from_user):
    tb, kb = TextBuilder(), get_bet_buttons(from_user.id, Games.GAME, chat_user[3])
    tb.add("🧟‍♂️ {user} бля дивлюся на тебе і ригати хочеться\nВибери ставку\n\n🏷️ У тебе: {balance} кг\n",
           user=TextMention(from_user.first_name, user=from_user),
           balance=Code(chat_user[3]))

    return tb, kb
