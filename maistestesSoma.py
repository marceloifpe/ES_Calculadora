import unittest
from calculator import soma


def soma(*args):
    return sum(args)


class TestSoma(unittest.TestCase):
    def test_soma_posi(self):
        self.assertEqual(soma(1, 2, 3, 4, 5), 15)

    def test_soma_nega(self):
        self.assertEqual(soma(-1, -2, -3, -4, -5), -15)

    def test_soma_posi_nega(self):
        self.assertEqual(soma(-1, 2, -3, 4, -5), -3)

    def test_soma_zer(self):
        self.assertEqual(soma(0, 1, 2, 3), 6)
        self.assertEqual(soma(0, -1, -2, -3), -6)

    def test_soma_rea(self):
        self.assertAlmostEqual(soma(0.1, 0.2), 0.3, places=7)

    def test_soma_num_uni(self):
        self.assertEqual(soma(7), 7)


if __name__ == '__main__':
    unittest.main()
