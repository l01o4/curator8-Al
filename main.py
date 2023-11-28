import telebot

bot = telebot.TeleBot('6952088842:AAGFUGZnq6HnYBTN7un2xJxGoLG0ysEOxKQ')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'привет йоу', parse_mode='Markdown')


@bot.message_handler(commands=['Nikita'])
def main(message):
    bot.send_message(message.chat.id, '*бутылка в шкафчик отправлена*', parse_mode='Markdown')


@bot.message_handler(commands=['negative'])
def main(message):
    bot.send_message(message.chat.id, '*не плачь и не грусти, лучше подписчиков накрути*', parse_mode='Markdown')


@bot.message_handler(commands=['im_programmer'])
def main(message):
    bot.send_message(message.chat.id, 'на ваш счет зачислено *1000000*', parse_mode='Markdown')


@bot.message_handler(commands=['pay'])
def main(message):
    bot.send_message(message.chat.id, '*С вашего счёта списано 500 рублей.*', parse_mode='Markdown')


@bot.message_handler(commands=['cringe'])
def main(message):
    bot.send_message(message.chat.id, 'написал бывший?\nотправь его в чс и *кайфуй*', parse_mode='Markdown')


@bot.message_handler(commands=['sad'])
def main(message):
    bot.send_message(message.chat.id, 'что делать если тебя все обижают? уйди в туалет', parse_mode='Markdown')


@bot.message_handler(commands=['Lilya'])
def main(message):
    bot.send_message(message.chat.id, 'с тобой я чувствую себя *happy*', parse_mode='Markdown')


@bot.message_handler(commands=['Mannanchik'])
def main(message):
    bot.send_message(message.chat.id, 'я за тобой слежу', parse_mode='Markdown')


@bot.message_handler(commands=['Karina'])
def main(message):
    bot.send_message(message.chat.id, 'ты случайно не Каринина еда? тогда почему ты так греешь мое сердце?',
                     parse_mode='Markdown')


@bot.message_handler(commands=['verysad'])
def main(message):
    bot.send_message(message.chat.id, 'i love you so', parse_mode='Markdown')


@bot.message_handler(commands=['ckychno'])
def main(message):
    bot.send_message(message.chat.id, 'пиши [мне](http://t.me/alinkoos)', parse_mode='Markdown')


bot.infinity_polling()