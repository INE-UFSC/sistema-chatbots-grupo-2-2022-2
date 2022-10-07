#encoding: utf-8
from Bots.Grupo_1.BotInteligente import BotInteligente
from Bots.Grupo_1.BotZangado_1 import BotZangado_1
from Bots.Grupo_3.botFeliz import BotFeliz_3
from Bots.Grupo_3.botTriste import BotTriste_3
from Bots.Grupo_3.botZangado import BotZangado_3
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste


###construa a lista de bots disponíveis aqui
lista_bots = [
    BotZangado("Yodaqa"), 
    BotTriste("Emuo"),
    BotInteligente("Gandalf"),
    BotZangado_1("Jonas"),
    BotFeliz_3("Pedro"),
    BotTriste_3("João"),
    BotZangado_3("Tony")
]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()