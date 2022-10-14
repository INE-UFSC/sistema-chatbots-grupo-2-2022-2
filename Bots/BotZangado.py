from Bots.bot import Bot
from SistemaChatBot.Comando import Comando

comandos = [Comando(1, 'Bom dia', ['Não existe bom dia. HOjé é um mau dia!']),
            Comando(2, 'Qual o seu nome?', 'Você já sabe meu nome!'),
            Comando(3, 'Quero um conselho', 'Um conselho? Converse com outro bot.'),
            Comando(4, 'Adeus', 'FINALMENTE! Tchau!')]

class BotZangado(Bot):
    def __init__(self, nome, comandos=comandos):
        super().__init__(nome, comandos)

    def apresentacao(self):
        return 'Grrrrrr. Meu nome é ' + self.nome + ' e eu te odeio!'
 
    def boas_vindas(self):
        return 'Eu não posso acreditar que você me escolheu, GRRRRRR!'

    def despedida(self):
        return 'FINALMENTE, é o dia mais feliz da minha vida. ADEUS!'
