from tkinter import *
from PIL import Image, ImageTk

def quantas_faz(pontos):
    
    if pontos != 1:

        label_quadrado_verde.place(x=310, y=450)

        if pontos == 0:
            label_disse_0.place(x=845, y=649)
        elif pontos == 2:
            label_disse_2.place(x=845, y=649)
        elif pontos == 3:
            label_disse_3.place(x=845, y=649)

        carta_1["state"] = "normal"
        carta_2["state"] = "normal"
        carta_3["state"] = "normal"

def jogar_carta(carta):
    
    if carta == 1:
        carta_1.place(x=621, y=450)
        carta_2["state"] = "disabled"
        carta_3["state"] = "disabled"
    elif carta == 2:
        carta_2.place(x=621, y=450)
        carta_1["state"] = "disabled"
        carta_3["state"] = "disabled"
    elif carta == 3:
        carta_3.place(x=621, y=450)
        carta_1["state"] = "disabled"
        carta_2["state"] = "disabled"

    label_off_1.place(x=903, y=647)
    label_on_2.place(x=903, y=22)

#Crianddo a janela principal
janela = Tk()
janela.geometry("1012x759")
janela.resizable(False, False)
janela.title("Interface Filho da Puta")

#Configurando a imagem de fundo
mesa = PhotoImage(file="assets/mesa-interface.png")
label_mesa = Label(janela, image=mesa)
label_mesa.place(x=0, y=0, relwidth=1, relheight=1)

#Configurando quantas_faz
imagem_botao_0 = ImageTk.PhotoImage(Image.open("assets/botao-0.png"))
imagem_botao_1 = ImageTk.PhotoImage(Image.open("assets/botao-1.png"))
imagem_botao_2 = ImageTk.PhotoImage(Image.open("assets/botao-2.png"))
imagem_botao_3 = ImageTk.PhotoImage(Image.open("assets/botao-3.png"))

botao_0 = Button(janela, command=lambda: quantas_faz(0), height=40, width=40, image=imagem_botao_0, bd=0, bg="#A5D744")
botao_1 = Button(janela, command=lambda: quantas_faz(1), height=40, width=40, image=imagem_botao_1, bd=0, bg="#A5D744")
botao_2 = Button(janela, command=lambda: quantas_faz(2), height=40, width=40, image=imagem_botao_2, bd=0, bg="#A5D744")
botao_3 = Button(janela, command=lambda: quantas_faz(3), height=40, width=40, image=imagem_botao_3, bd=0, bg="#A5D744")

botao_0.place(x=419, y=524)
botao_1.place(x=469, y=524)
botao_2.place(x=519, y=524)
botao_3.place(x=569, y=524)

#Configurando jogar_carta
imagem_carta_1 = ImageTk.PhotoImage(Image.open("assets/carta-1.png"))
imagem_carta_2 = ImageTk.PhotoImage(Image.open("assets/carta-2.png"))
imagem_carta_3 = ImageTk.PhotoImage(Image.open("assets/carta-3.png"))

carta_1 = Button(janela, command=lambda: jogar_carta(1), width=73, height=102, image=imagem_carta_1, bd=3, state="disabled")
carta_2 = Button(janela, command=lambda: jogar_carta(2), width=73, height=102, image=imagem_carta_2, bd=3, state="disabled")
carta_3 = Button(janela, command=lambda: jogar_carta(3), width=73, height=102, image=imagem_carta_3, bd=3, state="disabled")

carta_1.place(x=360, y=644)
carta_2.place(x=491, y=644)
carta_3.place(x=621, y=644)

#Configurando outros assets
quadrado_verde = ImageTk.PhotoImage(Image.open("assets/quadrado-verde.png"))
off_1 = ImageTk.PhotoImage(Image.open("assets/1-off.png"))
on_2 = ImageTk.PhotoImage(Image.open("assets/2-on.png"))

label_quadrado_verde = Label(janela, image=quadrado_verde, bd=0)
label_off_1 = Label(janela, image=off_1, bd=0)
label_on_2 = Label(janela, image=on_2, bd=0)

#Configurando disse
disse_0 = ImageTk.PhotoImage(Image.open("assets/disse-0.png"))
disse_2 = ImageTk.PhotoImage(Image.open("assets/disse-2.png"))
disse_3 = ImageTk.PhotoImage(Image.open("assets/disse-3.png"))

label_disse_0 = Label(janela, image=disse_0, bd=0)
label_disse_2 = Label(janela, image=disse_2, bd=0)
label_disse_3 = Label(janela, image=disse_3, bd=0)

#Loop principal
janela.mainloop()