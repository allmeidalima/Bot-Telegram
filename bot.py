import json

class Wolf():

    def __init__(self):
        self.memory = open('memoria.json', 'w')
        self.memory.write('''[["WOLF", "Lucas", "Claudia"], {"Bom dia" : "Bom dia", "Boa tarde" : "Boa tarde", "Boa noite" : "Boa noite"}]''')
        self.memory.close()
        self.memory = open('memoria.json', 'r')

        self.people, self.message = json.load(self.memory)
        self.memory.close()


Wolf()


