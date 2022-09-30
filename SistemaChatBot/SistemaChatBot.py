from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa, lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        var = True
        for i in lista_bots:
            if not isinstance(i, Bot):
                var = False
        if var: self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print('Olá, esse é o sistema de chatbots da empresa CrazyBots\n')
        # mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Os chatbots disponíveis no momento são:')
        for i,j in self.__lista_bots:
            print(i, '- Bot:', j.nome, '- Mensagem de apresentação: ',
                  j.apresentacao)
        # mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        print('Digite o número do chatbot desejado:', end='')
        i = int(input())
        print(i)
        self.__bot = self.__lista_bots[i]
        print()
        print('-->',self.__bot.nome, 'diz:', self.__bot.boas_vindas)
        # faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        chaves = self.__bot.mostra_comando.split()
        k = len(chaves)
        for i in range(k):
            print(i, '-', chaves[i])
        # mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        print('Digite o comando desejado (ou -1 fechar o programa e sair):', end='')
        i = int(input())
        print(i)
        print()
        if i == -1: 
            k = self.__bot.despedida
            l = ''
        else:
            chaves = self.__bot.mostra_comando.split()
            k = chaves[i]
            l = '\n --> Eu te respondo:',"'" + self.__bot.executa_comando(k) + ""
        print('-->', self.__bot.nome, "diz: Você disse", "'" + k + "'", end='')
        print(l)
        return i
        # faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        boas_vindas()
        mostra_menu()
        escolhe_bot()
        mostra_comandos_bot()
        while True:
            a = le_envia_comando()
            if a == -1: break
            mostra_comandos_bot()

        
        # mostra mensagem de boas-vindas do sistema
        # mostra o menu ao usuário
        # escolha do bot      
        # mostra mensagens de boas-vindas do bot escolhido
        # entra no loop de mostrar comandos do bot e 
        # escolher comando do bot até o usuário definir a saída
        # ao sair mostrar a mensagem de despedida do bot
