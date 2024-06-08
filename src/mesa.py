class Mesa:
    def __init__(self):
        self.__jogadores_na_mesa = []

    def adicionar_jogador_na_mesa(self, jogador):
        self.__jogadores_na_mesa.append(jogador)

    def computar_vencedor_mesa(self):
        vencedor = None
        for jogador in self.__jogadores_na_mesa:
            if jogador.carta_jogada.get_forca() >= vencedor.carta_jogada.get_forca() or vencedor == None:
                vencedor = jogador
        return vencedor

    def limpar_mesa(self):
        self.__jogadores_na_mesa = []

    def get_jogadores_na_mesa(self):
        return self.__jogadores_na_mesa
    
    