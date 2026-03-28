# words = [
#     "дом", "окно", "дерево", "река", "гора", "море", "книга", "стол", "стул", "школа",
#     "учитель", "ученик", "город", "улица", "машина", "поезд", "самолет", "корабль", "солнце", "луна",
#     "звезда", "небо", "земля", "вода", "огонь", "воздух", "камень", "песок", "лес", "поле",
#     "цветок", "трава", "лист", "корень", "ветер", "дождь", "снег", "буря", "туман", "облако",
#     "друг", "семья", "ребенок", "мать", "отец", "брат", "сестра", "человек", "народ", "страна",
#     "язык", "слово", "мысль", "идея", "работа", "день", "ночь", "утро", "вечер", "время",
#     "год", "месяц", "неделя", "час", "минута", "секунда", "жизнь", "смерть", "любовь", "счастье",
#     "радость", "грусть", "смех", "слеза", "сила", "энергия", "движение", "покой", "игра", "музыка",
#     "картина", "фильм", "театр", "песня", "голос", "звук", "свет", "тень", "форма", "цвет",
#     "вопрос", "ответ", "путь", "дорога", "цель", "мечта", "память", "знание", "опыт", "успех"
#     ]
# KNB = ['Камень','Ножницы','Бумага']
# GN = ['1','2','3','4','5','6','7','8','9','10']
# greetings = [
#         "С 8 марта! Пусть каждый день будет наполнен радостью и улыбками!",
#         "Поздравляю с Международным женским днем! Желаю счастья и вдохновения!",
#         "С праздником весны! Пусть каждый момент приносит тепло и свет!",
#         "С 8 марта! Желаю любви, гармонии и исполнения самых заветных желаний!",
#         "Поздравляю с 8 марта! Пусть жизнь будет яркой, как весенние цветы!"
#     ]
# picture = ['image/h.jpeg','image/images.jpeg','image/mart.jpeg','image/q.jpeg','image/w.jpeg']
# @rt.message(Command('chop'))
# async def cmd_shop(message:Message):
#
#     async with async_session() as curs:
#         lessons = await curs.execute(select(Lesson.name))
#         result = lessons.scalars()
#     await message.answer(' Нажми на кнопки, чтобы сделать заказ',reply_markup=buttons_bd(result))
#
# @rt.callback_query(F.data == 'mart')
# async def callback_mart(callback: CallbackQuery):
#         photo_mart = FSInputFile(random.choice(picture))
#         await callback.message.answer_photo(photo=photo_mart,caption= random.choice(greetings))
#         await callback.answer('')
#
# @rt.callback_query(F.data == 'heart')
# async def callback_heart(callback: CallbackQuery):
#
#         await callback.message.answer('❤️')
#         await callback.answer('')
#
# @rt.callback_query(F.data == 'bucket')
#
# async def callback_bucket(callback: CallbackQuery):
#
#         await callback.message.answer('💐')
#         await callback.answer('')
#
# @rt.callback_query(F.data == 'mua')
#
# async def callback_mua(callback: CallbackQuery):
#
#         await callback.answer()
#         await callback.message.answer('💋')
#         chmok = FSInputFile('../audio/zvuk-poceluya.mp3')
#         await callback.message.answer_audio(chmok)
#
#
#
# @rt.callback_query(F.data == 'img')
#
# async def callback_img(callback: CallbackQuery):
#
#         photo = FSInputFile('../image/photo_2026-03-07_12-51-00.jpg')
#         await callback.message.answer_photo(photo=photo, caption='Вот картинка')
#
#         await callback.answer()
# @rt.callback_query(F.data == 'stick')
# async def callback_img(callback: CallbackQuery):
#
#         await callback.message.answer_sticker('CAACAgIAAxkBAAEQsmNpq_nFKmown8ebj4eEFVIcd2PSdAACUVUAArOwCUjur7FplqoxVzoE')
#         await callback.answer()
#
# @rt.callback_query(F.data == 'КНБ')
# async def game_state(callbacke: CallbackQuery,state: FSMContext):
#
#         await state.set_state(Game.gameKNB)
#         await callbacke.message.answer('Давай начнем!',reply_markup=buttons_playKNB())
#         await callbacke.answer('')
#
#
#
# @rt.message(Game.gameKNB)
# async def command_gameKNB_handler(message: Message, state: FSMContext) -> None:
#
#         if (message.text != '/end' and message.text != '/start'):
#
#             text = random.choice(KNB)
#             await message.answer(text)
#             if message.text == text:
#
#                         await message.answer('Ничья')
#
#             if (message.text == 'Камень' and text == 'Ножницы') or (message.text == 'Бумага' and text == 'Камень') or (message.text == 'Ножницы' and text == 'Бумага'):
#
#                         await message.answer('Ты выиграл')
#
#             if (message.text == 'Ножницы' and text  == 'Камень') or (message.text == 'Камень' and text == 'Бумага') or (message.text == 'Бумага' and text == 'Ножницы'):
#
#                         await message.answer('Ты проиграл')
#
#
#
#
#
# @rt.callback_query(F.data == 'GN')
#
# async def command_GN_FSM(callback: CallbackQuery,state: FSMContext ) -> None:
#         global number
#
#         await state.clear()
#         number = random.randint(1, 10)
#         await callback.message.answer('Я загадал',reply_markup=buttons_playGN())
#
#         await callback.answer('')
#
#         await state.set_state(Secrets.score)
#
# @rt.message(Secrets.score)
# async def command_GN_handler(message: Message, state: FSMContext):
#         global number
#
#
#
#         print(number)
#
#         if (str(number) == message.text and message.text != 'Игра угадай число') and ( message.text != '/end' and message.text != '/start'):
#
#
#
#             number = random.randint(1,10)
#
#             # score = await state.get_data()
#             # await message.answer(f'Вы потратили {score['score']} ')
#
#             await message.answer('Вы выиграли! Я еще раз загадал!')
#
#         else :
#             if (message.text != '/end' and message.text != '/start'):
#                 if int(number) > int(message.text):
#                     # await state.update_data(score= 0 + 1)
#                     await message.answer('Больше')
#
#                 if int(number) < int(message.text):
#                     # await state.update_data(score=0 + 1)
#                     await message.answer('Меньше')
#
#
# @rt.callback_query(F.data == 'W')
# async def command_gameW_handler(callback: CallbackQuery, state: FSMContext) -> None:
#         global word
#
#         await state.clear()
#
#         word = random.choice(words)
#
#         await callback.message.answer('Давай начнем!',reply_markup =  buttons_playW3())
#         await callback.answer('')
#         await state.set_state(Secrets.score_W)
#
# @rt.message(Secrets.score_W)
# async def command_playW_handler(message:Message,state: FSMContext) -> None:
#         global word
#         flag = False
#         print(word)
#
#
#         if (message.text != '/end' and message.text != '/start'):
#
#             if message.text == word:
#
#
#
#                     await message.answer('Правильно!')
#                     flag = True
#
#                     await message.answer('Давай еще раз!',reply_markup = buttons_playW3())
#                     word = random.choice(words)
#
#             if message.text == 'Подсказка 1':
#                     await message.answer(f'Первая буква: {word[0]}', reply_markup= buttons_playW2())
#                     # await state.update_data(score_W=1)
#
#             if message.text == 'Подсказка 2':
#                     await message.answer(f'Вторая буква: {word[1]}', reply_markup = buttons_playW1())
#                     # await state.update_data(score_W=2)
#             if message.text == 'Подсказка 3':
#                     await message.answer(f'Третья буква {word[2]}', reply_markup=ReplyKeyboardRemove())
#                     # await state.update_data(score_W=3)
#
#             if (message.text != word and message.text.capitalize() != 'Подсказка 1') and (message.text.capitalize() != 'Подсказка 2') and (message.text.capitalize()!= 'Подсказка 3' and message.text != 'Игра угадай слово') and (flag == False):
#                     await message.answer('Попробуй еще раз!')
#
# @rt.message(Command('reg'))
# async def reg_one(message: Message, state: FSMContext):
#         await state.set_state(Reg.name)
#         await message.answer('Введите имя: ')
#
# @rt.message(Reg.name)
# async def reg_two( message: Message, state: FSMContext):
#         await state.update_data(name=message.text)
#         await state.set_state(Reg.number)
#         await message.answer('Нажмите',reply_markup=in_butt_contact())
# @rt.callback_query(F.data == 'Number')
# async def button_contact(callback: CallbackQuery):
#
#         await callback.answer('',shipping_options=True)
#
# @rt.message(Reg.number)
# async def reg_three(message: Message, state: FSMContext):
#
#
#         await state.update_data(name = message.contact.phone_number)
#         data = await state.get_data()
#         await message.answer(f'Спасибо, вы прошли регестрацию')

