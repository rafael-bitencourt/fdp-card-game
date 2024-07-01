from baralho import Baralho
from tkinter import *

class Posicao:
    def __init__(self, player_interface, jogador):
        # Atributos imutáveis
        self._jogador = jogador
        self._player_interface = player_interface
        self._janela = player_interface.get_janela()

        # Dicionário de imagens das cartas
        self._imagens_cartas = {}
        cartas = Baralho().get_cartas()
        for carta in cartas:
            path = f"assets/cartas/{carta.get_nome()}.png"
            self._imagens_cartas[carta.get_nome()] = PhotoImage(file=path)
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

        if self._player_interface.get_placar():
            placar = self._player_interface.get_placar()
            for i in range(4):
                if placar[i][0] == self._jogador.get_nome():
                    text = f"({placar[i][1]}pts) {placar[i][0]}"
                    self._label_colocacao = Label(self._janela, text=text, font=("Arial", 18, "bold"), bg="#D9D9D9", fg="#782359")
                    self._label_colocacao.place(x=519, y=329 + 47 * i, anchor="center")
                
        # Atualiza elementos da interface
        else:
            self.imprimir_elementos()

    def imprimir_elementos(self):
        pass


class PosicaoBaixo(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)
        # Imagens do menu quantas disse
        self._imagem_menu_quantas_disse = PhotoImage(file="assets/menu_quantas_disse.png")
        self._label_menu_quantas_disse = None
        self._imagens_botoes_quantas_disse = []
        for i in range (8):
            self._imagens_botoes_quantas_disse.append(PhotoImage(file=f"assets/botoes/diz_{i}.png"))
        self._botoes_quantas_disse = []
        
    def imprimir_elementos(self):
        # Imprime label do total de pontos
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 31, "bold"), bg="#D9D9D9", fg="#782359")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=934, y=666)
        else:
            self._label_total_pontos.place(x=922, y=664)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_disse.place(x=846, y=645)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_fez.place(x=846, y=702)

        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[self._carta_jogada.get_nome()])
            self._label_carta_jogada.place(x=470, y=465)
        
        # Cria botoes das cartas do jogador
        for carta in self._cartas_jogador:
            botao = Button(self._janela , image=self._imagens_cartas[carta.get_nome()], command=lambda jogador=self._player_interface.get_jogador_local(), carta=carta: self._player_interface.jogar_carta(jogador, carta))
            self._botoes_cartas_jogador[carta.get_nome()] = botao

        # Estado dos botoes
        if self._jogador.get_turno() and not self._player_interface.get_inicio_de_rodada():
            estado = "normal" 
        else:
            estado = "disabled"

        # Imprime os botoes centralizados
        largura_janela = 990
        largura_carta = 55
        n = len(self._botoes_cartas_jogador)
        x_inicial = (largura_janela - (n * largura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            x = x_inicial + i * largura_carta
            botao["state"] = estado
            botao.place(x=x, y=635)

        # Exclui menu_quantas_disse
        if self._label_menu_quantas_disse:
            self._label_menu_quantas_disse.destroy()
        if self._botoes_quantas_disse:
            for botao in self._botoes_quantas_disse:
                botao.destroy()
        self._botoes_quantas_disse = []

        # Imprime menu_quantas_disse
        if self._jogador.get_turno() and self._player_interface.get_inicio_de_rodada():
            self._label_menu_quantas_disse = Label(self._janela, image=self._imagem_menu_quantas_disse, borderwidth=0)
            self._label_menu_quantas_disse.place(x=280, y=245)

            num_botoes = len(self._jogador.get_cartas_jogador()) + 1
            largura_janela = 1012  # Largura da janela
            largura_botao = 50     # Largura de cada botão
            espacamento = 10       # Espaço adicional entre os botões, se necessário

            # Calcula a largura total ocupada pelos botões e o espaçamento entre eles
            largura_total_botoes = num_botoes * largura_botao + (num_botoes - 1) * espacamento
        
            # Calcula a posição x inicial para centralizar os botões
            x_inicial = (largura_janela - largura_total_botoes) // 2

            for i in range(num_botoes):
                self._imagens_botoes_quantas_disse.append(PhotoImage(file=f"assets/botoes/diz_{i}.png"))
                botao = Button(self._janela, image=self._imagens_botoes_quantas_disse[i], command=lambda jogador=self._jogador, i=i: self._player_interface.diz_quantas_faz(jogador, i), borderwidth=0, highlightthickness=0)
                self._botoes_quantas_disse.append(botao)

                if i == self._player_interface.get_botao_bloqueado():
                    botao["state"] = "disabled"

                # Calcula a posição x para cada botão
                pos_x = x_inicial + i * (largura_botao + espacamento)
                botao.place(x=pos_x, y=440)


class PosicaoDireita(Posicao):
    def __init__(self, player_interface, jogador):
        super().__init__(player_interface, jogador)

    def imprimir_elementos(self):
        # Imprime label do total de pontos
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 31, "bold"), bg="#D9D9D9", fg="#782359")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=933, y=43)
        else:
            self._label_total_pontos.place(x=923, y=41)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_disse.place(x=945, y=124)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_fez.place(x=945, y=181)

        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso de lado"], height=60, width=90)
            self._botoes_cartas_jogador[carta.get_nome()] = label

        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[self._carta_jogada.get_nome()])
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
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 31, "bold"), bg="#D9D9D9", fg="#782359")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=54, y=42)
        else:
            self._label_total_pontos.place(x=43, y=41)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_disse.place(x=250, y=19)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_fez.place(x=250, y=76)

        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso"], height=90, width=60)
            self._botoes_cartas_jogador[carta.get_nome()] = label
        
        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[self._carta_jogada.get_nome()])
            self._label_carta_jogada.place(x=470, y=180)

    
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
        self._label_total_pontos = Label(self._janela, text=str(self._total_pontos), font=("Arial", 31, "bold"), bg="#D9D9D9", fg="#782359")
        if self._total_pontos < 10:
            self._label_total_pontos.place(x=53, y=671)
        else:
            self._label_total_pontos.place(x=42, y=669)

        # Imprime label de quantas disse
        self._label_quantas_disse = Label(self._janela, text=str(self._quantas_disse), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_disse.place(x=140, y=544)

        # Imprime label de quantas fez
        self._label_quantas_fez = Label(self._janela, text=str(self._quantas_fez), font=("Arial", 20, "bold"), bg="#D9D9D9", fg="#782359")
        self._label_quantas_fez.place(x=140, y=601)

        # Cria labels das cartas do jogador
        for carta in self._cartas_jogador:
            label = Label(self._janela, image=self._imagens_cartas["verso de lado"], height=60, width=90)
            self._botoes_cartas_jogador[carta.get_nome()] = label
        
        # Imprime label da carta jogada
        if self._carta_jogada:
            self._label_carta_jogada = Label(self._janela, image=self._imagens_cartas[self._carta_jogada.get_nome()])
            self._label_carta_jogada.place(x=300, y=325)
    
        # Imprime os labels centralizados
        altura_janela = 650
        altura_carta = 55
        n = len(self._botoes_cartas_jogador)
        y_inicial = (altura_janela - (n * altura_carta)) / 2
        for i, (carta, botao) in enumerate(self._botoes_cartas_jogador.items()):
            y = y_inicial + i * altura_carta
            botao.place(x=50, y=y)