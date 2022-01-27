import time, telepot, json
from telepot.loop import MessageLoop
from bot import Wolf

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(msg)
    #print(content_type, chat_type, chat_id)
    

    if content_type == 'text':
        bot.sendMessage(chat_id, " ")

with open('token.json', 'r') as file:
    TOKEN = json.load(file) 

#TOKEN = json_file

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)