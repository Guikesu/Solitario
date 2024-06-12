class Carta:
    def __init__(self, valor, palo, volteada=False):
        self.valor = valor
        self.palo = palo
        self.volteada = volteada

    def __repr__(self):
        if self.volteada:
            return f"{self.valor} de {self.palo}"
        return "Carta volteada"

# Implementación de `__str__` opcional si se necesita
    def __str__(self):
        return self.__repr__()