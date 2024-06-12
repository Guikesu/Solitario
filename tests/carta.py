class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        self.volteada = False

    def voltear(self):
        self.volteada = not self.volteada

    def __str__(self):
        return f"{self.valor} de {self.palo}" if self.volteada else "Carta oculta"