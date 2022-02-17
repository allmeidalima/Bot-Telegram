import json
import sys, os, webbrowser
import subprocess as sp
from subprocess import Popen 



class Wolf():

    def __init__(self):
        try:
            self.memory = open('memoria.json', 'r')
        except FileNotFoundError:
            self.memory = open('memoria.json', 'w')
            self.memory.write('''[["WOLF", "Lucas", "Claudia"], {"Bom dia" : "Bom dia", "Boa tarde" : "Boa tarde", "Boa noite" : "Boa noite", "Como você esta?" : "Eu estou bem, obrigado por perguntar.", "Quem te criou?" : "Meu criador se chama Lucas ele é meu Deus!", "Quem o Lucas ama?" : "Mais é claro que é a Claudinha"}]''')
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
        elif 'Abra link' in phrase:
            def openLink(linkPhrase):
                platform = sys.platform
                link = linkPhrase.replace('Abra link ', '')
                if 'win' in platform:
                    os.startfile(link)
                elif 'linux' in platform:
                    try:
                        sp.Popen(link)
                    except FileNotFoundError:
                        sp.Popen(['xdg-open', link])
                elif 'darwin' in platform:
                    webbrowser.open(link)
            openLink(phrase)
        elif phrase not in self.message:
            return 'Não sei responder isso ainda, mas garanto pra você que uma hora eu aprendo!'

    def speak(self, bot_phrase):
        self.historic.append(bot_phrase)
#Wolf()


