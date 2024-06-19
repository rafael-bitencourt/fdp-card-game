class Mesa:
    def __init__(self, jogadores):
        print("-> NOVA MESA INICIADA")
        # Atributos da mesa
        self.__jogadores = jogadores
        self.__vencedor_da_mesa = None
        self.__cartas_na_mesa = 0
        self.__terminou = False

    # Adicionar jogador na mesa
    def adicionar_jogador_na_mesa(self):
        self.__cartas_na_mesa += 1

        # Verificar fim de mesa
        if self.__cartas_na_mesa == 4:

            # Se sim computa vencedor da mesa e incrementa quantas fez
            self.computar_vencedor_mesa()
            self.incrementar_quantas_fez()
            self.limpar_cartas_jogadas()
            self.__terminou = True

        else:

            # Se nao passa para o proximo da mesa
            self.proximo_da_mesa()

    # Computar vencedor da mesa
    def computar_vencedor_mesa(self):
        for jogador in self.__jogadores:
            if self.__vencedor_da_mesa == None or jogador.get_carta_jogada().get_forca() >= self.__vencedor_da_mesa.get_carta_jogada().get_forca():
                self.__vencedor_da_mesa = jogador
            
            jogador.set_turno(False)
        print(f"Vencedor da mesa: {self.__vencedor_da_mesa.get_nome()}")
        self.__vencedor_da_mesa.set_turno(True)

    # Incrementar quantas fez
    def incrementar_quantas_fez(self):
        self.__vencedor_da_mesa.incrementar_quantas_fez()
    
    # Limpar cartas jogadas
    def limpar_cartas_jogadas(self):
        for jogador in self.__jogadores:
            jogador.set_carta_jogada(None)

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

    # Get fim mesa
    def terminou(self):
        return self.__terminou
