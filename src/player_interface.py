from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from jogador import Jogador

class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        # Criando menu de inicio
        self.__janela = Tk()
        self.__janela.geometry("1012x759")
        self.__janela.resizable(False, False)
        self.__janela.title("Interface Filho da Puta")
        self.__icone = PhotoImage(file='assets/icone.png')
        self.__janela.iconphoto(True, self.__icone)

        self.__mesa = PhotoImage(file="assets/fundo.png")
        self.__label_mesa = Label(self.__janela, image=self.__mesa)
        self.__label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

        # Criação texto pedindo nome
        self.__texto = Label(self.__janela, text="Digite seu nome:", font=('Helvetica', 15), bg='white', fg='black')
        self.__texto.pack(pady=20)
        self.__texto.place(x=425, y=250)

        # Criando e configurando o botão conectar ao servidor
        self.start_button = Button(self.__janela, text="Conectar ao servidor", command=self.conectar_servidor)
        self.start_button.pack(pady=20, ipadx=10, ipady=5)
        self.start_button.place(x=420, y=350)

        # Criando e configurando o botão iniciar partida
        self.start_match_button = Button(self.__janela, text="Iniciar partida", command=self.start_match)
        self.start_match_button.pack(pady=20, ipadx=10, ipady=5)
        self.start_match_button.place(x=440, y=400)

        # Criação do Entry
        self.entry = Entry(self.__janela, font=('Helvetica', 12), width=20)
        self.entry.pack(pady=20)
        self.entry.place(x=410, y=300)

        #Loop principal
        self.__janela.mainloop()

    
    def conectar_servidor(self):
            self.__nome = self.entry.get()
            self.dog_server_interface = DogActor()
            mensagem = self.dog_server_interface.initialize(self.__nome, self)
            messagebox.showinfo("Mensagem", mensagem)
            if mensagem == "Conectado a Dog Server":
                self.start_button["state"] = "disabled"
                self.start_button["text"] = "Aguardando oponente"
    


    def imprime_elementos_mesa(self):
        #Configurando a imagem de fundo
        self.__mesa = PhotoImage(file="assets/mesa-interface.png")
        self.__label_mesa = Label(self.__janela, image=self.__mesa)
        self.__label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

        # Criando e configurando o botão iniciar partida
        # self.start_match_button = Button(self.__janela, text="Iniciar partida", command=self.start_match)
        # self.start_match_button.pack(pady=20, ipadx=10, ipady=5)
        # self.start_match_button.place(x=450, y=450)

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


    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo("Mensagem", message)
        if message == "Partida iniciada":
            self.imprime_elementos_mesa()
            self.start_match_button.destroy()
   

    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        if message == "Partida iniciada":
            self.imprime_elementos_mesa()
            self.start_match_button.destroy()

        
    def receive_move(self, a_move):
        print(f"O jogador jogou.")


    def receive_withdrawal_notification(self):
        print("O jogador desistiu do jogo")
    

playerInterface = PlayerInterface()