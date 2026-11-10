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

    def test_desconto_dez_porcento(self):
        self.assertEqual(calcular_total(50, 2, desconto=10), 90)

    def test_desconto_zero(self):
        self.assertEqual(calcular_total(50, 2, desconto=0), 100)

    def test_desconto_cem_porcento(self):
        self.assertEqual(calcular_total(50, 2, desconto=100), 0)

    def test_desconto_acima_do_limite(self):
        with self.assertRaises(ValueError):
            calcular_total(50, 2, desconto=120)

    def test_desconto_abaixo_do_limite(self):
        with self.assertRaises(ValueError):
            calcular_total(50, 2, desconto=-5)


if __name__ == "__main__":
    unittest.main()
