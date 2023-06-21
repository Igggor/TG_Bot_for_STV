from telebot import types
from globs import BOT_TOKEN, CHAT_ID, WEB_APP_LINK
import telebot, time, math

tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))

mess = []
vid = []

bot = telebot.TeleBot(BOT_TOKEN)

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
   global WEB_APP_LINK
   webAppTest = types.WebAppInfo(WEB_APP_LINK) #создаем webappinfo - формат хранения url
   one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard #возвращаем клавиатуру

def webAppKeyboardInline(): #создание inline-клавиатуры с webapp кнопкой
   keyboard = types.InlineKeyboardMarkup(row_width=1) #создаем клавиатуру inline
   global WEB_APP_LINK
   webApp = types.WebAppInfo(WEB_APP_LINK) #создаем webappinfo - формат хранения url
   one = types.InlineKeyboardButton(text="Веб приложение", web_app=webApp) #создаем кнопку типа webapp
   keyboard.add(one) #добавляем кнопку в клавиатуру

   return keyboard #возвращаем клавиатуру


def create_button(text):
   keyboard = types.ReplyKeyboardMarkup(row_width=1)  # создаем клавиатуру
   one_butt = types.KeyboardButton(text=text)  # создаем кнопку типа webapp
   keyboard.add(one_butt)  # добавляем кнопки в клавиатуру
   return keyboard

@bot.message_handler(commands=['start']) #обрабатываем команду старт
def start_fun(message):
   bot.send_message( message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)\nЗапустить тестовые страницы можно нажав на кнопку снизу или кнопку меню.', parse_mode="Markdown", reply_markup=webAppKeyboard()) #отправляем сообщение с нужной клавиатурой


@bot.message_handler(content_types="text")
def new_mes(message):
   if message.text == "Отправить фото":
      global mess
      while(len(mess) != 0):
         group = []
         for i in range(min(len(mess), 10)):
            el = mess[0]
            group.append(types.InputMediaPhoto(el.photo[0].file_id))
            del mess[0]
         bot.send_media_group(CHAT_ID, group)
         print("Отправлено")
         print(len(mess))
      print(len(mess))
      bot.send_message(message.chat.id, "Фото отправлены, теперь отправьте видео", parse_mode="Markdown", reply_markup=create_button("Отправить видео"))


   elif message.text == "Отправить видео":
      global vid
      while (len(vid) != 0):
         group = []
         for i in range(min(len(vid), 10)):
            el = vid[0]
            group.append(types.InputMediaVideo(el.video.file_id))
            del vid[0]
         bot.send_media_group(CHAT_ID, group)
         print("Отправлено")
         print(len(vid))
      print(len(vid))
      bot.send_message(message.chat.id, "Видео отправлены, форма заполненена", parse_mode="Markdown",
                       reply_markup=webAppKeyboard())

   else: start_fun(message)



@bot.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):
   # print(webAppMes) #вся информация о сообщении
   t = webAppMes.web_app_data.data
   t = t.split("\n")
   print(t) #конкретно то что мы передали в бота
   bot.send_message(webAppMes.chat.id, f"инофрмация из формы получена") 
   if(t[0] != "" and t[1] != '' and t[2] != '' and t[5] != "-Выберете модель дома-" and t[6] != "-Выберете тип монтажа-" and t[7] != "" and t[8] != '-Выберете тип обращения-'):
      st = f"ФИО клиента: {t[0]};\nФИО выездного: {t[1]};\nФИО монтажника: {t[2]};\nДата выезда: {t[3]};\nДата подписания КС: {t[4]};\nМодель дома: {t[5]};\nТип монтажа: {t[6]};\nАдрес объекта: {t[7]};\nТип обращения: {t[8]};\nКомментарий: {t[9]}."
      bot.send_message(webAppMes.chat.id, st)
      global CHAT_ID
      chat = CHAT_ID
      bot.send_message(chat,st)

      keyboard = types.ReplyKeyboardMarkup(row_width=1)
      one = types.KeyboardButton(text="Отправить фото")
      keyboard.add(one)

      bot.send_message(webAppMes.chat.id, "Отправьте фото", parse_mode="Markdown", reply_markup=keyboard)
   else:
      bot.send_message(webAppMes.chat.id, "Заполнены не все поля, заполните форму полностью.")
   #отправляем сообщение в ответ на отправку данных из веб-приложения 

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
   global CHAT_ID
   global mess
   mess.append(message)
   # bot.forward_message(chat_id=CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)


@bot.message_handler(content_types=['video'])
def handle_video(message):
   global vid

   video = message
   vid.append(video)


if __name__ == '__main__':
   bot.infinity_polling()