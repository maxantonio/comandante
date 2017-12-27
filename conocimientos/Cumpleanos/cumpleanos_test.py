import unittest
from conocimientos import Cumpleanos


parametro = 'Yadier Abel de Quesada'
testmes = 'Julio'
class CumpleanosTest(unittest.TestCase):

    def test_dia(self):
        self.assertEqual(Cumpleanos.dia('',parametro), "Su cumple es el 16 de Julio")
        self.assertEqual(Cumpleanos.dia('','Python'), "no tengo ese dato todavia")

    def test_diasfaltantes(self):
        self.assertNotEqual(Cumpleanos.diasfaltantes('', parametro), "no tengo ese dato todavia")
        self.assertEqual(Cumpleanos.diasfaltantes('', 'Python'), "no tengo ese dato todavia")

    def test_busca_usuario(self):
        self.assertEqual(Cumpleanos.busca_usuario(parametro),{'name': 'Yadier Abel de Quesada', 'date': '1987-07-16'})
        self.assertFalse(Cumpleanos.busca_usuario('Python'))

    def test_delmes(self):
        self.assertNotEqual(Cumpleanos.test_delmes('', testmes), "Este mes no hay cumples")

    # segun la fecha actual responde cual es el proximo cumpleano
    def test_proximo(self):
        self.assertNotEqual(Cumpleanos.test_delmes('', testmes), "Aun no se responder")


if __name__ == "__main__":
    unittest.main()

