"""Testes da Calculadora Científica.

Bug escolhido para o TDD: Bug #1 (a adição retorna 2x + y em vez de x + y).
Esses testes descrevem o comportamento ESPERADO da soma, então
precisam falhar enquanto o bug existir (fase vermelha do TDD).

Como rodar:
    python -m unittest -v
"""

import unittest

from Calculadora import (
    adicao,
    subtracao,
    multiplicacao,
    divisao,
    potencia,
    raiz_quadrada,
)


class TestAdicao(unittest.TestCase):

    def test_soma_numeros_positivos(self):
        self.assertEqual(adicao(2, 3), 5)

    def test_soma_numeros_negativos(self):
        self.assertEqual(adicao(-2, -3), -5)

    def test_soma_positivo_com_negativo(self):
        self.assertEqual(adicao(10, -4), 6)

    def test_soma_com_zero(self):
        # zero é o elemento neutro: x + 0 = x e 0 + x = x
        self.assertEqual(adicao(7, 0), 7)
        self.assertEqual(adicao(0, 7), 7)

    def test_soma_numeros_decimais(self):
        # 0.1 + 0.2 não dá exatamente 0.3 em ponto flutuante,
        # por isso uso assertAlmostEqual
        self.assertAlmostEqual(adicao(0.1, 0.2), 0.3)

    def test_soma_e_comutativa(self):
        # a ordem não pode mudar o resultado: x + y = y + x
        self.assertEqual(adicao(4, 9), adicao(9, 4))

    def test_soma_como_no_menu_com_float(self):
        # o menu converte a entrada com float(), então testo com float também
        self.assertEqual(adicao(2.0, 3.0), 5.0)

    def test_retorna_float_comum_no_menu(self):
        # depois da refatoração (x + y) o resultado é float do Python,
        # igual às outras operações básicas como a subtração
        self.assertIsInstance(adicao(2.0, 3.0), float)


class TestRegressaoOperacoesBasicas(unittest.TestCase):
    """Testes de regressão: as operações que já funcionavam
    não podem quebrar por causa da correção da adição."""

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 4), 6)
        self.assertEqual(subtracao(4, 10), -6)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 4), 12)
        self.assertEqual(multiplicacao(-2, 5), -10)

    def test_divisao_com_divisor_diferente_de_zero(self):
        # divisão por zero é o Bug #2 e ainda não foi corrigida
        self.assertEqual(divisao(10, 4), 2.5)

    def test_potencia(self):
        self.assertEqual(potencia(2, 10), 1024)
        self.assertEqual(potencia(9, 0.5), 3)

    def test_raiz_quadrada_de_numero_positivo(self):
        self.assertEqual(raiz_quadrada(16), 4)


if __name__ == "__main__":
    unittest.main()
