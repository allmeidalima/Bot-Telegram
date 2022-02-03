import json

class Wolf():

    def __init__(self):
        try:
            self.memory = open('memoria.json', 'r')
        except FileNotFoundError:
            self.memory = open('memoria.json', 'w')
            self.memory.write('''[["WOLF", "Lucas", "Claudia"], {"Bom dia" : "Bom dia", "Boa tarde" : "Boa tarde", "Boa noite" : "Boa noite", "Como você esta?" : "Eu estou bem, obrigado por perguntar."}]''')
            self.memory.close()
            self.memory = open('memoria.json', 'r')

        self.people, self.message = json.load(self.memory)
        self.memory.close()
        self.historic = [None]

    def listen(self, phrase=None):
        return phrase

    def think(self, phrase):
        if phrase in self.message:
            return self.message[phrase]

    def speak(self, bot_phrase):
        self.historic.append(bot_phrase)
#Wolf()


