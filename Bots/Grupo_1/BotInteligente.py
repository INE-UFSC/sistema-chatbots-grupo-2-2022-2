from Bots.bot import Bot
from SistemaChatBot.Comando import Comando


COMANDOS = [Comando(1, 'Bom dia', ["Bom dia! Este é um belo dia para aprender, não?"]),
            Comando(2, 'Qual o seu nome?', ''),
            Comando(3, 'Quero um conselho', "Não há nada mais importante que o conhecimento, Buscador. Nunca se esqueça disso"),
            Comando(4, "Do que você gosta?", ["Livros, Buscador! Eles são a essência do aprendizado e possuem segredos inimagináveis para os não-iniciados"]),
            Comando(5, "Como você está se sentindo?", ["Curioso. Há tantos segredos ainda não descobertos..."])]


class BotInteligente(Bot):
    def __init__(self,nome, comandos = COMANDOS):
        #atualiza o nome
        self.comandos = COMANDOS
        self.nome = nome
        self.comandos[1] = self.nome + ", mestre dos magos e rei dos dragões"

        super().__init__(self.nome, self.comandos)

    def apresentacao(self):
        return "Olá, meu nome é " + self.nome + ", detentor de todo o conhecimento existente"

    def boas_vindas(self):
        return "Bem-vindo buscador da chama. Pronto para aprender sobre as maravilhas do universo?"

    def despedida(self) -> str:
        return "Espero que essa conversa tenha sido tão proveitosa para você quanto foi para mim. Adeus, buscador da chama"