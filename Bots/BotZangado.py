from Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome,comandos:{}):
        self.__nome = nome
        self.__comandos = comandos


    #nao esquecer o decorator
    def nome(self):
        return self.__comandos['Qual o seu nome?']

    #nao esquecer o decorator
    def setNome(nome):
        self.__nome = nome

    def apresentacao(self):
        return self.__comandos["apresentacao"]

    def mostra_comandos(self):
        retorno = ""
        for key in self.__comandos.keys():
            retorno = retorno + " " + key
        return retorno

    def executa_comando(self,cmd):
        if cmd == 'Bom Dia':
            self.boas_vindas()
        elif cmd == 'Qual o seu nome?':
            self.nome()
        elif cmd == 'Quero um conselho':
            self.conselho()

    def boas_vindas(self):
        return self.__comandos['Bom Dia']

    def despedida(self):
        return self.__comandos['Adeus']
    def conselho(self):
        return self.__comandos['Quero um conselho']