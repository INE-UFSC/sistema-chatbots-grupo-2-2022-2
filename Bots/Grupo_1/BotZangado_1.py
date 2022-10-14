from Bots.bot import Bot
from SistemaChatBot.Comando import Comando


COMANDOS = [
    Comando(1, "Bom dia", ["Só se for pra você."]),
    Comando(2, "Qual o seu nome?", ["Te interessa?"]),
    Comando(3, "Quero um conselho", ["E eu tenho cara de psicólogo por acaso?"]),
    Comando(4, "Do que você gosta?", ["De tudo que você odeia"]),
    Comando(5, "Como você está se sentindo?",["Zangado!!"]),
    Comando(6, "Por quê você está zangado?", ["Porque você está aqui"])
]


class BotZangado_1(Bot):
    def __init__(self,nome, comandos = COMANDOS):
        super().__init__(nome, comandos)

    def apresentacao(self):
        return "Olá, meu nome é " + {self.nome} + ". Eu estou tendo um péssimo dia, então por favor não faça nada para me irritar."
            
            
    def boas_vindas(self):
        return f"Nao consigo acreditar que eu tenho que fazer isso novamente...\n De qualquer maneira, boas-vindas caro cliente. Espero que a sua estadia seja breve e dolorosa."

    def despedida(self) -> str:
        return "Finalmente!! Espero nunca te ver novamente, seu chato!"
        