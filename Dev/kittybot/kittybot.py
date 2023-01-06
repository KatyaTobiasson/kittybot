from telegram import Bot

# Здесь укажите токен, 
# который вы получили от @Botfather при создании бот-аккаунта
bot = Bot(token='5950069262:AAEU9l56sRRQjO36Axiuy8gmh52E-Nx7w5Q')

# Укажите id своего аккаунта в Telegram
chat_id = 51867841
text = 'Вам телеграмма!'

# Отправка сообщения
bot.send_message(chat_id, text) 