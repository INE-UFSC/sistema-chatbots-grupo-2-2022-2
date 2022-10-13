from Bots.bot import Bot

class BotTriste_3(Bot):
    def __init__(self, nome):
        comandos = {"Qual o seu nome?": "Meu nome é tristeza. Na verdade é %s mas é quase a mesma coisa..." % nome,
        "Quero um conselho.": "Meu conselho é você não me perguntar nada. Eu não sei nada.",
        "Quero uma piada.": "Eu não sei contar piadas. Eu sou triste."}

        super().__init__(nome, comandos)
        #Super classe = Bot, passa-se os parâmetros para o construtor dela
    
    def mostra_comandos(self):
        return super().mostra_comandos()
    
    def executa_comando(self, cmd):
        return super().executa_comando(cmd)

    def apresentacao(self):
        return "%s diz: Olá, eu sou o %s e estou triste hoje :(" % (self.nome, self.nome) 

    def boas_vindas(self):
        return "%s diz: Por quê me escolher? Eu não sou feliz :/" % self.nome 

    def despedida(self):
        return "%s diz: Ainda bem, agora posso ficar triste sozinho." % self.nome