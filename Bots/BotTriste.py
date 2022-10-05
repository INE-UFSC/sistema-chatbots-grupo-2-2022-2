from Bots.bot import Bot

comandos =  {'Bom dia': 'Bom dia? Não acho, mas já que voce diz...',
            'Qual o seu nome?': 'Meu nome é ',
            'Quero um conselho': 'Não crie expectativas',
            'Adeus': 'Adeus!'}

class BotTriste(Bot):
    def __init__(self, nome, comandos=comandos):
        super().__init__(nome, comandos)
        comandos['Qual o seu nome?'] += self.nome

    def mostra_comandos(self):
        return super().mostra_comandos()

    def executa_comando(self, cmd):
       return super().executa_comando(cmd)

    def apresentacao(self):
        return 'Oi, eu sou o %s' % (self.nome)
 
    def boas_vindas(self):
        return 'Oi, o que você quer?'

    def despedida(self):
        return 'Tchau'
