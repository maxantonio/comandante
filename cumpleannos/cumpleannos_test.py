import unittest
import cumpleannos

parametro = 'Yadier Abel de Quesada'
class CumpleanosTest(unittest.TestCase):

    def test_dia(self):
        self.assertEqual(cumpleannos.dia('',parametro), "Su cumple es el 16 de Julio")
        self.assertEqual(cumpleannos.dia('','Python'), "no tengo ese dato todavia")

    def test_busca_usuario(self):
        self.assertEqual(cumpleannos.busca_usuario(parametro),{'name': 'Yadier Abel de Quesada', 'date': '1987-07-16'})
        self.assertFalse(cumpleannos.busca_usuario('Python'))

    def test_diasfaltantes(self):
        self.assertNotEqual(cumpleannos.diasfaltantes('', parametro), "no tengo ese dato todavia")
        self.assertEqual(cumpleannos.diasfaltantes('', 'Python'), "no tengo ese dato todavia")


if __name__ == "__main__":
    unittest.main()

