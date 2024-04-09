from tkinter import *
from PIL import Image, ImageTk

def quantas_faz(pontos):

    label_quadrado_verde.place(x=320, y=445)

    if pontos == 0:
        label_zero_pontos.place(x=845, y=649)
    elif pontos == 2:
        label_dois_pontos.place(x=845, y=649)
    elif pontos == 3:
        label_tres_pontos.place(x=845, y=649)

    carta_1.place(x=360, y=644)
    carta_2.place(x=491, y=644)
    carta_3.place(x=621, y=644)

def jogar_carta(carta):
    if carta == 1:
        print("Joguei a carta", carta)
    if carta == 2:
        print("Joguei a carta", carta)
    if carta == 3:
        print("Joguei a carta", carta)

#Crianddo a janela principal
janela = Tk()
janela.geometry("1012x759")
janela.title("Interface Filho da Puta")

#Configurando a imagem de fundo
mesa = PhotoImage(file="interface/assets/mesa-interface.png")
label_mesa = Label(janela, image=mesa)
label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

#Configurando quantas_faz
faco_0 = Button(janela, command=lambda: quantas_faz(0), height=2, width=4)
faco_2 = Button(janela, command=lambda: quantas_faz(2), height=2, width=4)
faco_3 = Button(janela, command=lambda: quantas_faz(3), height=2, width=4)

faco_0.place(x=419, y=524)
faco_2.place(x=519, y=524)
faco_3.place(x=569, y=524)

#Configurando jogar_carta
carta_1 = Button(janela, command=lambda: jogar_carta(1), height=6, width=9)
carta_2 = Button(janela, command=lambda: jogar_carta(2), height=6, width=9)
carta_3 = Button(janela, command=lambda: jogar_carta(3), height=6, width=9)

#Configurando imagens
quadrado_verde = ImageTk.PhotoImage(Image.open("interface/assets/quadrado-verde.png"))
label_quadrado_verde = Label(janela, image=quadrado_verde, bd=0)

zero_pontos = ImageTk.PhotoImage(Image.open("interface/assets/0-pontos.png"))
dois_pontos = ImageTk.PhotoImage(Image.open("interface/assets/2-pontos.png"))
tres_pontos = ImageTk.PhotoImage(Image.open("interface/assets/3-pontos.png"))

label_zero_pontos = Label(janela, image=zero_pontos, bd=0)
label_dois_pontos = Label(janela, image=dois_pontos, bd=0)
label_tres_pontos = Label(janela, image=tres_pontos, bd=0)

#Loop principal
janela.mainloop()