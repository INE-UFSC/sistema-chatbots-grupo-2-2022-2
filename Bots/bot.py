##implemente as seguintes classes
from abc import ABC, abstractmethod
from SistemaChatBot.Comando import Comando

class Bot(ABC):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    def mostra_comandos(self):
        r = ''
        for i in self.__comandos:
            r += i.msg + '\n'
        return r[:-1]

    def executa_comando(self,cmd):
        i = self.__comandos.index(cmd)
        return self.__comandos[i].msg

    @abstractmethod
    def apresentacao():
        pass
    
    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass