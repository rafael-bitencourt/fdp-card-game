from model.carta import Carta

class Baralho:
    def __init__(self):
        self.cartas = []
    
    def criar_baralho(self):
        naipes = ["copas", "espadas", "ouros", "paus"]
        valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        
        for naipe in naipes:
            for valor in valores:
                self.cartas.append(Carta(valor, naipe))