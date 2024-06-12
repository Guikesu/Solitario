from juego import Juego
from jugador import Jugador

def mostrar_menu():
    print("Opciones:")
    print("1. Mover carta a fundación")
    print("2. Mostrar estado del juego")
    print("3. Salir")

def obtener_opcion():
    return input("Selecciona una opción: ")

def obtener_indice_columna():
    try:
        return int(input("Introduce el número de columna (1-7): ")) - 1
    except ValueError:
        print("Entrada no válida. Debe ser un número entre 1 y 7.")
        return obtener_indice_columna()

def main():
    print("Bienvenido al Solitario!")
    nombre_jugador = input("Introduce tu nombre: ")
    jugador = Jugador(nombre_jugador)
    juego = Juego()

    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "1":
            columna = obtener_indice_columna()
            if 0 <= columna < 7:
                if jugador.realizar_movimiento(juego, columna, 'fundacion'):
                    print("Movimiento realizado.")
                else:
                    print("Movimiento no permitido.")
            else:
                print("Columna no válida.")
        elif opcion == "2":
            juego.imprimir_estado()
        elif opcion == "3":
            print(f"Gracias por jugar, {jugador.nombre}. Has realizado {jugador.movimientos} movimientos.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()