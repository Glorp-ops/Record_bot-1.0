from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder, ReplyKeyboardMarkup,KeyboardButton
from aiogram import Bot, Dispatcher,F
import asyncio
dp = Dispatcher()

def register_keyboard():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text='Зарегестрироваться', callback_data='reg')
    keyboard.button(text='Войти', callback_data='login')
    return keyboard.as_markup()
def bad_register_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Попробовать еще раз', callback_data='reg')
    keyboard.button(text='Войти', callback_data='login')
    return keyboard.as_markup()