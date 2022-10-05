#encoding: utf-8
from Bots.Grupo_1.BotInteligente import BotInteligente
from Bots.Grupo_1.BotZangado_1 import BotZangado_1
from SistemaChatBot import SistemaChatBot as scb
from Bots.bot import Bot
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste


###construa a lista de bots disponíveis aqui
lista_bots = [
    BotZangado("Yodaqa"), 
    BotTriste("Emuo"),
    BotInteligente("Gandalf"),
    BotZangado_1("Jonas")
]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()