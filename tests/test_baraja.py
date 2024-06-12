import unittest
from src.baraja import Baraja

class TestBaraja(unittest.TestCase):
    def test_creacion_baraja(self):
        baraja = Baraja()
        self.assertEqual(len(baraja.cartas), 52)

    def test_barajar(self):
        baraja = Baraja()
        cartas_antes = baraja.cartas.copy()
        baraja.barajar()
        self.assertNotEqual(cartas_antes, baraja.cartas)

    def test_repartir(self):
        baraja = Baraja()
        carta = baraja.repartir()
        self.assertEqual(len(baraja.cartas), 51)
        self.assertIsNotNone(carta)

if __name__ == "__main__":
    unittest.main()