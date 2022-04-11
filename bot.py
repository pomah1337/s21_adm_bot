import telebot
token = ""
bot = telebot.TeleBot(token)  # найти бота в телеграмме s21admbot
@bot.message_handler(content_types=['text'])


def get_text_messages(message):
    if message.text == "/info_supp":
        bot.send_message(message.from_user.id, """За что выдает пенальти отдел Support:
 ● Выход из учётки или скринлог экрана при включённом VPN;
 ● Упоминание сотрудников;
 ● Флуд в слаке.""")
    elif message.text == "/info_help":
        bot.send_message(message.from_user.id, """За что выдает пенальти отдел ADM:
 ● Запрещено приносить/хранить/распространять/использовать спиртные напитки, наркотические и одурманивающие средства, а также находиться в школе в состоянии алкогольного, наркотического или другого опьянения;"
 ● Запрещено приносить/хранить/распространять/использовать оружие, взрывчатые и огнеопасные вещества, горючие жидкости, пиротехнические изделия, газовые баллончики, а также ядовитые и токсические вещества, режущие и колющие предметы;
 ● Курение в здании запрещено! Разрешается курить на улице в специально отведенных зонах;
 ● Запрещены оскорбление и дискриминация любых участников и сотрудников Школы на территории школы, в чатах и других каналах;
 ● Запрещены драки и любые виды насилия;
 ● Запрещено использование нецензурной лексики на территории школы, а также в любых каналах коммуникации Школы;
 ● Запрещен флуд в рабочих каналах корпоративного месседжера Slack (все административные каналы);
 ● Запрещено использовать channel.""")
        # bot.send_message(message.from_user.id, adm)
    elif message.text == "/report":
        bot.send_message(message.from_user.id, "Написать отзыв о работе команды Школы 21 - https://clck.ru/eoyYp")

    else:
        bot.send_message(message.from_user.id, """Введи
         /info_supp (за что выдает пенальти отдел Support)
         
         /info_help (за что выдает пенальти отдел ADM)
         
         /report (написать отзыв о работе команды Школы 21)""")

bot.polling(none_stop=True, interval=0)
