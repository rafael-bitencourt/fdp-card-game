from tkinter import *
from tkinter import messagebox
import time

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from jogador import Jogador
from carta import Carta
from jogo import Jogo
from posicao import *

class PlayerInterface(DogPlayerInterface):
    def __init__(self):

        # Atributos
        self.__nome = None
        self.__jogo = None
        self.__posicoes = []
        self.__jogadores = []
        self.__jogador_local = None
        self.__dog_server_interface = None
        self.__inicio_de_rodada = False
        self.__botao_bloqueado = None
        self.__placar = []
        self.__jogada = {}

        # Tela de inicio
        self.inicializar()
    

    # Caso de uso inicializar
    def inicializar(self):

        # Cria a janela
        self.__janela = Tk()
        self.__janela.geometry("1012x759")
        self.__janela.resizable(False, False)
        self.__janela.title("Filho da Puta")
        self.__icone = PhotoImage(file='assets/icone.png')
        self.__janela.iconphoto(True, self.__icone)

        # Configura a imagem de fundo
        self.__imagem_mesa = PhotoImage(file="assets/mesa.png")
        self.__label_mesa = Label(self.__janela, image=self.__imagem_mesa)
        self.__label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

        # Cria texto pedindo nome
        self.__texto = Label(self.__janela, text="Digite seu nome:", font=('Helvetica', 15), bg='white', fg='black')
        self.__texto.pack(pady=20)
        self.__texto.place(x=430, y=225)

        # Cria a entrada de texto
        self.__entrada = Entry(self.__janela, font=('Helvetica', 12), width=20)
        self.__entrada.pack(pady=20)
        self.__entrada.place(x=415, y=275)

        # Cria e configura o botão conectar ao servidor
        self.__botao_conectar = Button(self.__janela, text="Conectar ao servidor", command=self.conectar_servidor)
        self.__botao_conectar.pack(pady=20, ipadx=10, ipady=5)
        self.__botao_conectar.place(x=445, y=455)

        # Crian e configura o botão iniciar partida
        self.__botao_iniciar = Button(self.__janela, text="Iniciar partida", command=self.start_match)
        self.__botao_iniciar.pack(pady=20, ipadx=10, ipady=5)
        self.__botao_iniciar.place(x=465, y=505)

        #Loop principal
        self.__janela.mainloop()


    # Conecta ao DogServer
    def conectar_servidor(self):

        # Verifica se o nome foi inserido
        self.__nome = self.__entrada.get()
        if self.__nome == "":
            messagebox.showinfo("Mensagem", "Digite um nome")
            return
        
        # Inicia conexão com o DogServer
        self.__dog_server_interface = DogActor()
        mensagem = self.__dog_server_interface.initialize(self.__nome, self)

        # Retorna a mensagem recebida
        messagebox.showinfo("Mensagem", mensagem)

        # Verifica sucesso na conexão e desabilita botão de conectar
        if mensagem == "Conectado a Dog Server":
            self.__botao_conectar["state"] = "disabled"
            self.__botao_conectar["text"] = "Aguardando oponente"
            self.__botao_conectar.place(x=440, y=455)


    # Iniciar partida
    def start_match(self):

        # Verifica se o jogador está conectado
        if self.__dog_server_interface == None:
            messagebox.showinfo("Mensagem", "Conecte ao servidor primeiro")
            return

        # Verifica quantidade de jogadores conectados
        start_status = self.__dog_server_interface.start_match(4)
        mensagem = start_status.get_message()

        # Retorna a mensagem recebida
        messagebox.showinfo("Mensagem", mensagem)

        # Verifica sucesso na inicialização da partida
        if start_status.code != '2':
            return
        
        #Destroi elementos da tela de inicio
        self.__botao_iniciar.destroy()
        self.__botao_conectar.destroy()
        self.__entrada.destroy()
        self.__texto.destroy()

        # Recebe e ordena lista de players do DogServer
        players_start_status = start_status.get_players()
        players_start_status.sort(key=lambda x: int(x[2]))

        # Transforma lista de players do DogServer em Jogaodres
        for player in players_start_status:
            novo_jogador = Jogador(player)
            self.__jogadores.append(novo_jogador)

            # Identifica o jogador local
            if novo_jogador.get_nome() == self.__nome:
                self.__jogador_local = novo_jogador

        # Instancia o jogo
        self.__jogo = Jogo(self, self.__jogadores)

        # Cria e popula as posições dos jogadores
        for jogador in self.__jogadores:
            if jogador.get_indice() == self.__jogador_local.get_indice():
                self.__posicoes.append(PosicaoBaixo(self, jogador))
            elif jogador.get_indice() == (self.__jogador_local.get_indice() % 4 + 1):
                self.__posicoes.append(PosicaoDireita(self, jogador))
            elif jogador.get_indice() == ((self.__jogador_local.get_indice() + 1) % 4 + 1):
                self.__posicoes.append(PosicaoCima(self, jogador))
            elif jogador.get_indice() == ((self.__jogador_local.get_indice() + 2) % 4 + 1):
                self.__posicoes.append(PosicaoEsquerda(self, jogador))

        # Atualiza a interface
        self.atualizar_interface()


    # Receber início
    def receive_start(self, start_status):

        # Verifica se a partida iniciou corretamente
        mensagem = start_status.get_message()

        # Retorna a mensagem recebida
        messagebox.showinfo("Mensagem", mensagem)
        
        # Destroi elementos da tela
        self.__botao_iniciar.destroy()
        self.__botao_conectar.destroy()
        self.__entrada.destroy()
        self.__texto.destroy()

        # Recebe e ordena lista de players do DogServer
        players_start_status = start_status.get_players()
        players_start_status.sort(key=lambda x: int(x[2]))

        # Transforma lista de players do DogServer em Jogaodres
        for player in players_start_status:
            novo_jogador = Jogador(player)
            self.__jogadores.append(novo_jogador)

            # Identifica o jogador local
            if novo_jogador.get_nome() == self.__nome:
                self.__jogador_local = novo_jogador

        # Instancia o jogo
        self.__jogo = Jogo(self, self.__jogadores)

        # Cria e popula as posições dos jogadores
        for jogador in self.__jogadores:
            if jogador.get_indice() == self.__jogador_local.get_indice():
                self.__posicoes.append(PosicaoBaixo(self, jogador))
            elif jogador.get_indice() == (self.__jogador_local.get_indice() % 4 + 1):
                self.__posicoes.append(PosicaoDireita(self, jogador))
            elif jogador.get_indice() == ((self.__jogador_local.get_indice() + 1) % 4 + 1):
                self.__posicoes.append(PosicaoCima(self, jogador))
            elif jogador.get_indice() == ((self.__jogador_local.get_indice() + 2) % 4 + 1):
                self.__posicoes.append(PosicaoEsquerda(self, jogador))

        # Atualiza a interface
        self.atualizar_interface()


    # Jogar carta
    def jogar_carta(self, jogador, carta):

        # Adiciona carta jogada e remove carta da mao do jogador
        jogador.jogar_carta(carta)

        # Adiciona carta na mesa e na logica do jogo
        self.__jogo.jogar_carta()

        # Verifica se a partida acabou
        if self.__placar:

            # Imprime o fundo do placar
            self.imprimir_placar()

        # Atualiza a interface
        self.atualizar_interface()

        # Verifica foi o jogador local que jogou
        if jogador == self.__jogador_local:

            # Configura a jogada caso seja do jogador local
            self.__jogada["tipo"] = "jogar_carta"
            self.__jogada["carta"] = carta.get_nome()
            self.__jogada["jogador"] = jogador.get_nome()
            self.__jogada["match_status"] = "next"

            # Envia a jogada
            self.__dog_server_interface.send_move(self.__jogada)

            # Limpa a jogada
            self.__jogada = {}


    # Diz quantas faz
    def diz_quantas_faz(self, jogador, quantas_disse):

        # Atribui quantas disse ao jogador
        jogador.set_quantas_disse(quantas_disse)

        # Adiciona quantas disse na logica do jogo
        self.__jogo.diz_quantas_faz()

        # Atualiza a interface
        self.atualizar_interface()

        # Verifica se foi o jogador local que disse quantas faz
        if jogador == self.__jogador_local:

            # Configura a jogada caso seja do jogador local
            self.__jogada["tipo"] = "diz_quantas_faz"
            self.__jogada["quantas_disse"] = quantas_disse
            self.__jogada["jogador"] = jogador.get_nome()
            self.__jogada["match_status"] = "next"

            # Envia a jogada
            self.__dog_server_interface.send_move(self.__jogada)

            # Limpa a jogada
            self.__jogada = {}


    # Receber movimento
    def receive_move(self, a_move):

        # Verifica se uma carta foi jogada
        if a_move["tipo"] == "jogar_carta":

            # Identifica o jogador responsavel
            for jogador in self.__jogadores:
                if jogador.get_nome() == a_move["jogador"]:

                    # Identifica a carta jogada
                    for carta in jogador.get_cartas_jogador():
                        if carta.get_nome() == a_move["carta"]:

                            # Reutiliza a função jogar carta
                            self.jogar_carta(jogador, carta)
                            break

        # Verifica se um jogador disse quantas faz
        elif a_move["tipo"] == "diz_quantas_faz":

            # Identifica o jogador responsavel
            for jogador in self.__jogadores:
                if jogador.get_nome() == a_move["jogador"]:

                    # Reutiliza a função diz quantas faz
                    self.diz_quantas_faz(jogador, int(a_move["quantas_disse"]))

        # Verifica se um jogador distribuiu cartas
        elif a_move["tipo"] == "distribuir_cartas":

            # Percorre os jogadores
            for jogador in self.__jogadores:
                cartas = []
                strings_cartas = a_move[jogador.get_nome()]

                # Indentifica e cria as cartas a serem compradas
                for string in strings_cartas:
                    valor, naipe = string.split(" ")
                    cartas.append(Carta(valor, naipe))

                # Adiciona as cartas ao jogador
                jogador.set_cartas_jogador(cartas)

            # Atualiza a interface
            self.atualizar_interface()


    # Receber notificação de desistencia
    def receive_withdrawal_notification(self):

        # Exibe mensagem de desistencia
        messagebox.showinfo("Mensagem", "O oponente se desconectou")

        # Fecha a janela
        self.__janela.destroy()


    # Atualiza a interface atraves das posicoes
    def atualizar_interface(self):
        for posicao in self.__posicoes:
            posicao.atualizar_posicao()


    # Atualiza a interface com delay de 1,5 segundos para melhor visualização
    def atualizar_interface_com_delay(self):
        self.atualizar_interface()
        self.__janela.update()
        time.sleep(1.5)


    # Imprimir fundo do placar
    def imprimir_placar(self):
        self.__imagem_placar = PhotoImage(file="assets/placar.png")
        self.__label_placar = Label(self.__janela, image=self.__imagem_placar, borderwidth=0)
        self.__label_placar.place(x=286, y=225)


    # Enviar jogada (acessivel por outras classes)
    def enviar_jogada(self, jogada):
        self.__dog_server_interface.send_move(jogada)


    # Getters e Setters
    def get_janela(self):
        return self.__janela

    def get_jogador_local(self):
        return self.__jogador_local
    
    def get_inicio_de_rodada(self):
        return self.__inicio_de_rodada
    
    def set_inicio_de_rodada(self, inicio_de_rodada):
        self.__inicio_de_rodada = inicio_de_rodada

    def get_botao_bloqueado(self):
        return self.__botao_bloqueado
    
    def set_botao_bloqueado(self, botao_bloqueado):
        self.__botao_bloqueado = botao_bloqueado
    
    def get_placar(self):
        return self.__placar

    def set_placar(self, placar):
        self.__placar = placar