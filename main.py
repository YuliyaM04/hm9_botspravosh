from ast import parse
import telebot
from telebot import types
import random
import xlrd
import csv
token = '5760711716:AAFSpGaECWYpBc4qoE3GKgzU8gBqEaVfAB4'
bot = telebot.TeleBot(token)
userkal=[]
#@bot.message_handler(content_types=['text'])#commands=['start'])

def main_menu():
    print('\Выберите:')
    print('1. Показать все контакты') #Таблицей
    print('2. Добавить контакты')
    x=1
    return x
    

@bot.message_handler(content_types=['text'])



def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Показать все контакты")
    but2 = types.KeyboardButton("Добавить контакт")
    markup.add(but1, but2)

    #bot.reply_to(message, "Здравствуй, {0.first_name}\nСмотрю, ты за Единую, Великую и Недилимую".format(message.from_user)
  #,parse_mode='html',reply_markup=markup)
    bot.send_message(message.chat.id,"Выберите действие.", reply_markup = markup)
    if message.text=="Показать все контакты":
        with open('bookT.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.reader(csvfile ,delimiter=';')
            for row in spamreader:
               bot.send_message(message.chat.id,' | '.join(row))
        #bot.reply_to(message,"НЕТУ")
    if message.text=="Добавить контакт":
        bot.send_message(message.chat.id,"Уточните Имя")
        #bot.reply
        bot.register_next_step_handler(message,name)
        #name()
        #fam=message.text
        #bot.reply_to(message,"Уточните Имя")
        #name=message.text
        #bot.reply_to(message,fam +""+ name +"Добавлен")

def fam(message):
    chat_id=message.chat.id   
    fam=message.text
    userkal.append(fam)
    
    
    bot.send_message(message.chat.id,"Уточните Телефон")
    #bot.register_next_step_handler(message,save)
    bot.register_next_step_handler(message,telefon)
def name(message):
    chat_id=message.chat.id
    
    name=message.text
    userkal.append(name)
    bot.send_message(message.chat.id,"Уточните Фамилию")
    bot.register_next_step_handler(message,fam)

def telefon(message):
    chat_id=message.chat.id
    tel=message.text
    userkal.append(tel)
    zapis(userkal)
    bot.send_message(message.chat.id,userkal[1] + " " + userkal[0] + " " +"Добавлен")
    bot.clear_step_handler_by_chat_id(chat_id)
    start(message)
    

def zapis(userkal):
   
    with open (r'bookT.csv',"a", newline='',encoding = 'utf-8',) as writerowtobook:
        writer=csv.writer(writerowtobook,delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(userkal)
    userkal=[]

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()

#bot.polling(none_stop=True)

