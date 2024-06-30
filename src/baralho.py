from carta import Carta
import random

class Baralho:
    def __init__(self):
        self.__cartas = []
        self.criar_baralho()

    
    def criar_baralho(self):
        naipes = ["copas", "espadas", "ouros", "paus"]
        valores = ["A", "3", "2", "K", "Q", "J", "7", "6", "5", "4"]

        for valor in valores:
            for naipe in naipes:
                self.__cartas.append(Carta(valor, naipe))
    

    def embaralhar(self):
        random.shuffle(self.__cartas)
    

    def retirar_cartas(self, quantidade):
        cartas = []
        for i in range(quantidade):
            cartas.append(self.__cartas.pop())
        return cartas
    
    
    def get_cartas(self):
        return self.__cartas