from Bots.bot import Bot
from SistemaChatBot.Comando import Comando

comandos =  [Comando(1, 'Bom dia', ['Bom dia? Não acho, mas já que voce diz...']),
            Comando(2, 'Qual o seu nome?', 'Meu nome é '),
            Comando(3, 'Quero um conselho', 'Não crie expectativas'),
            Comando(4, 'Adeus', 'Adeus!')]

class BotTriste(Bot):
    def __init__(self, nome, comandos=comandos):
        self.nome = nome
        self.comandos = comandos
        self.comandos[1].addResposta('Meu nome é ' + self.nome)
        super().__init__(self.nome, self.comandos)

    def apresentacao(self):
        return 'Oi, eu sou o ' + self.nome
 
    def boas_vindas(self):
        return 'Oi, o que você quer?'

    def despedida(self):
        return 'Tchau'
