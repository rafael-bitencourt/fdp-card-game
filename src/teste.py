import tkinter as tk
from tkinter import PhotoImage
from jogador import Jogador
from baralho import Baralho

baralho = Baralho()
baralho.embaralhar()

jogador1 = Jogador(["Jogador 1", 1, 100])
jogador1.set_cartas_jogador(baralho.retirar_cartas(5))

root = tk.Tk()

imagens_cartas = {}  # Dicionário para armazenar as PhotoImages
botoes_cartas = {}   # Dicionário para armazenar os botões de cada carta

for carta in jogador1.get_cartas_jogador():
    path = f"assets/cartas/{carta.get_valor()} {carta.get_naipe()}.png"
    imagens_cartas[carta] = PhotoImage(file=path)


def jogar_carta(carta):
    jogador1.jogar_carta(carta)
    # Desabilitar o botão da carta jogada
    botao = botoes_cartas[carta]
    botao.destroy()  # Desabilita o botão
    print(f"Carta jogada: {jogador1.get_carta_jogada().get_valor()} de {jogador1.get_carta_jogada().get_naipe()}")
    print(f"Cartas restantes: {[carta.get_valor() for carta in jogador1.get_cartas_jogador()]}")


for carta, img in imagens_cartas.items():
    botao = tk.Button(root, image=img, command=lambda carta=carta: jogar_carta(carta))
    botao.pack()
    botoes_cartas[carta] = botao  # Armazena o botão na tabela de correspondência

root.mainloop()
