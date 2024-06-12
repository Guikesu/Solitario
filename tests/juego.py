from baraja import Baraja
from carta import Carta

class Pila:
    def __init__(self):
        self.cartas = []

    def agregar(self, carta):
        self.cartas.append(carta)

    def remover(self):
        return self.cartas.pop() if self.cartas else None

    def cima(self):
        return self.cartas[-1] if self.cartas else None

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas) if self.cartas else "Vacío"

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.columnas = [Pila() for _ in range(7)]
        self.fundaciones = [Pila() for _ in range(4)]
        self.montones = Pila()
        self._inicializar_juego()

    def _inicializar_juego(self):
        for i in range(7):
            for j in range(i + 1):
                carta = self.baraja.repartir()
                if j == i:
                    carta.volteada = True
                self.columnas[i].agregar(carta)

    def mover_a_fundacion(self, columna_idx):
        if 0 <= columna_idx < len(self.columnas):
            carta = self.columnas[columna_idx].cima()
            if carta and self._puede_mover_a_fundacion(carta):
                self.columnas[columna_idx].remover()
                self.fundaciones[self._indice_fundacion(carta.palo)].agregar(carta)

    def _puede_mover_a_fundacion(self, carta):
        fundacion = self.fundaciones[self._indice_fundacion(carta.palo)]
        if not fundacion.cima() and carta.valor == "A":
            return True
        elif fundacion.cima():
            cima = fundacion.cima()
            return self._valor_siguiente(cima.valor) == carta.valor
        return False

    def _indice_fundacion(self, palo):
        return ["Corazones", "Diamantes", "Tréboles", "Picas"].index(palo)

    def _valor_siguiente(self, valor):
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        idx = valores.index(valor)
        return valores[idx + 1] if idx < len(valores) - 1 else None

    def mover(self, origen, destino):
        if isinstance(origen, int) and destino == 'fundacion':
            carta = self.columnas[origen].cima()
            if carta and self._puede_mover_a_fundacion(carta):
                self.mover_a_fundacion(origen)
                return True
        return False

    def estado_juego(self):
        return {
            "columnas": [str(col) for col in self.columnas],
            "fundaciones": [str(fund) for fund in self.fundaciones],
            "montones": str(self.montones)
        }

    def imprimir_estado(self):
        estado = self.estado_juego()
        print("Columnas:")
        for idx, col in enumerate(estado["columnas"]):
            print(f"Columna {idx + 1}: {col}")
        print("\nFundaciones:")
        for idx, fund in enumerate(estado["fundaciones"]):
            print(f"Fundación {idx + 1}: {fund}")
        print("\nMontones:")
        print(estado["montones"])

if __name__ == "__main__":
    juego = Juego()
    juego.imprimir_estado()
    juego.mover(0, 'fundacion')
    juego.imprimir_estado()