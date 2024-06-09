import math

class Jogo:
    def __init__(self, jogadores, indice_local):
        self.__jogadores = jogadores
        self.__indice_local = indice_local
    
    def get_jogadores(self):
        return self.__jogadores
    
    def get_indice_local(self):
        return self.__indice_local

    def computar_vencedor_jogo(self):
        jogadores = self.get_jogadores()
        menor = math.inf
        for i in range(len(jogadores)):
            if jogadores[i].get_total_pontos() < menor:
                menor = jogadores[i].get_total_pontos()
                jogador_menos_pontos = jogadores[i]   
        return jogador_menos_pontos
        
        