# @rt.message(Command('end'))
# async def end_game(message: Message, state: FSMContext):
#         await state.clear()
#         await message.answer('Давай еще поиграем!', reply_markup=buttons_game())

# def buttons_reg():
#     keyboard_game = InlineKeyboardBuilder()
#
#     keyboard_game.button(text = 'Игра в КНБ', callback_data = 'КНБ')
#     # keyboard_game.button(text = 'Игра угадай слово', callback_data = 'W')
#     # keyboard_game.button(text = 'Игра угадай число', callback_data = 'GN')
#     # keyboard_game.button(text = 'Картинка(красивая)', callback_data='img')
#     # keyboard_game.button(text = 'Стики',callback_data='stick')
#     # keyboard_game.button(text = 'Могут нажать только девушки(и Дадик)', callback_data='mart')
#     # keyboard_game.button(text='Сердечко', callback_data='heart')
#     # keyboard_game.button(text='Букет', callback_data='bucket')
#     # keyboard_game.button(text='Поцелуй', callback_data='mua')
#
#     keyboard_game.adjust(1, 1, 1, 1, 1, 1 , 3 )
#
#     return keyboard_game.as_markup()
#
#
# def buttons_playKNB():
#
#
#             keyboard = ReplyKeyboardBuilder()
#
#             keyboard.button(text = 'Ножницы')
#             keyboard.button(text = 'Бумага')
#             keyboard.button(text = 'Камень')
#
#             keyboard.adjust(1,1,1,)
#
#             return keyboard.as_markup(resize_keyboard = True)
#
# def buttons_playGN():
#     keyboard_GN = ReplyKeyboardBuilder()
#
#     keyboard_GN.button(text='1')
#     keyboard_GN.button(text='2')
#     keyboard_GN.button(text='3')
#     keyboard_GN.button(text='4')
#     keyboard_GN.button(text='5')
#     keyboard_GN.button(text='6')
#     keyboard_GN.button(text='7')
#     keyboard_GN.button(text='8')
#     keyboard_GN.button(text='9')
#     keyboard_GN.button(text='10')
#
#     keyboard_GN.adjust(5)
#
#     return keyboard_GN.as_markup(resize_keyboard=True)
#
#
# # def buttons_playW1():
#     # keyboardW = ReplyKeyboardBuilder()
#     #
#     # keyboardW.button(text='Подсказка 1')
#     # keyboardW.button(text='Подсказка 2')
#     # keyboardW.button(text='Подсказка 3')
#     #
#     # keyboardW.adjust(1, 1, 1, )
#     #
#     # return keyboardW.as_markup(resize_keyboard=True)
#
# # def buttons_playW2():
# #     keyboardW = ReplyKeyboardBuilder()
# #
# #     keyboardW.button(text='Подсказка 2')
# #     keyboardW.button(text='Подсказка 3')
# #
# #     keyboardW.adjust(1, 1, 1, )
# #
# #     return keyboardW.as_markup(resize_keyboard=True)
#
# def buttons_playW1():
#     keyboardW = ReplyKeyboardBuilder()
#
#     keyboardW.button(text='Подсказка 3')
#
#     keyboardW.adjust(1, 1, 1, )
#
#     return keyboardW.as_markup(resize_keyboard=True)
#
# def buttons_playW2():
#     keyboardW = ReplyKeyboardBuilder()
#
#     keyboardW.button(text='Подсказка 2')
#
#     keyboardW.adjust(1, 1, 1, )
#
#     return keyboardW.as_markup(resize_keyboard=True)
#
# def buttons_playW3():
#     keyboardW = ReplyKeyboardBuilder()
#
#     keyboardW.button(text='Подсказка 1')
#
#     keyboardW.adjust(1, 1, 1, )
#
#     return keyboardW.as_markup(resize_keyboard=True)
#
# # def buttons_playW6():
# #     keyboardW = ReplyKeyboardBuilder()
# #
# #     keyboardW.button(text='Подсказка 1')
# #     keyboardW.button(text='Подсказка 3')
# #
# #     keyboardW.adjust(1, 1, 1, )
# #
# #     return keyboardW.as_markup(resize_keyboard=True)
# # def buttons_playW7():
# #     keyboardW = ReplyKeyboardBuilder()
# #
# #     keyboardW.button(text='Подсказка 1')
# #     keyboardW.button(text='Подсказка 2')
# #
# #     keyboardW.adjust(1, 1, 1, )
# #
# #     return keyboardW.as_markup(resize_keyboard=True)
# def buttons_img():
#     img_keyboard = InlineKeyboardBuilder()
#
#     img_keyboard.button(text = 'Картинка(красивая)', callback_data='img')
#
#     return  img_keyboard.as_markup()
# def buttons_bd(massiv) -> ReplyKeyboardMarkup:
#     buttons_bd = [KeyboardButton(text=item) for item in massiv]
#     return ReplyKeyboardMarkup(keyboard=[buttons_bd],resize_keyboard=True)