from Bots.bot import Bot

class BotTriste(Bot):
    def __init__(self, nome='Triste', comandos={}):
        super().__init__(nome, comandos)

    def mostra_comandos(self):
        return super().mostra_comandos()

    def executa_comando(self, cmd):
       return super().executa_comando(cmd)

    def apresentacao(self):
        return 'Oi'
 
    def boas_vindas(self):
        return 'Oi, o que você quer?'

    def despedida(self):
        return 'Tchau'
