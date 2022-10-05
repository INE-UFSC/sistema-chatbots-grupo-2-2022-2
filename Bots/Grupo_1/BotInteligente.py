from Bots.bot import Bot

COMANDOS = {
    "Bom dia": "Bom dia! Este é um belo dia para aprender, não?",
    "Qual o seu nome?":"",
    "Quero um conselho":"Não há nada mais importante que o conhecimento, Buscador. Nunca se esqueça disso",
    "Do que você gosta?":"Livros, Buscador! Eles são a essência do aprendizado e possuem segredos inimagináveis para os não-iniciados",
    "Como você está se sentindo?":"Curioso. Há tantos segredos ainda não descobertos...",
}


class BotInteligente(Bot):
    def __init__(self,nome, comandos = COMANDOS):
        #atualiza o nome
        comandos["Qual o seu nome?"] = f"{nome}, mestre dos magos e rei dos dragões"

        super().__init__(nome, comandos)

    def mostra_comandos(self):
        return super().mostra_comandos()
    
    def executa_comando(self, cmd):
        return super().executa_comando(cmd)

    def apresentacao(self):
        return f"Olá, meu nome é {self.nome}, detentor de todo o conhecimento existente"

    def boas_vindas(self):
        return f"Bem-vindo buscador da chama. Pronto para aprender sobre as maravilhas do universo?"

    def despedida(self) -> str:
        return "Espero que essa conversa tenha sido tão proveitosa para você quanto foi para mim. Adeus, buscador da chama"