from baralho import Baralho
from mesa import Mesa

class Rodada:
    def __init__(self, player_interface, jogadores, numero_da_rodada):
        print(f"-> RODADA {numero_da_rodada} INICIADA")
        # Atributos da rodada
        self.__player_interface = player_interface
        self.__numero_da_rodada = numero_da_rodada
        self.__jogadores = jogadores
        self.__numero_da_mesa = 1
        self.__mesa = Mesa(self.__player_interface, self.__jogadores)
        self.__baralho = Baralho()
        self.__baralho.embaralhar()
        self.distribuir_cartas()
        self.__terminou = False

    # Distribuir cartas
    def distribuir_cartas(self):
        for jogador in self.__jogadores:
            jogador.set_cartas_jogador(self.__baralho.retirar_cartas(self.__numero_da_rodada))

    # Jogar carta
    def jogar_carta(self):
        self.__mesa.adicionar_jogador_na_mesa()

        # Verificar fim de rodada
        if self.__mesa.terminou():
            if self.__numero_da_mesa == self.__numero_da_rodada:
                self.atribuir_pontos()
                self.proximo_que_inicia()
                self.limpar_quantas_fez()
                self.limpar_quantas_disse()
                self.__terminou = True
            else:
                self.criar_mesa()
    
    # Atribuir pontos
    def atribuir_pontos(self):
        for jogador in self.__jogadores:
            diferenca = abs(jogador.get_quantas_disse() - jogador.get_quantas_fez())
            jogador.incrementar_total_pontos(diferenca)

    # Continuar rodada
    def proximo_que_inicia(self):
        for jogador in self.__jogadores:
            if jogador.get_indice() == (self.__numero_da_rodada % 4) + 1:
                jogador.set_turno(True)
            else:
                jogador.set_turno(False)

    # Criar nova mesa
    def criar_mesa(self):
        self.__numero_da_mesa += 1
        self.__mesa = Mesa(self.__player_interface, self.__jogadores)

    # Get fim rodada
    def terminou(self):
        return self.__terminou

    # Limpar quantas fez
    def limpar_quantas_fez(self):
        for jogador in self.__jogadores:
            jogador.set_quantas_fez(0)
    
    # Limpar quantas disse
    def limpar_quantas_disse(self):
        for jogador in self.__jogadores:
            jogador.set_quantas_disse(0)


        
            
