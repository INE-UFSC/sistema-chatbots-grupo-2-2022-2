#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.bot import Bot
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste


###construa a lista de bots disponíveis aqui
dZangado = {'Bom dia': 'Não existe bom dia. HOjé é um mau dia!',
            'Qual o seu nome?': 'Você já sabe meu nome!',
            'Quero um conselho': 'Um conselho? Converse com outro bot.',
            'Adeus': 'FINALMENTE! Tchau!'}

dTriste =  {'Bom dia': 'Bom dia? Não acho, mas já que voc^e diz...',
            'Qual o seu nome?': 'Meu nome é Emo',
            'Quero um conselho': 'Não crie expectativas',
            'Adeus': 'Adeus!'}

lista_bots = [BotZangado("Yoda", dZangado), BotTriste("Emo", dTriste)]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()