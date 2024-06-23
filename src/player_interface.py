from tkinter import *
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
        self.__jogo = None
        self.__posicoes = []
        self.__jogadores = []
        self.__jogador_local = None
        self.__dog_server_interface = None
        self.__inicio_de_rodada = False
        self.__botao_bloqueado = None
        self.__jogada = {}

        # Tela de inicio
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
        self.__imagem_mesa = PhotoImage(file="assets/mesa.png")
        self.__label_mesa = Label(self.__janela, image=self.__imagem_mesa)
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

        # NAO ESQUECER DE TIRAR NO FINAL
        self.__botao_teste = Button(self.__janela, text="Teste", command=self.teste)
        self.__botao_teste.pack(pady=20, ipadx=10, ipady=5)
        self.__botao_teste.place(x=485, y=555)
        # NAO ESQUECER DE TIRAR NO FINAL

        #Loop principal
        self.__janela.mainloop()


    # NAO ESQUECER DE TIRAR NO FINAL
    def teste(self):

        print("-> TESTE INICIADO")
        # Nome do jogador de teste
        self.__nome = "Jogador Local"
        
        #Destroi elementos da tela
        self.__botao_iniciar.destroy()
        self.__botao_conectar.destroy()
        self.__botao_teste.destroy()
        self.__entrada.destroy()
        self.__texto.destroy()

        # Transforma lista de players do DogServer em Jogaodres
        players_start_status = ["Jogador Local", "0000", "1"], ["Jogador X    ", "0000", "4"], ["Jogador Y    ", "0000", "2"], ["Jogador Z    ", "0000", "3"]

        for player in players_start_status:
            novo_jogador = Jogador(player)
            if novo_jogador.get_nome() == self.__nome:
                self.__jogador_local = novo_jogador
            self.__jogadores.append(novo_jogador)

        # Competencias de jogo
        self.__jogo = Jogo(self, self.__jogadores)

        # Cria as posições dos jogadores
        for jogador in self.__jogadores:
            if jogador.get_indice() == self.__jogador_local.get_indice():
                self.__posicoes.append(PosicaoBaixo(self, jogador))
            elif jogador.get_indice() == (self.__jogador_local.get_indice() % 4 + 1):
                self.__posicoes.append(PosicaoDireita(self, jogador))
            elif jogador.get_indice() == ((self.__jogador_local.get_indice() + 1) % 4 + 1):
                self.__posicoes.append(PosicaoCima(self, jogador))
            elif jogador.get_indice() == ((self.__jogador_local.get_indice() + 2) % 4 + 1):
                self.__posicoes.append(PosicaoEsquerda(self, jogador))

        # NAO ESQUECER DE TIRAR NO FINAL
        self.botao_proximo_joga_carta = Button(self.__janela, text="Proximo da mesa", command=self.proximo_joga_carta)
        self.botao_proximo_joga_carta.place(x=0, y=0)

        self.botao_proximo_diz_quantas_faz = Button(self.__janela, text="Proximo diz quantas faz", command=self.proximo_diz_quantas_faz)
        self.botao_proximo_diz_quantas_faz.place(x=100, y=0)
        # NAO ESQUECER DE TIRAR NO FINAL

        # Atualiza a interface
        self.atualizar_interface()

    # NAO ESQUECER DE TIRAR NO FINAL
    def proximo_joga_carta(self):
        for jogador in self.__jogadores:
            if jogador.get_turno() and jogador != self.__jogador_local:
                self.jogar_carta(jogador, jogador.get_cartas_jogador()[0])
                break

    def proximo_diz_quantas_faz(self):
        for jogador in self.__jogadores:
            if jogador.get_turno() and jogador != self.__jogador_local:
                self.diz_quantas_faz(jogador, 1)
                break


    def conectar_servidor(self):
        # Verifica se o nome foi inserido
        self.__nome = self.__entrada.get()
        if self.__nome == "":
            messagebox.showinfo("Mensagem", "Digite um nome")
            return
        
        # Conecta ao servidor
        self.__dog_server_interface = DogActor()
        mensagem = self.__dog_server_interface.initialize(self.__nome, self)

        # Retorna a mensagem recebida
        messagebox.showinfo("Mensagem", mensagem)

        # Verifica sucesso na conexão
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
        
        #Destroi elementos da tela
        self.__botao_iniciar.destroy()
        self.__botao_conectar.destroy()
        self.__entrada.destroy()
        self.__texto.destroy()

        # NAO ESQUECER DE TIRAR NO FINAL
        self.__botao_teste.destroy()
        # NAO ESQUECER DE TIRAR NO FINAL

        # NAO ESQUECER DE TIRAR NO FINAL
        self.botao_proximo_joga_carta = Button(self.__janela, text="Proximo da mesa", command=self.proximo_joga_carta)
        self.botao_proximo_joga_carta.place(x=0, y=0)

        self.botao_proximo_diz_quantas_faz = Button(self.__janela, text="Proximo diz quantas faz", command=self.proximo_diz_quantas_faz)
        self.botao_proximo_diz_quantas_faz.place(x=100, y=0)
        # NAO ESQUECER DE TIRAR NO FINAL

        # Transforma lista de players do DogServer em Jogaodres
        players_start_status = start_status.get_players()
        players_start_status.sort(key=lambda x: int(x[2]))
        for player in players_start_status:
            novo_jogador = Jogador(player)
            if novo_jogador.get_nome() == self.__nome:
                self.__jogador_local = novo_jogador
            self.__jogadores.append(novo_jogador)

        # Instancia o jogo
        self.__jogo = Jogo(self, self.__jogadores)

        # Cria as posições dos jogadores
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
        
        #Destroi elementos da tela
        self.__botao_iniciar.destroy()
        self.__botao_conectar.destroy()
        self.__entrada.destroy()
        self.__texto.destroy()

        # NAO ESQUECER DE TIRAR NO FINAL
        self.__botao_teste.destroy()
        # NAO ESQUECER DE TIRAR NO FINAL

        # NAO ESQUECER DE TIRAR NO FINAL
        self.botao_proximo_joga_carta = Button(self.__janela, text="Proximo da mesa", command=self.proximo_joga_carta)
        self.botao_proximo_joga_carta.place(x=0, y=0)

        self.botao_proximo_diz_quantas_faz = Button(self.__janela, text="Proximo diz quantas faz", command=self.proximo_diz_quantas_faz)
        self.botao_proximo_diz_quantas_faz.place(x=100, y=0)
        # NAO ESQUECER DE TIRAR NO FINAL

        # Transforma lista de players do DogServer em Jogaodres
        players_start_status = start_status.get_players()
        players_start_status.sort(key=lambda x: int(x[2]))
        for player in players_start_status:
            novo_jogador = Jogador(player)
            if novo_jogador.get_nome() == self.__nome:
                self.__jogador_local = novo_jogador
            self.__jogadores.append(novo_jogador)

        # Instancia o jogo
        self.__jogo = Jogo(self, self.__jogadores)

        # Cria as posições dos jogadores
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
        jogador.jogar_carta(carta)
        self.__jogo.jogar_carta()
        self.atualizar_interface()
        if jogador == self.__jogador_local:
            self.__jogada["tipo"] = "jogar_carta"
            self.__jogada["carta"] = str(carta)
            self.__jogada["jogador"] = jogador.get_nome()
            self.__jogada["match_status"] = "next"
            self.__dog_server_interface.send_move(self.__jogada)
            self.__jogada = {}

    # Diz quantas faz
    def diz_quantas_faz(self, jogador, quantas_disse):
        jogador.set_quantas_disse(quantas_disse)
        self.__jogo.diz_quantas_faz()
        self.atualizar_interface()
        if jogador == self.__jogador_local:
            self.__jogada["tipo"] = "diz_quantas_faz"
            self.__jogada["quantas_disse"] = quantas_disse
            self.__jogada["jogador"] = jogador.get_nome()
            self.__jogada["match_status"] = "next"
            self.__dog_server_interface.send_move(self.__jogada)
            self.__jogada = {}

    # Receber movimento
    def receive_move(self, a_move):
        if a_move["tipo"] == "jogar_carta":
            for jogador in self.__jogadores:
                if jogador.get_nome() == a_move["jogador"]:
                    for carta in jogador.get_cartas_jogador():
                        if str(carta) == a_move["carta"]:
                            self.jogar_carta(jogador, carta)
                            break

        elif a_move["tipo"] == "diz_quantas_faz":
            for jogador in self.__jogadores:
                if jogador.get_nome() == a_move["jogador"]:
                    self.diz_quantas_faz(jogador, int(a_move["quantas_disse"]))

        self.atualizar_interface()

    # Aviso de desconexão
    def receive_withdrawal_notification(self):
        messagebox.showinfo("Mensagem", "O oponente se desconectou")
        self.__janela.destroy()
        
    # Atualiza a interface
    def atualizar_interface(self):
        for posicao in self.__posicoes:
            posicao.atualizar_posicao()

    # Atualiza a interface com delay
    def atualizar_interface_com_delay(self):
        self.atualizar_interface()
        self.__janela.update()
        time.sleep(1.5)


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