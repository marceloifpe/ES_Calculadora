import unittest
from main import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
       
        self.calculadora = Calculadora(10, 5)

     # Testes Soma
    def test_somar_positivo_positivo(self):
        self.assertEqual(self.calculadora.somar(), 15)

    def test_somar_negativo_negativo(self):
        c = Calculadora(-10, -5)
        self.assertEqual(c.somar(), -15)

    def test_somar_positivo_negativo(self):
        c = Calculadora(10, -5)
        self.assertEqual(c.somar(), 5)

    def test_somar_negativo_positivo(self):
        c = Calculadora(-10, 5)
        self.assertEqual(c.somar(), -5)

    def test_somar_neutro(self):
        c = Calculadora(0, 5)
        self.assertEqual(c.somar(), 5)

    def test_somar_positivo_positivo_custom(self):
        self.calculadora = Calculadora(13, 7)
        self.assertEqual(self.calculadora.somar(), 20)

        # Testes Subtração

    def test_subtrair_positivo_positivo(self):
        self.assertEqual(self.calculadora.subtrair(), 5)

    def test_subtrair_negativo_negativo(self):
        c = Calculadora(-10, -5)
        self.assertEqual(c.subtrair(), -5)

    def test_subtrair_positivo_negativo(self):
        c = Calculadora(10, -5)
        self.assertEqual(c.subtrair(), 15)

    def test_subtrair_negativo_positivo(self):
        c = Calculadora(-10, 5)
        self.assertEqual(c.subtrair(), -15)

    def test_subtrair_neutro(self):
        c = Calculadora(0, 5)
        self.assertEqual(c.subtrair(), -5)

    def test_subtrair_positivo_positivo_custom(self):
        self.calculadora = Calculadora(13, 7)
        self.assertEqual(self.calculadora.subtrair(), 6)

        # Testes Multiplicação

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

    def test_multiplicar_positivo_positivo_custom(self):
        self.calculadora = Calculadora(13, 7)
        self.assertEqual(self.calculadora.multiplicar(), 91)


        # Testes Divisão
    def test_dividir_positivo_positivo(self):
        self.assertEqual(self.calculadora.dividir(), 2)

    def test_dividir_negativo_negativo(self):
        c = Calculadora(-10, -5)
        self.assertEqual(c.dividir(), 2)

    def test_dividir_positivo_negativo(self):
        c = Calculadora(10, -5)
        self.assertEqual(c.dividir(), -2)

    def test_dividir_negativo_positivo(self):
        c = Calculadora(-10, 5)
        self.assertEqual(c.dividir(), -2)

    def test_dividir_neutro(self):
        c = Calculadora(0, 5)
        self.assertEqual(c.dividir(), 0)

    def test_dividir_positivo_positivo_custom(self):
        self.calculadora = Calculadora(14, 7)
        self.assertEqual(self.calculadora.dividir(), 2)

if __name__ == '__main__':
    unittest.main()
