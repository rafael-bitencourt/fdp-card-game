from tkinter import *

class Posicao:
    def __init__(self, player_interface, jogador):
        # Atributos imutáveis
        self._jogador = jogador
        self._player_interface = player_interface
        self._janela = player_interface.get_janela()

        # Dicionário de imagens das cartas
        self._imagens_cartas = {}
        naipes = ["copas", "espadas", "ouros", "paus"]
        valores = ["A", "3", "2", "K", "Q", "J", "7", "6", "5", "4"]
        for valor in valores:
            for naipe in naipes:
                path = f"assets/cartas/{valor} {naipe}.png"
                self._imagens_cartas[f"{valor} {naipe}"] = PhotoImage(file=path)
        self._imagens_cartas["verso"] = PhotoImage(file="assets/cartas/verso.png")
        self._imagens_cartas["verso de lado"] = PhotoImage(file="assets/cartas/verso de lado.png")

        # Atributos mutáveis
        self._label_total_pontos = None
        self._label_quantas_disse = None
        self._label_quantas_fez = None
        self._label_carta_jogada = None
        self._botoes_cartas_jogador = {}
    
    def atualizar_posicao(self):
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
        # Imprime label do total de pontos
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 34), bg="#D9D9D9")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=932, y=664)
        else:
            self._label_total_pontos.place(x=919, y=664)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_disse.place(x=846, y=645)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_fez.place(x=846, y=702)

        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[str(self._carta_jogada)])
            self._label_carta_jogada.place(x=470, y=465)
        
        # Cria botoes das cartas do jogador
        for carta in self._cartas_jogador:
            botao = Button(self._janela , image=self._imagens_cartas[str(carta)], command=lambda jogador=self._player_interface.get_jogador_local(), carta=carta: self._player_interface.jogar_carta(jogador, carta))
            self._botoes_cartas_jogador[str(carta)] = botao

        # Estado dos botoes
        estado = "normal" if self._jogador.get_turno() else "disabled"

        # Imprime os botoes centralizados
        largura_janela = 990
        largura_carta = 55
        n = len(self._botoes_cartas_jogador)
        x_inicial = (largura_janela - (n * largura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            x = x_inicial + i * largura_carta
            botao["state"] = estado
            botao.place(x=x, y=635)


class PosicaoDireita(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)

    def imprimir_elementos(self):
        # Imprime label do total de pontos
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 34), bg="#D9D9D9")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=933, y=41)
        else:
            self._label_total_pontos.place(x=920, y=41)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_disse.place(x=945, y=124)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_fez.place(x=945, y=181)

        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso de lado"], height=60, width=90)
            self._botoes_cartas_jogador[str(carta)] = label

        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[str(self._carta_jogada)])
            self._label_carta_jogada.place(x=630, y=325)
    
        # Imprime os labels centralizados
        altura_janela = 850
        altura_carta = 55
        n = len(self._botoes_cartas_jogador)
        y_inicial = (altura_janela - (n * altura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            y = y_inicial + i * altura_carta
            botao.place(x=870, y=y)


class PosicaoCima(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)

    def imprimir_elementos(self):
        # Imprime label do total de pontos
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 34), bg="#D9D9D9")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=54, y=41)
        else:
            self._label_total_pontos.place(x=41, y=41)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_disse.place(x=250, y=19)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_fez.place(x=250, y=76)

        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso de lado"], height=60, width=90)
            self._botoes_cartas_jogador[str(carta)] = label

        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[str(self._carta_jogada)])
            self._label_carta_jogada.place(x=470, y=180)

        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso"], height=90, width=60)
            self._botoes_cartas_jogador[str(carta)] = label
    
        # Imprime os labels centralizados
        largura_janela = 1020
        largura_carta = 55
        n = len(self._botoes_cartas_jogador)
        x_inicial = (largura_janela - (n * largura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            x = x_inicial + i * largura_carta
            botao.place(x=x, y=20)


class PosicaoEsquerda(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)

    def imprimir_elementos(self):
        # Imprime label do total de pontos
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 34), bg="#D9D9D9")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=52, y=669)
        else:
            self._label_total_pontos.place(x=39, y=669)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_disse.place(x=140, y=544)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 21), bg="#D9D9D9")
        self._label_quantas_fez.place(x=140, y=601)

        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[str(self._carta_jogada)])
            self._label_carta_jogada.place(x=300, y=325)

        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso de lado"], height=60, width=90)
            self._botoes_cartas_jogador[str(carta)] = label
    
        # Imprime os labels centralizados
        altura_janela = 650
        altura_carta = 55
        n = len(self._botoes_cartas_jogador)
        y_inicial = (altura_janela - (n * altura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            y = y_inicial + i * altura_carta
            botao.place(x=50, y=y)