from player_interface import PlayerInterface
from jogador import Jogador

def main():
    jogador1 = Jogador(input('Digite o nome do jogador: '))
    playerInterface = PlayerInterface(jogador1)

main()