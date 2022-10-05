from Bots.bot import Bot


class BotZangado(Bot):
    def __init__(self, nome='Zangado', comandos={}):
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
