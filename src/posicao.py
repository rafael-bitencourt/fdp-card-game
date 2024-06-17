from tkinter import Frame

class Posicao:
    def __init__(self, jogador, janela):
        self._frame = None
        self._altura = 0
        self._largura = 0
        self._xframe = 0
        self._yframe = 0
        self._jogador = jogador
        self._janela = janela
        self._total_pontos = jogador.get_total_pontos()
        self._quantas_disse = jogador.get_quantas_disse()
        self._quantas_fez = jogador.get_quantas_fez()
        self._cartas_jogador = jogador.get_cartas_jogador()
        self._carta_jogada = jogador.get_carta_jogada()
        self.cor = "white"
    
    def atualizar_frame(self):
        self._frame = Frame(self._janela, bg=self.cor, width=self._altura, height=self._largura)
        self._frame.place(x=self._xframe , y=self._yframe)

class PosicaoBaixo(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self._largura = 200
        self._altura = 200
        self._xframe = 400
        self._yframe = 400
        self.cor = "red"

class PosicaoDireita(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self._largura = 200
        self._altura = 200
        self._xframe = 600
        self._yframe = 200
        self.cor = "blue"
    
class PosicaoCima(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self._largura = 200
        self._altura = 200
        self._xframe = 400
        self._yframe = 0
        self.core = "green"

class PosicaoEsquerda(Posicao):
    def __init__(self, jogador, janela):
        super().__init__(jogador, janela)
        self._largura = 200
        self._altura = 200
        self._xframe = 200
        self._yframe = 200
        self.cor = "yellow"