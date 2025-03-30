import telebot
from telebot import types
from weather import weather_finder, find_city

bot = telebot.TeleBot("7914071941:AAFIbKc4SNmmdFn-UBLd3bpIA3HlOuzpA68")
user_states = {}


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        f"Hello {message.from_user.first_name}, my name is {bot.get_me().first_name}",
    )
    main(message)


def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Weather")
    btn2 = types.KeyboardButton("Library")
    btn3 = types.KeyboardButton("Coming soon...")
    markup.add(btn1, btn2).row(btn3)

    bot.send_message(
        message.chat.id, "Choose the following option:", reply_markup=markup
    )


@bot.message_handler(content_types=["text"])
def activity(message):
    if message.text == "Weather":
        user_states["user_id"] = "waiting_for_city"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn = types.KeyboardButton("Quit to menu")
        btn2 = types.KeyboardButton(text="Send location", request_location=True)
        bot.reply_to(message, "Send me name of the city or your geolocation.", reply_markup=markup.add(btn2).row(btn))

    elif message.text == "Quit to menu":
        if "user_id" in user_states:
            del user_states["user_id"]
        main(message)

    elif message.text == "Library":
        bot.reply_to(message, "In progress")

    elif "user_id" in user_states and user_states["user_id"] == "waiting_for_city":
        bot.reply_to(message, weather_finder(message.text))


@bot.message_handler(content_types=["location"])
def location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    city_name = find_city(lat, lon)
    if message.location is not None and user_states["user_id"] == "waiting_for_city":
        bot.reply_to(message, weather_finder(city_name))


bot.infinity_polling()

