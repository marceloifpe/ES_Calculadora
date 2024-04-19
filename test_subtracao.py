import unittest

def subtracao(num1, num2):
    return num1 - num2

class TestSubtracao(unittest.TestCase):
    def test_subtracao_positiva(self):
        resultado = subtracao(7, 3)
        self.assertEqual(resultado, 4, "A subtração de 7 - 3 deve ser igual a 4")

    def test_subtracao_positiva(self):
        resultado = subtracao(50, 50)
        self.assertEqual(resultado, 0, "A subtração de 50 - 50 deve ser igual a 0")

    def test_subtracao_negativa(self):
        resultado = subtracao(200, 250)
        self.assertEqual(resultado, -50, "A subtração de 200 - 250 deve ser igual a -50")

    def test_subtracao_negativa(self):
        resultado = subtracao(-7, -3)
        self.assertEqual(resultado, -4, "A subtração de -7 - (-3) deve ser igual a -4")

    def test_subtracao_mista(self):
        resultado = subtracao(7, -3)
        self.assertEqual(resultado, 10, "A subtração de 7 - (-3) deve ser igual a 10")



if __name__ == '__main__':
    unittest.main()