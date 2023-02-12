import time
import cv2
import face_recognition
import requests
import telebot
from telebot import TeleBot



token = "6080146941:AAGHOsJu0QMvFnxaKRqk5YoIb-fy7Iu9hSE"
id = '1445931397'
bot: TeleBot = telebot.TeleBot(token)
faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)



@bot.message_handler(content_types=['text'])
def get_second_result(message):
    if message.text == 'д':
        second_result = True

try:
    img2 = cv2.imread("photos/Messi1.png")
    img_encoding2 = face_recognition.face_encodings(img2)[0]
except IndexError:
    print('Лицето на снимката не е разпознато')
    exit()



while True:
    try:
        success, img = cap.read()
        img_encoding = face_recognition.face_encodings(img)[0]
        faces = faceCascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50))
        result = face_recognition.compare_faces([img_encoding], img_encoding2)
        if result[0] == False:
            print("Result: ", result[0])
        elif result[0] == True:
            print("Result: ", result[0])
            requests.get('https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' +
                         id + '&text=' + f'Някой опитва се да отвори врата. Вие ли сте?(д/н)')
            @bot.message_handler(content_types=['text'])
            def get_second_result(message):
                if message.text == 'д':
                    print("Result: ", result[0])
                    time.sleep(20)








    except IndexError:
        time.sleep(2)




bot.polling(none_stop=True)