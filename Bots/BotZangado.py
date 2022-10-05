from Bots.bot import Bot

comandos = {'Bom dia': 'Não existe bom dia. HOjé é um mau dia!',
            'Qual o seu nome?': 'Você já sabe meu nome!',
            'Quero um conselho': 'Um conselho? Converse com outro bot.',
            'Adeus': 'FINALMENTE! Tchau!'}

class BotZangado(Bot):
    def __init__(self, nome, comandos=comandos):
        super().__init__(nome, comandos)

    def mostra_comandos(self):
        return super().mostra_comandos()

    def executa_comando(self,cmd):
       return super().executa_comando(cmd)

    def apresentacao(self):
        return 'Grrrrrr. Meu nome é ' + self.nome + ' e eu te odeio!'
 
    def boas_vindas(self):
        return 'Eu não posso acreditar que você me escolheu, GRRRRRR!'

    def despedida(self):
        return 'FINALMENTE, é o dia mais feliz da minha vida. ADEUS!'
