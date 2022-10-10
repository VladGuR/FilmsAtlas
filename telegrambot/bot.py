import config
import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
# from sqlighter import SQLighter


# from stopgame import StopGame

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# инициализируем соединение с БД
# db = SQLighter('db.db')
# инициализируем парсер
# sg = StopGame('lastkey.txt')

# # Команда активации подписки
# @dp.message_handler(commands=['subscribe'])
# async def subscribe(message: types.Message):
# 	if(not db.subscriber_exists(message.from_user.id)):
# 		# если юзера нет в базе, добавляем его
# 		db.add_subscriber(message.from_user.id)
# 	else:
# 		# если он уже есть, то просто обновляем ему статус подписки
# 		db.update_subscription(message.from_user.id, True)
#
# 	await message.answer("Вы успешно подписались на рассылку!\nЖдите, скоро выйдут новые обзоры и вы узнаете о них первыми =)")
#
# # Команда отписки
# @dp.message_handler(commands=['unsubscribe'])
# async def unsubscribe(message: types.Message):
# 	if(not db.subscriber_exists(message.from_user.id)):
# 		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
# 		db.add_subscriber(message.from_user.id, False)
# 		await message.answer("Вы итак не подписаны.")
# 	else:
# 		# если он уже есть, то просто обновляем ему статус подписки
# 		db.update_subscription(message.from_user.id, False)
# 		await message.answer("Вы успешно отписаны от рассылки.")
def scheduled(wait_for):
	bot.send_game(917276720, 'dsfe')
scheduled(10)

@dp.message_handler()
async def check_cat(message: types.Message):
	keybutton = types.ReplyKeyboardMarkup()
	button_1 = 'кнопка 1'
	keybutton.add(button_1)
	button_2 = '2 ryjgrf'
	keybutton.add(button_2)
	await message.answer(f'{message.text} |\n {message.from_user} |\n {message.date} |\n {message.chat} |\n ', reply_markup=keybutton)
	# await message.reply("qwe")



@dp.message_handler(regexp='Привет')
async def check_message(message: types.Message):
	await message.answer("Привет")


@dp.message_handler(regexp='Смотреть категории')
async def check_cat(message: types.Message):
	mebel = m.categories_list()
	cat = [f" - {obj.get('name')} \n - {obj.get('href')} \n" for obj in mebel]
	await message.answer(f"Смотреть категории: \n{''.join(cat)}\n")
	@dp.message_handler()
	async def check_cat(message: types.Message):
		print(message.text)
		categories = m.categories_list()
		for obj in categories:
			print(message.text, " == ", str(obj.get('name')))
			if message.text == str(obj.get('name')):
				print(message.text, " =\= ", str(obj.get('name')))
				mebel_list = m.categori_product(obj.get('href'))
				print(mebel_list)
				for object in mebel_list:
					print('8')
					await message.answer(f"Наименование: {object.get('name')} \nЦенна: {object.get('price')}\n{object.get('href')}")

		# mebel = m.categories_list()
		# print(obj.get('href') for obj in mebel)
		# mebel = m.categori_product(obj.get('href') for obj in mebel)
		# print(mebel)
		# await message.answer(f"Смотреть ghjlerns: \n{mebel}\n")
		# await message.answer("hi")


# проверяем наличие новых игр и делаем рассылки
# async def scheduled(wait_for):
# 	while True:
# 		await asyncio.sleep(wait_for)
# 		subscriptions = db.get_subscriptions()
# 		for s in subscriptions:
# 			await bot.send_photo(s[1], caption = 'Gghbdtn' , disable_notification = True)
		# # проверяем наличие новых игр
		# new_games = sg.new_games()

		# if(new_games):
		# 	# если игры есть, переворачиваем список и итерируем
		# 	new_games.reverse()
		# 	for ng in new_games:
		# 		# парсим инфу о новой игре
		# 		nfo = sg.game_info(ng)
		#
		# 		# получаем список подписчиков бота
		# 		subscriptions = db.get_subscriptions()
		#
		# 		# отправляем всем новость
		# 		with open(sg.download_image(nfo['image']), 'rb') as photo:
		# 			for s in subscriptions:
		# 				await bot.send_photo(
		# 					s[1],
		# 					photo,
		# 					caption = nfo['title'] + "\n" + "Оценка: " + nfo['score'] + "\n" + nfo['excerpt'] + "\n\n" + nfo['link'],
		# 					disable_notification = True
		# 				)
		#
		# 		# обновляем ключ
		# 		sg.update_lastkey(nfo['id'])


# запускаем лонг поллинг
if __name__ == '__main__':
	# dp.loop.create_task(scheduled(100))
	# dp.loop.create_task(scheduled(10)) # пока что оставим 10 секунд (в качестве теста)
	executor.start_polling(dp, skip_updates=True)

