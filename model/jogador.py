
class Jogador:
    def __init__(self, index):
        self.__index = index
        self.__cartas_jogador = []
        self.__vez_de_jogar = False
        self.__quantas_disse = 0
        self.__quantas_fez = 0
        self.__pontos = 0
        self.__carta_jogada = None
    
    def get_index(self):
        return self.__index
    
    def get_cartas_jogador(self):
        return self.__cartas_jogador
    
    def get_vez_de_jogar(self):
        return self.__vez_de_jogar
    
    def get_quantas_disse(self):
        return self.__quantas_disse
    
    def get_quantas_fez(self):
        return self.__quantas_fez
    
    def get_pontos(self):
        return self.__pontos
    
    def get_carta_jogada(self):
        return self.__carta_jogada
    
    def set_cartas_jogador(self, cartas):
        self.__cartas_jogador = cartas

    def set_vez_de_jogar(self, vez):
        self.__vez_de_jogar = vez
    
    def set_quantas_disse(self, quantas_disse):
        self.__quantas_disse = quantas_disse
    
    def set_quantas_fez(self, quantas_fez):
        self.__quantas_fez = quantas_fez
    
    def set_pontos(self, pontos):
        self.__pontos = pontos
    
    def set_carta_jogada(self, carta):
        self.__carta_jogada = carta
    