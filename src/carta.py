class Carta:
    forca_cartas = {
        "A de espadas": 14, "A de paus": 13, "7 de espadas": 12, "7 de ouros": 11,
        "A de copas": 10, "A de ouros": 10, "K de espadas": 9, "K de copas": 9,
        "K de ouros": 9, "K de paus": 9, "Q de espadas": 8, "Q de copas": 8,
        "Q de ouros": 8, "Q de paus": 8, "J de espadas": 7, "J de copas": 7,
        "J de ouros": 7, "J de paus": 7, "7 de copas": 6, "7 de paus": 6,
        "6 de espadas": 5, "6 de copas": 5, "6 de ouros": 5, "6 de paus": 5,
        "5 de espadas": 4, "5 de copas": 4, "5 de ouros": 4, "5 de paus": 4,
        "4 de espadas": 3, "4 de copas": 3, "4 de ouros": 3, "4 de paus": 3,
    }

    def __init__(self, valor, naipe):
        self.__valor = valor
        self.__naipe = naipe
    
    def __str__(self):
        return f"{self.valor} de {self.naipe}"
    
    def get_valor(self):
        return self.__valor

    def get_naipe(self):
        return self.__naipe

    def get_forca(self):
        return Carta.forca_cartas[f"{self.get_valor()} {self.get_naipe()}"]