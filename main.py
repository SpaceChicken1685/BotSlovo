# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# В google colab добавить: !pip install Faker
# 'PyTelegramBotApi'


import telebot

# Создаем экземпляр бота с вашим токеном
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Словарь терминов, используемых тестировщиками
dictionary = {
    
}

# Функция для начала работы с ботом
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я словарь тестировщика. Напиши термин, и я дам его определение.")

# Функция для обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def get_definition(message):
    word = message.text.lower()  # Приводим к нижнему регистру для стандартизации
    definition = dictionary.get(word)

    if definition:
        bot.reply_to(message, f"{word.capitalize()}: {definition}")
    else:
        bot.reply_to(message, f"Извините, я не знаю определения термина '{word}'.")

# Запуск бота
if __name__ == '__main__':
    bot.polling(
