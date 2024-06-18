from tkinter import *

class Posicao:
    def __init__(self, player_interface, jogador):
        # Atributos imutáveis
        self._jogador = jogador
        self._player_interface = player_interface
        self._janela = player_interface.get_janela()

        # Dicionário de imagens das cartas
        self._imagens_cartas = {}
        self._imagens_cartas["verso"] = PhotoImage(file="assets/cartas/verso.png")
        naipes = ["copas", "espadas", "ouros", "paus"]
        valores = ["A", "3", "2", "K", "Q", "J", "7", "6", "5", "4"]
        for valor in valores:
            for naipe in naipes:
                path = f"assets/cartas/{valor} {naipe}.png"
                self._imagens_cartas[f"{valor} {naipe}"] = PhotoImage(file=path)

        # Atributos mutáveis
        self._label_total_pontos = None
        self._label_quantas_disse = None
        self._label_quantas_fez = None
        self._label_carta_jogada = None
        self._botoes_cartas_jogador = {}
    
    def atualizar_interface(self):
        # Atributos do jogador
        self._total_pontos = self._jogador.get_total_pontos()
        self._quantas_disse = self._jogador.get_quantas_disse()
        self._quantas_fez = self._jogador.get_quantas_fez()
        self._carta_jogada = self._jogador.get_carta_jogada()
        self._cartas_jogador = self._jogador.get_cartas_jogador()

        # Exclui elementos antigos
        if self._label_total_pontos:
            self._label_total_pontos.destroy()
        if self._label_quantas_disse:
            self._label_quantas_disse.destroy()
        if self._label_quantas_fez:
            self._label_quantas_fez.destroy()
        if self._label_carta_jogada:
            self._label_carta_jogada.destroy()
        if self._botoes_cartas_jogador:
            for carta, botao in self._botoes_cartas_jogador.items():
                botao.destroy()
        
        # Elementos da interface
        self._label_total_pontos = None
        self._label_quantas_disse = None
        self._label_quantas_fez = None
        self._label_carta_jogada = None
        self._botoes_cartas_jogador = {}

        # Atualiza elementos da interface
        self.imprimir_elementos()

    def imprimir_elementos(self):
        pass


class PosicaoBaixo(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)
        
    def imprimir_elementos(self):
        # Cria botoes das cartas do jogador
        for carta in self._cartas_jogador:
            botao = Button(self._janela , image=self._imagens_cartas[str(carta)], command=lambda carta=carta: self._player_interface.jogar_carta(carta))
            self._botoes_cartas_jogador[str(carta)] = botao
            botao.pack()

        # Imprime os botoes centralizados
        largura_janela = 990
        largura_carta = 55
        n = len(self._botoes_cartas_jogador)
        x_inicial = (largura_janela - (n * largura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            x = x_inicial + i * largura_carta
            botao.place(x=x, y=635)


class PosicaoDireita(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)


class PosicaoCima(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)

    def imprimir_elementos(self):
        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso"])
            self._botoes_cartas_jogador[str(carta)] = label
            label.pack()
    
        # Imprime os labels centralizados
        largura_janela = 990
        largura_carta = 55
        n = len(self._botoes_cartas_jogador)
        x_inicial = (largura_janela - (n * largura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            x = x_inicial + i * largura_carta
            botao.place(x=x, y=15)

class PosicaoEsquerda(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)