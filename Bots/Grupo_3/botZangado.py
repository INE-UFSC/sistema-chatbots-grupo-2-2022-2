from Bots.bot import Bot

class BotZangado_3(Bot):
    def __init__(self, nome):
        comandos = {"Qual é o seu nome?" : f"Meu nome é {nome} e pare de falar comigo", 
        "Quero um conselho.": "Meu conselho é que você vá embora. Eu não quero conversar com você!",
        "Quero uma piada.": "Não sou palhaço para contar uma piada para você. Vá embora!"}
        super().__init__(nome , comandos)
    
    def mostra_comandos(self):
        return super().mostra_comandos()
    
    def executa_comando(self, cmd):
        return super().executa_comando(cmd)

    def apresentacao(self):
        return f"{self.nome} diz: Estou dormindo escolha outro bot."

    def boas_vindas(self):
        return f"{self.nome} diz: Porque você me escolheu. Eu te odeio!" 

    def despedida(self):
        return f"{self.nome} diz: Finalmente! Não aguentava mais você!"