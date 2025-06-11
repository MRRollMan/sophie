from datetime import datetime, timedelta

from aiogram import types
from aiogram.enums import ChatType, ParseMode
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.utils.formatting import Code

from src import config
from src.database import Database
from src.types import Games, Actions, BetCallback, BaseGameCallback
from src.utils import TextBuilder, get_time_until_midnight, get_time_until


class CooldownFilter(BaseFilter):
    def __init__(self, cooldown_type: str | Games | Actions, send_answer: bool = False):
        self.is_game = isinstance(cooldown_type, Games)
        self.cooldown_type = str(cooldown_type)
        self.send_answer = send_answer

    # refactor it, please
    async def __call__(self, message: Message, db: Database):
        callback = False
        if config.TEST:
            return True
        if isinstance(message, types.CallbackQuery):
            callback = True
            user_id = message.from_user.id
            message = message.message
        else:
            user_id = message.from_user.id

        cooldown = await db.cooldown.get_user_cooldown(message.chat.id, user_id, self.cooldown_type)
        if cooldown is None or cooldown[0] == 0:
            return True
        last_game_date = datetime.fromtimestamp(cooldown[0])
        message_date = datetime.fromtimestamp(message.date.timestamp())

        if self.cooldown_type == Actions.GIVE:
            result = last_game_date.date() < message_date.date()
            next_time = get_time_until_midnight(message.date.timestamp())
        else:
            delta = 12 if self.cooldown_type == Games.KILLRU else 3
            next_play = last_game_date + timedelta(hours=delta)
            result = next_play < message_date
            next_time = get_time_until(message.date.timestamp(), next_play.timestamp())

        if not result and self.send_answer:
            text = "⏰ У тебе шо альцгеймер? Спробуй через {ttp}" \
                if self.is_game \
                else "⏰ Єблан, в тебе кулдаун. Спробуй через {ttp}"
            text = TextBuilder(text, ttp=Code(next_time))
            if callback:
                await message.edit_text(text.render(ParseMode.MARKDOWN_V2))
            else:
                await message.reply(text.render(ParseMode.MARKDOWN_V2))
        return result


class BetFilter(BaseFilter):
    async def __call__(self, callback: types.CallbackQuery, callback_data: BetCallback | BaseGameCallback, db: Database):
        chat_user = await db.chat_user.get_chat_user(callback.message.chat.id, callback.from_user.id)
        if callback_data.bet > chat_user[3]:
            await callback.message.edit_text(TextBuilder("🫵😂 Пішов нахуй, бомж. Зароби спочатку русофобію").render())
            return False
        return True


class GamesFilter(BaseFilter):
    async def __call__(self, message: Message, db: Database):
        chat = await db.chat.get_chat(message.chat.id)
        return bool(chat[1])


class GiveFilter(BaseFilter):
    async def __call__(self, message: Message, db: Database):
        chat = await db.chat.get_chat(message.chat.id)
        return bool(chat[2])


class IsChat(BaseFilter):
    async def __call__(self, message: Message):
        return message.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        return message.from_user.id in config.ADMIN


class IsSupport(BaseFilter):
    async def __call__(self, message: Message):
        return message.from_user.id in config.SUPPORT


class IsChatAdmin(BaseFilter):
    async def __call__(self, message: Message):
        if isinstance(message, types.CallbackQuery):
            chat = message.message.chat
        else:
            chat = message.chat
        chat = await message.bot.get_chat_member(chat.id, message.from_user.id)
        return chat.status in ["administrator", "creator"]


class IsCurrentUser(BaseFilter):
    def __init__(self, send_callback: bool = False):
        self.send_callback = send_callback

    async def __call__(self, callback: types.CallbackQuery, callback_data):
        result = callback.from_user.id == callback_data.user_id
        if not result and self.send_callback:
            await callback.bot.answer_callback_query(callback.id, "🖕😂 Ці кнопочки не для тебе",
                                                     show_alert=True)
        return result
