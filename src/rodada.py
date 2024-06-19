from baralho import Baralho
from mesa import Mesa

class Rodada:
    def __init__(self, numero_da_rodada):
        self.__numero_da_rodada = numero_da_rodada
        self.__jogador_comeca_mesa = None
        self.__baralho = Baralho()
        self.__baralho.embaralhar()
        self.__mesa_atual = 0
        self.__mesa_maxima = 7
        self.__mesa = Mesa()
    
    def get_numero_da_rodada(self):
        return self.__numero_da_rodada

    def get_jogador_comeca_mesa(self):
        return self.__jogador_comeca_mesa
    
    def get_mesa_atual(self):
        return self.__mesa_atual

    def get_mesa_maxima(self):
        return self.__mesa_maxima
    
    def get_mesa(self):
        return self.__mesa
    
    def set_numero_da_rodada(self, numero):
        self.__numero_da_rodada = numero
    
    def set_jogador_comeca_mesa(self, jogador):
        self.__jogador_comeca_mesa = jogador
    
    def set_mesa_atual(self, n):
        self.__mesa_atual = n
    
    def set_mesa_maxima(self, n):
        self.__mesa_maxima = n

    def criar_mesa(self, jogadores):
        self.__mesa.set_jogadores_na_mesa(jogadores)
        self.__mesa_atual = 1
    
    def incrementar_mesa(self):
        self.__mesa_atual += 1
    
    def entregar_cartas(self):
        for jogador in self.__mesa.get_jogadores_na_mesa():
            cartas = self.__baralho.dar_cartas(self.__numero_da_rodada) # quantidade de cartas na mão dos jogadores é igual ao numero da rodada
            jogador.set_cartas_jogador(cartas)
