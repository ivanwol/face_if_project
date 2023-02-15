import telebot
from telebot import TeleBot

bot: TeleBot = telebot.TeleBot("6080146941:AAGHOsJu0QMvFnxaKRqk5YoIb-fy7Iu9hSE")


@bot.message_handler(commands=["change_photo"])
def start(message):
    bot.send_message(message.chat.id, 'Ок. Пратете ми своята снимка')


@bot.message_handler(content_types=['text'])
def get_second_result(message):
    if message.text == 'д':
        second_result = True
        print("Second Result: ", second_result)


@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = '.\photos\photo.png'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Снимката е добавена")




bot.polling(none_stop=True)
