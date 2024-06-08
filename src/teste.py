from carta import Carta
import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()


imagens_cartas = {}  # Dicionário para armazenar as PhotoImages
lista_cartas = [Carta("A", "ouros"), Carta("K", "copas"), Carta("3", "espadas")]  # Lista de cartas

for carta in lista_cartas:
    path = f"assets/cartas/{carta.get_valor()} {carta.get_naipe()}.png"
    imagens_cartas[carta] = PhotoImage(file=path)

def acao_carta(carta):
    print(f"Carta clicada: {carta.get_valor()} de {carta.get_naipe()}")

for carta, img in imagens_cartas.items():
    botao = tk.Button(root, image=img, command=lambda c=carta: acao_carta(c))
    botao.pack()  

root.mainloop()
