import math
from rodada import Rodada

class Jogo:
    def __init__(self, jogadores):
        print("-> JOGO INICIADO")
        self.__jogadores = jogadores
        self.__numero_da_rodada = 1
        self.__rodada = Rodada(self.__numero_da_rodada, self.__jogadores)
        self.__terminou = False

    # Jogar carta
    def jogar_carta(self):
        self.__rodada.jogar_carta()

        # Verificar fim de jogo
        if self.__rodada.terminou():
            if self.__numero_da_rodada == 7:
                self.__terminou = True
            else:
                self.criar_rodada()

        if self.__terminou:
            print(f"-> JOGO TERMINADO")
            placar = self.computar_placar()
            for jogador, pontos in placar:
                print(f"{jogador.get_nome()}: {pontos} pontos")


    # Computar vencedor do jogo
    def computar_placar(self):
        pontos = {}
        for jogador in self.__jogadores:
            pontos[jogador] = jogador.get_total_pontos()
        return sorted(pontos.items(), key=lambda x: x[1])
        
    
    # Criar nova rodada
    def criar_rodada(self):
        self.__numero_da_rodada += 1
        self.__rodada = Rodada(self.__numero_da_rodada, self.__jogadores)
    
    # Get fim jogo
    def terminou(self):
        return self.__terminou



        
        