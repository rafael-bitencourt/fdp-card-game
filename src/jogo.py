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
    
    def atribuir_pontos(self):
        jogadores = self.get_jogadores()
        for i in range(len(jogadores)):
            diferenca = abs(jogadores[i].get_quantas_disse() - jogadores[i].get_quantas_fez())
            jogadores[i].incrementar_total_pontos(diferenca)

        
        