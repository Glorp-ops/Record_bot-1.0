from DataBase.model import User, async_session
from sqlalchemy import *

from Middleware.middleware import LoggerMiddlewareMessage,LoggerMiddlewareCallback
from State.state import  Reg
from KeyBoards import register_keyboard, bad_register_keyboard
from aiogram import F,Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

# import database.requests as rq

TOKEN = '8308422383:AAFxUe1sTxe66yz1cJ4qefu3dpKqqwF3eMk'


rt = Router()

rt.message.middleware(LoggerMiddlewareMessage())
rt.callback_query.middleware(LoggerMiddlewareCallback())




#

    # Command handler
@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
        await message.answer("Я тг бот для записи на занятия \n"
                             "Зарегестрируете или войдите в аккаунт", reply_markup=register_keyboard())





@rt.callback_query(F.data == 'reg')
async def reg_name(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg.name)
    await callback.answer()

    await callback.message.answer('Введите имя')




@rt.message(Reg.name)

async def name(message: Message, state: FSMContext):
    async with async_session() as curs:
        check_tg_id = await curs.execute(select(User).where(User.tg_id == message.from_user.id))

        tg_id_user  = check_tg_id.fetchone()
        await state.update_data(name=message.text)
        name = await state.get_data()
        print(tg_id_user)
        if tg_id_user == None and message.from_user.id != 1822405102:

            user = User(username = message.from_user.username, name =name['name'], tg_id = message.from_user.id, role = 'user')
            curs.add(user)


            await message.answer('Спасибо за регестрацию')
        if tg_id_user != None:
            await message.answer('О, так у вас есть аккаунт! Пожалуйста войдите!', reply_markup=bad_register_keyboard())

@rt.message(F.text,StateFilter(None))
async def command_text_handler(message: Message) -> None:
        await message.answer('Нажмите на кнопку, чтобы начать игру')
