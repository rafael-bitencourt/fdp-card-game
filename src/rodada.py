from baralho import Baralho
from mesa import Mesa
import time

class Rodada:
    def __init__(self, player_interface, jogadores, numero_da_rodada):
        # Atributos da rodada
        self.__player_interface = player_interface
        self.__numero_da_rodada = numero_da_rodada
        self.__player_interface.set_inicio_de_rodada(True)
        self.__player_interface.set_botao_bloqueado(None)
        self.__quantos_disseram = 0
        self.__total_dito = 0
        self.__jogadores = jogadores
        self.__numero_da_mesa = 1
        self.__mesa = Mesa(self.__player_interface, self.__jogadores)
        self.__terminou = False

        for jogador in self.__jogadores:
            if jogador.get_turno():
                break

        if jogador == self.__player_interface.get_jogador_local():
            self.__baralho = Baralho()
            self.__baralho.embaralhar()
            self.distribuir_cartas()

    # Distribuir cartas
    def distribuir_cartas(self):
        time.sleep(1)
        jogada = {}
        jogada["tipo"] = "distribuir_cartas"
        jogada["match_status"] = "progress"
        for jogador in self.__jogadores:
            strings_cartas = []
            cartas = self.__baralho.retirar_cartas(self.__numero_da_rodada)
            jogador.set_cartas_jogador(cartas)
            for carta in cartas:
                strings_cartas.append(carta.get_nome())
            jogada[jogador.get_nome()] = strings_cartas
        self.__player_interface.enviar_jogada(jogada)

    # Diz quantas faz
    def diz_quantas_faz(self):
        self.__quantos_disseram += 1
        # Bloquear botão diz quantas faz
        if self.__quantos_disseram == 3:
            for jogador in self.__jogadores:
                self.__total_dito += jogador.get_quantas_disse()
            self.__player_interface.set_botao_bloqueado(self.__numero_da_rodada - self.__total_dito)
        # Verificar fim de diz quantas faz
        if self.__quantos_disseram == 4:
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
    def jogar_carta(self, jogador):
        self.__mesa.adicionar_jogador_na_mesa(jogador)

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


        
            
