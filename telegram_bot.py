import telegram

bot = telegram.Bot(token = '1009840016:AAG8G8EHAU7wW6HR8toY21J0xIButtY3-T4')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id=1038006440, text="테스트입니다.")

# inflearn-testbot
# username : mijungbot
# token : 1009840016:AAG8G8EHAU7wW6HR8toY21J0xIButtY3-T4