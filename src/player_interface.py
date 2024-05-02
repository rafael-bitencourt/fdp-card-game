from tkinter import *
from PIL import Image, ImageTk

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from jogador import Jogador

class PlayerInterface(DogPlayerInterface):
    def __init__(self, jogador):

        #Crianddo a janela principal
        self.__janela = Tk()
        self.__janela.geometry("1012x759")
        self.__janela.resizable(False, False)
        self.__janela.title("Interface Filho da Puta")
        self.__icone = PhotoImage(file='assets/icone.png')
        self.__janela.iconphoto(True, self.__icone)


        #Configurando a imagem de fundo
        self.__mesa = PhotoImage(file="assets/mesa-interface.png")
        self.__label_mesa = Label(self.__janela, image=self.__mesa)
        self.__label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

        #Configurando jogar_carta
        self.__imagem_carta_1 = ImageTk.PhotoImage(Image.open("assets/carta-1.png"))
        self.__imagem_carta_2 = ImageTk.PhotoImage(Image.open("assets/carta-2.png"))
        self.__imagem_carta_3 = ImageTk.PhotoImage(Image.open("assets/carta-3.png"))

        self.__carta_1 = Button(self.__janela, command=lambda: self.jogar_carta(1), width=73, height=102, image=self.__imagem_carta_1, bd=3)
        self.__carta_2 = Button(self.__janela, command=lambda: self.jogar_carta(2), width=73, height=102, image=self.__imagem_carta_2, bd=3)
        self.__carta_3 = Button(self.__janela, command=lambda: self.jogar_carta(3), width=73, height=102, image=self.__imagem_carta_3, bd=3)
        
        self.__carta_1.place(x=360, y=644)
        self.__carta_2.place(x=491, y=644)
        self.__carta_3.place(x=621, y=644)

        #Loop principal
        self.__janela.mainloop()

        #Interface com DogActor
        self.__jogador = jogador
        self.dog_server_interface = DogActor()
        mensagem = self.dog_server_interface.initialize(self.__jogador.get_nome(), self)
        print(mensagem)

    def jogar_carta(self, carta):
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

    def receive_start(self, start_status):
        print(f"O jogo começou.")
    
    def receive_move(self, a_move):
        print(f"O jogador jogou.")
    
    def receive_withdrawal_notification(self):
        print("O jogador desistiu do jogo")
    