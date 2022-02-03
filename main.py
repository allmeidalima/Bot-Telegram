import time, telepot, json
from telepot.loop import MessageLoop
from bot import Wolf

with open('token.json', 'r') as file:
    TOKEN = json.load(file)

telegram = telepot.Bot(TOKEN)
bot = Wolf()

def handle(msg):
    user_phrase = bot.listen(phrase=msg['text'])
    response = bot.think(user_phrase)
    bot.speak(response)
    content_type, chat_type, chat_id = telepot.glance(msg)
    telegram.sendMessage(chat_id, response)
    
    #print(msg)
    #print(content_type, chat_type, chat_id)
    
    #if content_type == 'text':

MessageLoop(telegram, handle).run_as_thread()
print ('Listening ...')

#TOKEN = json_file


# Keep the program running.
while 1:
    time.sleep(10)