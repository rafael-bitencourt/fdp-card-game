from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from jogador import Jogador
from jogo import Jogo
from posicao import *

class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        # Atributos
        self.__nome = None
        self.__jogador_local = None
        self.__inicio_rodada = TRUE
        self.__posicoes = []
        self.__jogo = None
        self.__jogadores = []
        self.__posicoes = []
        self.__dog_server_interface = None

        # Inicializa a interface
        self.inicializar()


    def inicializar(self):
        # Criando a janela
        self.__janela = Tk()
        self.__janela.geometry("1012x759")
        self.__janela.resizable(False, False)
        self.__janela.title("Interface Filho da Puta")
        self.__icone = PhotoImage(file='assets/icone.png')
        self.__janela.iconphoto(True, self.__icone)

        # Configurando a imagem de fundo
        self.__mesa = PhotoImage(file="assets/mesa.png")
        self.__label_mesa = Label(self.__janela, image=self.__mesa)
        self.__label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

        # Criação texto pedindo nome
        self.__texto = Label(self.__janela, text="Digite seu nome:", font=('Helvetica', 15), bg='white', fg='black')
        self.__texto.pack(pady=20)
        self.__texto.place(x=430, y=225)

        # Criação do Entry
        self.__entrada = Entry(self.__janela, font=('Helvetica', 12), width=20)
        self.__entrada.pack(pady=20)
        self.__entrada.place(x=415, y=275)

        # Criando e configurando o botão conectar ao servidor
        self.__botao_conectar = Button(self.__janela, text="Conectar ao servidor", command=self.conectar_servidor)
        self.__botao_conectar.pack(pady=20, ipadx=10, ipady=5)
        self.__botao_conectar.place(x=445, y=455)

        # Criando e configurando o botão iniciar partida
        self.__botao_iniciar = Button(self.__janela, text="Iniciar partida", command=self.start_match)
        self.__botao_iniciar.pack(pady=20, ipadx=10, ipady=5)
        self.__botao_iniciar.place(x=465, y=505)

        #Loop principal
        self.__janela.mainloop()


    def conectar_servidor(self):
        # Verifica se o nome foi inserido
        self.__nome = self.__entrada.get()
        if self.__nome == "":
            messagebox.showinfo("Mensagem", "Digite um nome")
            return
        
        # Conecta ao servidor
        self.__dog_server_interface = DogActor()
        mensagem = self.__dog_server_interface.initialize(self.__nome, self)

        # Verifica se o nome foi inserido
        if self.__nome == "":
            messagebox.showinfo("Mensagem", "Digite um nome")
            return

        # Retorna a mensagem recebida
        messagebox.showinfo("Mensagem", mensagem)

        # Verifica sucesso na conexão
        if mensagem == "Conectado a Dog Server":
            self.__botao_conectar["state"] = "disabled"
            self.__botao_conectar["text"] = "Aguardando oponente"
            self.__botao_conectar.place(x=440, y=455)


    def start_match(self):
        # Verifica se o jogador está conectado
        if self.__dog_server_interface == None:
            messagebox.showinfo("Mensagem", "Conecte ao servidor primeiro")
            return

        # Verifica quantidade de jogadores conectados
        start_status = self.__dog_server_interface.start_match(2)
        mensagem = start_status.get_message()

        # Retorna a mensagem recebida
        messagebox.showinfo("Mensagem", mensagem)

        # Verifica sucesso na inicialização da partida
        if start_status.code != '2':
            return

        self.__botao_iniciar.destroy()
        self.__botao_conectar.destroy()
        self.__entrada.destroy()
        self.__texto.destroy()

        # Transforma lista de players do DogServer em Jogaodres
        players_start_status = start_status.get_players()
        for player in players_start_status:
            novo_jogador = Jogador(player)
            if novo_jogador.get_nome() == self.__nome:
                self.__jogador_local = novo_jogador
            if novo_jogador.get_indice() == 1:
                novo_jogador.set_turno(TRUE)
            self.__jogadores.append(novo_jogador)

        # Instancia o jogo
        self.__jogo = Jogo(self.__jogadores, self.__jogador_local)

        # Cria as posições dos jogadores
        for jogador in self.__jogadores:
            if jogador.get_indice() == self.__jogador_local.get_indice():
                self.__posicoes.append(PosicaoBaixo(jogador, self.__janela))
            elif jogador.get_indice() == (self.__jogador_local.get_indice() + 1) % 4:
                self.__posicoes.append(PosicaoDireita(jogador, self.__janela))
            elif jogador.get_indice() == (self.__jogador_local.get_indice() + 2) % 4:
                self.__posicoes.append(PosicaoCima(jogador, self.__janela))
            elif jogador.get_indice() == (self.__jogador_local.get_indice() + 3) % 4:
                self.__posicoes.append(PosicaoEsquerda(jogador, self.__janela))

        # Botão de atualizar interface para testes
        self.botao = Button(self.__janela, text="atualizar", command=self.atualizar_interface)
        self.botao.place(x=0, y=0)

        # Atualiza a interface
        self.atualizar_interface()

        # Muda a cor e espera atualização
        for posicao in self.__posicoes:
            posicao.cor = "white"

    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        if message == "Partida iniciada":
            self.imprime_elementos_mesa()
            self.__botao_iniciar.destroy()
            players = start_status.get_players()
            print(players)

        
    def receive_move(self, a_move):
        print(f"O jogador jogou.")


    def receive_withdrawal_notification(self):
        print("O jogador desistiu do jogo")
        

    def atualizar_interface(self):
        for posicao in self.__posicoes:
            posicao.atualizar_frame()


    def imprime_elementos_mesa(self):
        #Configurando a imagem de fundo
        self.__mesa = PhotoImage(file="assets/mesa-interface.png")
        self.__label_mesa = Label(self.__janela, image=self.__mesa)
        self.__label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

        #Configurando jogar_carta
        self.__imagem_carta_1 = ImageTk.PhotoImage(Image.open("assets/cartas/K paus.png"))
        self.__imagem_carta_2 = ImageTk.PhotoImage(Image.open("assets/cartas/Q copas.png"))
        self.__imagem_carta_3 = ImageTk.PhotoImage(Image.open("assets/cartas/6 paus.png"))

        self.__carta_1 = Button(self.__janela, command=lambda: self.imprimir_carta(1), width=70, height=100, image=self.__imagem_carta_1, bd=3)
        self.__carta_2 = Button(self.__janela, command=lambda: self.imprimir_carta(2), width=70, height=100, image=self.__imagem_carta_2, bd=3)
        self.__carta_3 = Button(self.__janela, command=lambda: self.imprimir_carta(3), width=70, height=100, image=self.__imagem_carta_3, bd=3)
        
        self.__carta_1.place(x=360, y=644)
        self.__carta_2.place(x=491, y=644)
        self.__carta_3.place(x=621, y=644)


    def imprimir_carta(self, carta):
        if carta == 1:
            self.__carta_1.place(x=621, y=450)
            self.__carta_2["state"] = "disabled"
            self.__carta_3["state"] = "disabled"
        elif carta == 2:
            self.__carta_2.place(x=621, y=450)
            self.__carta_1["state"] = "disabled"
            self.__carta_3["state"] = "disabled"
        elif carta == 3:
            self.__carta_3.place(x=621, y=450)
            self.__carta_1["state"] = "disabled"
            self.__carta_2["state"] = "disabled"