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
    
    def verificar_vencedor_mesa(self):
        carta_mais_alta = None
        vencedor = None
        
        # Coleta as cartas jogadas na mesa por cada jogador
        for jogador in self.__jogadores_na_mesa:
            carta_jogada = jogador.get_carta_jogada()
            
            # Verifica se a carta atual é mais alta do que a carta mais alta já registrada
            if carta_mais_alta is None or carta_jogada.valor > carta_mais_alta.valor:
                carta_mais_alta = carta_jogada
                vencedor = jogador
                
        return vencedor