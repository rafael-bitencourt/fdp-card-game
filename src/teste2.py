from tkinter import *
from tkinter import PhotoImage
from jogador import Jogador
from baralho import Baralho

# Inicializando o baralho e o jogador
baralho = Baralho()
baralho.embaralhar()
jogador1 = Jogador(["Jogador 1", 1, 100])
jogador1.set_cartas_jogador(baralho.retirar_cartas(7))


# Configuração da janela principal
janela = Tk()
janela.geometry("1012x759")
janela.resizable(False, False)
janela.title("Interface Filho da Puta")
icone = PhotoImage(file='assets/icone.png')
janela.iconphoto(True, icone)
mesa = PhotoImage(file="assets/mesa-interface.png")
label_mesa = Label(janela, image=mesa)
label_mesa.place(x=0, y=0, relwidth=1, relheight=1)


# Dicionários para armazenar imagens e botões das cartas
imagens_cartas = {}
botoes_cartas = {}
carta_na_mesa = None  


# Carrega as imagens das cartas iniciais do jogador
for carta in jogador1.get_cartas_jogador():
    path = f"assets/cartas/{carta.get_valor()} {carta.get_naipe()}.png"
    imagens_cartas[carta] = PhotoImage(file=path)


# Função para jogar uma carta
def jogar_carta(carta):
    global carta_na_mesa  # Permite modificar a variável global
    jogador1.jogar_carta(carta)
    # Se já existe uma carta na mesa, removê-la
    if carta_na_mesa:
        carta_na_mesa.destroy()
    
    # Exibe a nova carta na mesa
    img_carta_jogada = imagens_cartas[carta]
    carta_na_mesa = Label(janela, image=img_carta_jogada)
    carta_na_mesa.place(x=480, y=490)  # Posiciona a carta na mesa (ajustar x e y conforme necessário)

    # Remove o botão da carta jogada
    botao = botoes_cartas.pop(carta)
    botao.destroy()  # Desabilita o botão
    print(f"Carta jogada: {jogador1.get_carta_jogada().get_valor()} de {jogador1.get_carta_jogada().get_naipe()}")
    print(f"Cartas restantes: {[carta.get_valor() for carta in jogador1.get_cartas_jogador()]}")
    
    # Atualiza a posição das cartas restantes
    atualizar_posicao_cartas()

# Função para atualizar a posição das cartas
def atualizar_posicao_cartas():
    largura_janela = 1012
    largura_carta = 55
    n = len(botoes_cartas)
    x_inicial = (largura_janela - (n * largura_carta)) / 2
    for i, (carta, botao) in enumerate(botoes_cartas.items()):
        x = x_inicial + i * largura_carta
        botao.place(x=x, y=664)

# Criar e posicionar os botões das cartas iniciais
for carta, img in imagens_cartas.items():
    botao = Button(janela, image=img, command=lambda carta=carta: jogar_carta(carta))
    botoes_cartas[carta] = botao
    botao.pack()

# Inicializa a posição das cartas
atualizar_posicao_cartas()

janela.mainloop()
