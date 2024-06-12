from tkinter import Frame

class Posicao:
    def __init__(self, jogador, janela):
        self._frame = None
        self._jogador = jogador
        self._janela = janela
        self._total_pontos = jogador.get_total_pontos()
        self._quantas_disse = jogador.get_quantas_disse()
        self._quantas_fez = jogador.get_quantas_fez()
        self._cartas_jogador = jogador.get_cartas_jogador()
        self._carta_jogada = jogador.get_carta_jogada()
    
    def atualizar_frame(self):
        pass

class PosicaoBaixo(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self.cor = "red"

    def atualizar_frame(self):
        self._frame = Frame(self._janela, bg=self.cor, width=200, height=200)
        self._frame.place(x=400, y=400)

class PosicaoDireita(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self.cor = "blue"

    def atualizar_frame(self):
        self._frame = Frame(self._janela, bg=self.cor, width=200, height=200)
        self._frame.place(x=600, y=200)
    
class PosicaoCima(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self.core = "green"

    def atualizar_frame(self):
        self._frame = Frame(self._janela, bg=self.cor, width=200, height=200)
        self._frame.place(x=400, y=0)

class PosicaoEsquerda(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self.cor = "yellow"

    def atualizar_frame(self):
        self._frame = Frame(self._janela, bg=self.cor, width=200, height=200)
        self._frame.place(x=200, y=200)