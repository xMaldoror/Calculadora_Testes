import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4


class TestCalculadora(unittest.TestCase):

    def teste_operacoes_basicas(self):
        # Teste operações básicas de cada operador + - * / % ^
        self.assertEqual(calculadora(2, 3, '+'), 5)

    def teste_v2_operacoes(self):
        # Teste operações básicas de cada operador + - * / % ^
        self.assertEqual(calculadora_v2(2, 3, '+'), 5)

    def teste_v3_operacoes(self):
        # Teste operações básicas de cada operador + - * / % ^
        self.assertEqual(calculadora_v3(2, 3, '+'), 5)

    def teste_v4_operacoes(self):
        # Teste operações básicas de cada operador + - * / % ^
        self.assertEqual(calculadora_v4(2, 3, '+'), 5)

    def teste_operacoes_diversas(self):
        # Teste divisão por zero operador para todas versões / %
        self.assertTrue(math.isnan(calculadora(5, 0, '/')))
        self.assertTrue(math.isnan(calculadora(5, 0, '%')))

        # Teste operador inválido - fazer três testes para todas as versões
        self.assertTrue(math.isnan(calculadora(2, 3, '$')))
        self.assertTrue(math.isnan(calculadora(2, 5, '#')))
        self.assertTrue(math.isnan(calculadora(0, 2, 'qwe')))

        # Teste números de virgula flutuante - fazer três testes para todas as versões
        self.assertAlmostEqual(calculadora(2.5, 1.5, '+'), 4.0)
        self.assertAlmostEqual(calculadora(4.5, 1.5, '-'), 3.0)
        self.assertAlmostEqual(calculadora(5.5, 1.5, '*'), 8.25)

        # Teste números negativos - fazer 3 testes para todas as versões
        self.assertEqual(calculadora(-2, 3, '*'), -6)

        # Teste números negativos com divisão e módulo, testar para todas as versões
        self.assertTrue(calculadora(-6, 3, '/'), -2.0)
        self.assertTrue(calculadora(-7, 3, '%'), 2.0)

        # Teste números negativos com exponenciação, testar para todas as versões
        self.assertEqual(calculadora(-2, 3, '^'), -8)

        # Teste números negativos com exponenciação de zero, testar para todas as versões
        self.assertEqual(calculadora(0, 3, '^'), 0)


if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v testes_main_alunos.py
