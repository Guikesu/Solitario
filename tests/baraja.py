import random
from carta import Carta

class Baraja:
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]

    def __init__(self):
        self.cartas = [Carta(valor, palo) for palo in self.palos for valor in self.valores]
        random.shuffle(self.cartas)

    def repartir(self):
        return self.cartas.pop() if self.cartas else None
