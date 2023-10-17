# Aluno: Danilo Pereira Viana
# Curso Sistema para Internet p1 B

import unittest
from exemplo_1 import multiplicar
from exemplo_1 import adicao


class TestMultiplicar(unittest.TestCase):

    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(multiplicar(2, 3), 6)



class TestAdicao(unittest.TestCase):

    def test_adicao_cinco_mais_seis(self):
        self.assertEqual(adicao(5, 6), 11)

if __name__ == '__main__':
    unittest.main()