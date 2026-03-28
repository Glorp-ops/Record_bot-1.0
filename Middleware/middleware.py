from aiogram import BaseMiddleware
from aiogram.filters.callback_data import CallbackQueryFilter
from aiogram.handlers import CallbackQueryHandler
from aiogram.types import TelegramObject,Message,CallbackQuery
from typing import Callable,Any,Dict,Awaitable

class LoggerMiddlewareMessage(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject,Dict[str,Any]],Awaitable[Any]],
                       event: Message,
                       data: Dict[str,Any]) -> Any:
        print('пришло сообщение')
        result = await handler(event,data)
        print('Действие после')
        return result

class LoggerMiddlewareCallback(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject,Dict[str,Any]],Awaitable[Any]],
                       event: CallbackQuery,
                       data: Dict[str,Any]) -> Any:

        print('вызван колбэк')
        result = await handler(event,data)
        print('Действие после')
        return result




