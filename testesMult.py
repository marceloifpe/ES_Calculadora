import unittest
from mainMult import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        
        self.calculadora = Calculadora(10, 5)
    
    def test_multiplicar_positivo_positivo(self):
        self.assertEqual(self.calculadora.multiplicar(), 50)

    def test_multiplicar_negativo_negativo(self):
        c = Calculadora(-10, -5)
        self.assertEqual(c.multiplicar(), 50)

    def test_multiplicar_positivo_negativo(self):
        c = Calculadora(10, -5)
        self.assertEqual(c.multiplicar(), -50)

    def test_multiplicar_negativo_positivo(self):
        c = Calculadora(-10, 5)
        self.assertEqual(c.multiplicar(), -50)

    def test_multiplicar_neutro(self):
        c = Calculadora(0, 5)
        self.assertEqual(c.multiplicar(), 0)


if __name__ == '__main__':
    unittest.main()
