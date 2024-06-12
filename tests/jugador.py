class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.movimientos = 0

    def realizar_movimiento(self, juego, origen, destino):
        # Esta es una función genérica, donde `origen` y `destino` podrían ser columnas, fundaciones, etc.
        if juego.mover(origen, destino):
            self.movimientos += 1
            return True
        return False

    def reiniciar_movimientos(self):
        self.movimientos = 0

    def __str__(self):
        return f"Jugador: {self.nombre}, Movimientos: {self.movimientos}"

if __name__ == "__main__":
    from juego import Juego

    juego = Juego()
    jugador = Jugador("Jugador 1")
    print(jugador)
    # Ejemplo de cómo el jugador realiza un movimiento
    if jugador.realizar_movimiento(juego, 0, 'fundacion'):  # mover la carta de la columna 0 a la fundación
        print("Movimiento realizado.")
    else:
        print("Movimiento no permitido.")
    print(jugador)