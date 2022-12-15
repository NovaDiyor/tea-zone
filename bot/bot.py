import telebot
import requests
from telebot import types
base_url = "http://127.0.0.1:8000/api"
bot = telebot.TeleBot("5795595345:AAEztZmIRlwvD65WZaf2DvRtQY6LbEs8b6s")


markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
markup.add(types.KeyboardButton("Buyurtma berish"), types.KeyboardButton('Dastavka'), types.KeyboardButton('Biz haqimizda'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	try:
		text = requests.get(f'{base_url}/info/').json()
		bot.send_message(message.from_user.id, text['text'], reply_markup=markup)
	except Exception as err:
		print(err)
		bot.reply_to(message, "hush kelibsiz!", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "Biz haqimizda":
		query = requests.get(f'{base_url}/detail/').json()
		text = f"<b>Tea-Zone choyhonasi</b>\n{query['text']}\nTelefon nomer: <b>{query['phone']}</b>"
		bot.send_photo(message.from_user.id, "https://lh5.googleusercontent.com/p/AF1QipNs_TAMZGz_cYiNrRbxdHj7cWTqObR8RUvJxbBH=s435-k-no", text, parse_mode='HTML')
		bot.send_location(message.from_user.id, latitude=query['lat'], longitude=query['lng'], reply_markup=markup)
	elif message.text == "Buyurtma berish":
		query = requests.get(f'{base_url}/rooms/').json()
		room_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		buttons = []
		for i in query:
			buttons.append(types.KeyboardButton(f"{i['number']}"))
			if len(buttons) == 2:
				room_markup.add(buttons[0], buttons[1])
				buttons.clear()
		if len(buttons) == 1:
			room_markup.add(buttons[0])
			buttons.clear()
		room_markup.add(types.KeyboardButton("Ortga"))
		bot_message = bot.send_message(message.from_user.id, 'Hozirdagi bosh honalar Buyurtma berish uchun honani tanlang!', reply_markup=room_markup)
		bot.register_next_step_handler(bot_message, name_controller)
	else:
		bot.reply_to(message, message.text)


def name_controller(message):
	if message.text == "Ortga":
		send_welcome(message)
	else:
		room = message.text
		bot_message = bot.send_message(message.from_user.id, 'Ismingizni kiriting!', reply_markup=types.ReplyKeyboardRemove())
		bot.register_next_step_handler(bot_message, phone_controller, room)


def phone_controller(message, room):
	if message.text == "Ortga":
		send_welcome(message)
	else:
		try:
			name = message.text
			contact_button = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
			contact_button.add(types.KeyboardButton("Raqam jo'natish", request_contact=True))
			bot_message = bot.send_message(message.from_user.id, 'Raqamingizni yuboring!', reply_markup=contact_button)
			bot.register_next_step_handler(bot_message, order_controller, room, name)
		except Exception as err:
			print(err)


def order_controller(message, room, name):
	if message.text == "Ortga":
		send_welcome(message)
	elif 'contact' in message.content_type:
		phone = message.contact.phone_number
		print(room, name, phone)
		data = {
			"name": name,
			"room": room,
			"phone": phone,
		}
		query = requests.post(f'{base_url}/create-order/', data=data).json()
		print(query)
		if query['status'] == 200:
			bot.send_message(message.from_user.id, 'Buyurtmangiz muvofaqiyatli berildi!', reply_markup=markup)
		elif query['status'] == 500:
			bot.send_message(message.from_user.id, 'Buyurtmangiz berishdagi hatolik!', reply_markup=markup)
		else:
			bot.send_message(message.from_user.id, 'Hatolik!', reply_markup=markup)
	else:
		bot.send_message(message.from_user.id, 'Raqam Notogri!', reply_markup=markup)
		send_welcome(message)


bot.infinity_polling()
