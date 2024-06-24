class Jogador():
    def __init__(self, player):
        self.__nome = player[0]
        self.__indice = int(player[2])
        self.__cartas_jogador = []
        self.__turno = False
        self.__quantas_disse = 0
        self.__quantas_fez = 0
        self.__total_pontos = 0
        self.__carta_jogada = None
    
    def get_nome(self):
        return self.__nome
    
    def get_indice(self):
        return self.__indice
    
    def get_cartas_jogador(self):
        return self.__cartas_jogador
    
    def get_turno(self):
        return self.__turno
    
    def get_quantas_disse(self):
        return self.__quantas_disse
    
    def get_quantas_fez(self):
        return self.__quantas_fez
    
    def get_total_pontos(self):
        return self.__total_pontos
    
    def get_carta_jogada(self):
        return self.__carta_jogada

    def set_turno(self, turno):
        self.__turno = turno
    
    def set_quantas_disse(self, quantas_disse):
        self.__quantas_disse = quantas_disse
    
    def set_quantas_fez(self, quantas_fez):
        self.__quantas_fez = quantas_fez

    def incrementar_quantas_fez(self):
        self.__quantas_fez += 1
    
    def set_cartas_jogador(self, cartas):
        self.__cartas_jogador = cartas

    def incrementar_total_pontos(self, pontos):
        self.__total_pontos = self.__total_pontos + pontos

    def set_carta_jogada(self, carta):
        self.__carta_jogada = carta
    
    def jogar_carta(self, carta):
        print(f"{self.__nome} jogou a carta {carta}")
        self.__carta_jogada = carta
        for carta in self.__cartas_jogador:
            if str(carta) == str(self.__carta_jogada):
                self.__cartas_jogador.remove(carta)

