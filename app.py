#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
dicioYoda = {'Bom Dia': 'Bom dia pra quem?', 
             'Qual o seu nome?': 'É sério que você quer que eu repita? É Yoda!!!',
             'Quero um conselho': 'Não tenho filho desse tamanho.',
             'Adeus': 'Já vai tarde!'}
lista_bots = [BotZangado("Yoda", dicioYoda)]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()