# src/carta.py
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __repr__(self):
        return f"{self.valor} de {self.palo}"