from typing import Dict, Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram import types
from aiogram.enums import ChatType

from src import Database


class RegisterChatMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message,
                       data: Dict[str, Any]
                       ):
        db: Database | None = data.get("db", None)
        if db is None:
            raise Exception("БД не знайдено")

        chat = await db.chat.get_chat(event.chat.id)
        if event.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP] and not chat:
            chat = await db.chat.add_chat(event.chat.id)
        data["chat"] = chat
        return await handler(event, data)


class RegisterUserMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message,
                       data: Dict[str, Any]
                       ):
        db: Database | None = data.get("db", None)
        if db is None:
            raise Exception("БД не знайдено")
        if not event.from_user:
            return await handler(event, data)

        # Ignore bot and channel messages
        if event.from_user.is_bot:
            return

        user = await db.user.get_user(event.from_user.id)
        if not user:
            user = await db.user.add_user(event.from_user.id, event.from_user.username)
            await event.reply(f"👋 {event.from_user.mention_markdown()}, вітаю\\. Підтримка: @k0k0sbot")

        data["user"] = user

        if isinstance(event, types.CallbackQuery):
            message = event.message
        else:
            message = event

        if message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            return await handler(event, data)

        chat_user = await db.chat_user.get_chat_user(message.chat.id, event.from_user.id)
        if not chat_user:
            chat_user_row_id = (await db.chat_user.add_chat_user(message.chat.id, event.from_user.id))[0]
            chat_user = await db.chat_user.get_by_id(chat_user_row_id)
            await db.cooldown.add_user_cooldown(message.chat.id, event.from_user.id)
        data["chat_user"] = chat_user

        return await handler(event, data)
