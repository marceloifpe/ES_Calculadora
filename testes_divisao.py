import unittest
from calculator import divisao


class TestCalculator(unittest.TestCase):
    def test_divisao_posi(self):
        self.assertEqual(divisao(10, 2), 5)

    def test_divisao_nega(self):
        self.assertEqual(divisao(-10, 2), -5)

    def test_divisao_zero(self):
        with self.assertRaises(ValueError):
            divisao(10, 0)


if __name__ == '__main__':
    unittest.main()
