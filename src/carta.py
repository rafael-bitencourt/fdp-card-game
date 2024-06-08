class Carta:
    forca_cartas = {
        "A espadas": 14,
        "A paus": 13,
        "7 espadas": 12,
        "7 ouros": 11,
        "A copas": 10,
        "A ouros": 10,
        "K espadas": 9,
        "K copas": 9,
        "K ouros": 9,
        "K paus": 9,
        "Q espadas": 8,
        "Q copas": 8,
        "Q ouros": 8,
        "Q paus": 8,
        "J espadas": 7,
        "J copas": 7,
        "J ouros": 7,
        "J paus": 7,
        "7 copas": 6,
        "7 paus": 6,
        "6 espadas": 5,
        "6 copas": 5,
        "6 ouros": 5,
        "6 paus": 5,
        "5 espadas": 4,
        "5 copas": 4,
        "5 ouros": 4,
        "5 paus": 4,
        "4 espadas": 3,
        "4 copas": 3,
        "4 ouros": 3,
        "4 paus": 3,
    }

    def __init__(self, valor, naipe):
        self.__valor = valor
        self.__naipe = naipe
    
    def __str__(self):
        return f"{self.valor} de {self.naipe}"
    
    def get_valor(self):
        return self.valor

    def get_naipe(self):
        return self.naipe

    def get_forca(self):
        return Carta.forca_cartas[f"{self.get_valor()} {self.get_naipe()}"]