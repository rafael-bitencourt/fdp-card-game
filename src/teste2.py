from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox
import time

def imprimir_carta():
    print("ta no inferno abaraca o perneta")

janela = Tk()
janela.geometry("1012x759")
janela.resizable(False, False)
janela.title("Interface Filho da Puta")
icone = PhotoImage(file='assets/icone.png')
janela.iconphoto(True, icone)

mesa = PhotoImage(file="assets/mesa-interface.png")
label_mesa = Label(janela, image=mesa)
label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

imagem_carta_1 = PhotoImage(file="assets/cartas/K paus.png")
imagem_carta_2 = PhotoImage(file="assets/cartas/Q copas.png")
imagem_carta_3 = PhotoImage(file="assets/cartas/A paus.png")
imagem_carta_4 = PhotoImage(file="assets/cartas/2 copas.png")
imagem_carta_5 = PhotoImage(file="assets/cartas/3 copas.png")
imagem_carta_6 = PhotoImage(file="assets/cartas/4 copas.png")
imagem_carta_7 = PhotoImage(file="assets/cartas/5 copas.png")
                            
carta_1 = Button(janela, command=lambda: imprimir_carta(), width=55, height=80, image=imagem_carta_1, bd=3)
carta_2 = Button(janela, command=lambda: imprimir_carta(), width=55, height=80, image=imagem_carta_2, bd=3)
carta_3 = Button(janela, command=lambda: imprimir_carta(), width=55, height=80, image=imagem_carta_3, bd=3)
carta_4 = Button(janela, command=lambda: imprimir_carta(), width=55, height=80, image=imagem_carta_4, bd=3)
carta_5 = Button(janela, command=lambda: imprimir_carta(), width=55, height=80, image=imagem_carta_5, bd=3)
carta_6 = Button(janela, command=lambda: imprimir_carta(), width=55, height=80, image=imagem_carta_6, bd=3)
carta_7 = Button(janela, command=lambda: imprimir_carta(), width=55, height=80, image=imagem_carta_7, bd=3)

carta_1.place(x=240, y=664)
carta_2.place(x=300, y=664)
carta_3.place(x=360, y=664)
carta_4.place(x=420, y=664)
carta_5.place(x=480, y=664)
carta_6.place(x=540, y=664)
carta_7.place(x=600, y=664)

janela.mainloop()
