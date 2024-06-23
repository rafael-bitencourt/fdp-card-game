from baralho import Baralho
from mesa import Mesa

class Rodada:
    def __init__(self, player_interface, jogadores, numero_da_rodada):
        print(f"-> RODADA {numero_da_rodada} INICIADA")
        # Atributos da rodada
        self.__player_interface = player_interface
        self.__numero_da_rodada = numero_da_rodada
        self.__player_interface.set_inicio_de_rodada(True)
        self.__quantos_disseram = 0
        self.__total_dito = 0
        self.__jogadores = jogadores
        self.__numero_da_mesa = 1
        self.__mesa = Mesa(self.__player_interface, self.__jogadores)
        self.__baralho = Baralho()
        #self.__baralho.embaralhar()
        self.distribuir_cartas()
        self.__terminou = False

    # Distribuir cartas
    def distribuir_cartas(self):
        for jogador in self.__jogadores:
            jogador.set_cartas_jogador(self.__baralho.retirar_cartas(self.__numero_da_rodada))

    # Diz quantas faz
    def diz_quantas_faz(self):
        self.__quantos_disseram += 1
        # Verificar fim de diz quantas faz
        if self.__quantos_disseram == 4:
            for jogador in self.__jogadores:
                self.__total_dito += jogador.get_quantas_disse()
            self.__player_interface.set_botao_bloqueado(self.__numero_da_rodada - self.__total_dito)
            # Se sim desabilita inicio de rodada
            self.__player_interface.set_inicio_de_rodada(False)
            self.__quantos_disseram = 0

        # Passa para o próximo jogador
        self.proximo_da_mesa()

    # Calcular proximo da mesa
    def proximo_da_mesa(self):

        for atual in self.__jogadores:
            if atual.get_turno():
                atual.set_turno(False)
                break

        for proximo in self.__jogadores:
            if proximo.get_indice() == ((atual.get_indice() % 4) + 1):
                proximo.set_turno(True)
                break


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


        
            
