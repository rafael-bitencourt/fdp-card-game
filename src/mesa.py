class Mesa:
    def __init__(self):
        self.__vencedor_de_mesa = None
        self.__jogadores_na_mesa = []
    
    def get_vencedor_de_mesa(self):
        return self.__vencedor_de_mesa
    
    def get_jogadores_na_mesa(self):
        return self.__jogadores_na_mesa
    
    def set_vencedor_de_mesa(self, vencedor):
        self.__vencedor_de_mesa = vencedor
    
    def set_jogadores_na_mesa(self, jogadores):
        self.__jogadores_na_mesa = jogadores