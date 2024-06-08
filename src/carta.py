class Carta:
    # O padrão para descrever cartas é "valor naipe"
    forca_cartas = {
        "A espadas": 14, "A paus": 13, "7 espadas": 12, "7 ouros": 11,
        "3 copas": 10, "3 espadas": 10, "3 ouros": 10, "3 paus": 10,
        "2 copas": 9, "2 espadas": 9, "2 ouros": 9, "2 paus": 9,
        "A copas": 8, "A ouros": 8,
        "K espadas": 7, "K ouros": 7, "K copas": 7, "K paus": 7,
        "Q espadas": 6, "Q ouros": 6, "Q copas": 6, "Q paus": 6,
        "J espadas": 5, "J ouros": 5, "J copas": 5, "J paus": 5,
        "7 copas": 4, "7 paus": 4,
        "6 espadas": 3, "6 ouros": 3, "6 copas": 3, "6 paus": 3,
        "5 espadas": 2, "5 ouros": 2, "5 copas": 2, "5 paus": 2,
        "4 espadas": 1, "4 ouros": 1, "4 copas": 1, "4 paus": 1
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