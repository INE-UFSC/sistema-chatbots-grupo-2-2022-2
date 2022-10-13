from Bots.bot import Bot

comandos = {
"Bom dia": "Que lindo dia para falar com uma pessoa legal!",
"Qual é o seu nome?": "mal te conheci e já te amooo! Meu nome é ",
"Conselho": "Ajeite a postura.",
"Adeus": "Auf wiedersehen! Até mais ver, sentirei saudades."
}

class BotFeliz4(Bot):
    def __init__(self, nome='Johann', comandos=comandos):
        super().__init__(nome, comandos)
        self.nome = nome
        self.comandos = comandos
            
    def apresentacao(self):
        return "Me chamo " + self.nome +',  prazer em conhecer você!'

    def boas_vindas(self):
        return "Ainda bem que você me escolheu!"

    def despedida(self):
        return "Ahhh que pena, queria conversar mais contigo. Ate a proxima!"