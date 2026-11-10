import unittest
from calculadora import calcular_total


class TestCalculadora(unittest.TestCase):
    def test_total_simples(self):
        self.assertEqual(calcular_total(50, 2), 100)

    def test_preco_negativo(self):
        with self.assertRaises(ValueError):
            calcular_total(-10, 1)

    def test_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            calcular_total(10, -2)


if __name__ == "__main__":
    unittest.main()
