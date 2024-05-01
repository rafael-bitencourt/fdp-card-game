from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface

class Jogador(DogPlayerInterface):
    def __init__(self, nome):
        self.__nome = nome
        self.__cartas_jogador = []
        self.__vez_de_jogar = False
        self.__quantas_disse = 0
        self.__quantas_fez = 0
        self.__pontos = 0
        self.__carta_jogada = None
        self.dog_server_interface = DogActor()
        mensagem = self.dog_server_interface.initialize(self.__nome, self)
        print(mensagem)
    
    def get_nome(self):
        return self.__nome
    
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
    
    def jogar_carta(self):
        cartas_na_mao = self.get_cartas_jogador()
        #for carta in cartas_na_mao:
            #print('Suas cartas são: ', carta, end=' ')

        print(f'{self.__nome} Suas cartas são: ', [str(carta) for carta in cartas_na_mao])
        carta = input(f'{self.__nome}, digite o número da carta que deseja jogar: ')
        for carta_jogador in self.__cartas_jogador:
            if carta_jogador.get_numero() == int(carta):
                carta = carta_jogador
                break
        self.set_carta_jogada(carta)
        self.__cartas_jogador.remove(carta)

jogador1 = Jogador('Jogador 1')
jogador2 = Jogador('Jogador 2')
jogador3 = Jogador('Jogador 3')
jogador4 = Jogador('Jogador 4')
        
