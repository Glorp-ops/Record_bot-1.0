from aiogram.types import Message
from DataBase.model import Lesson,Registration_study,User,async_session
from sqlalchemy import *




# async def add_items() :
#      async with async_session() as curs:
#         category_game = Category(name = 'games')
#         category_product = Category(name = 'products')
#
#         items_game = Item(name = 'Zero Down',count = 3, price = 3500)
#         items_products = Item(name = 'Milk', count = 8, price = 100)
#
#         items_game.category = category_game
#         items_products.category = category_product
#         curs.add_all([items_game,items_products])
#         await curs.commit()



async def add_lesson():
    async with async_session() as curs:

        english = Lesson(name = 'Английский язык', datetime = 'Среда 12:30', time_lesson = '1 час')
        russian = Lesson(name = 'Русский язык', datetime = 'Вторник 15:00', time_lesson = '1 час')
        math = Lesson(name = 'Математика', datetime = 'Понедельник', time_lesson = '1 час 30 минут' )
        music = Lesson(name = 'Музыка', datetime = 'Суббота', time_lesson = '2 часа')
        art = Lesson(name = 'ИЗО', datetime = 'Четверг', time_lesson = '2 часа')

        curs.add_all([english,russian,math,music,art])

        await curs.commit()


        # if admin == None:
        #
        #     admin = User(username = username, name = name, tg_id = tg_id, role = 'admin')
        #     curs.add(admin)


# async def login_database(username,name ,tg_id):
#     async with async_session() as curs:
#         user_search = await curs.execute(select(User).where(User.username == username and User.tg_id == tg_id))
#         user = user_search.fetchone()
#         if user == None:
#             user_add = User(username = username, name = name, tg_id = tg_id, role = 'admin')
