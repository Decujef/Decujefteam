import telebot
bot = telebot.TeleBot("8320307281:AAFpDe7-E64hir-A-L5RnMcFLBjZQBpcLR0")
@bot.message_handlers(['Text'])
def m():
    bot.send_message("не")