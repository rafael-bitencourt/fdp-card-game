from src.carta import Carta
import random

class Baralho:
    def __init__(self):
        self.cartas = []
    

    def criar_baralho(self):
        naipes = ["copas", "espadas", "ouros", "paus"]
        valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for naipe in naipes:
            for valor in valores:
                self.cartas.append(Carta(valor, naipe))
    

    def embaralhar(self):
        random.shuffle(self.cartas)
    

    def dar_cartas(self, quantidade):
        cartas = []
        for _ in range(quantidade):
            cartas.append(self.cartas.pop())
        return cartas