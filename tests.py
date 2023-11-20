# tests.py
import unittest
from program import calcular_media

class TestCalcularMedia(unittest.TestCase):

    def test_media_lista_inteiros(self):
        numeros = [1, 2, 3, 4, 5]
        resultado = calcular_media(numeros)
        self.assertEqual(resultado, 3.0)

    def test_media_lista_floats(self):
        numeros = [1.5, 2.5, 3.5, 4.5, 5.5]
        resultado = calcular_media(numeros)
        self.assertEqual(resultado, 3.5)

    def test_media_lista_mista(self):
        numeros = [1, 2.5, 3, 4.5, 5]
        resultado = calcular_media(numeros)
        self.assertEqual(resultado, 3.2)

    def test_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

if __name__ == '__main__':
    unittest.main()
