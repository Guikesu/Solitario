# Solitario en Python 🃏

## Descripción

Este proyecto es una implementación del juego de cartas Solitario en Python. El juego se ha desarrollado como una aplicación de consola, con clases bien definidas para representar las cartas, la baraja y la lógica del juego. Opcionalmente, se puede agregar una interfaz gráfica usando `tkinter` o `pygame`.

## Reglas del Juego

El juego implementa la variante Klondike del Solitario. Las reglas básicas son:

1. El objetivo es mover todas las cartas a las pilas de fundación, organizadas por palo en orden ascendente desde el As hasta el Rey.
2. Solo se puede mover una carta a la vez, ya sea a una columna del tablero o a una pila de fundación.
3. Se pueden mover las cartas a columnas vacías solo si son Reyes.
4. Las cartas en las columnas del tablero deben alternar colores y estar en orden descendente.
5. El juego termina cuando todas las cartas están en las pilas de fundación o cuando no hay más movimientos posibles.

## Instalación

Para ejecutar el juego localmente, sigue estos pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Guikesu/Solitario.git
    cd solitario
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar el juego, ejecuta el archivo `main.py`:
```bash
python src/main.py
