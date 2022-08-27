# importando bibliotecas:
from telebot import *
from pytube import *

api = "TOKEN"
bot = telebot.TeleBot(api)

# Chamando a funcao da biblioteca telebot:
@bot.message_handler(func=lambda message: True)
def msg(cr):
    # Verifica se possui /sgt na entrada:
    if "/sgt" in cr.text:

        # Filtra o comando, parametro e o link da entrada:
        command, res, link = cr.text.split()

        # Passando o link para a biblioteca pytube:
        yt = YouTube(link)
        bot.reply_to(cr, "Baixando video: " + yt.title)
        if res == "-p":
            vid = yt.streams.get_by_itag(18)

            # Baixando o video:
            vid.download()
            bot.reply_to(cr, "Baixando video em 360p")
            video = open(yt.title + ".mp4", 'rb')
            bot.send_video(cr, video)

# Funcao para o bot rodar sem parar:            
bot.infinity_polling()
