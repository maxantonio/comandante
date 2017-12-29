import unittest
import mercados

parametro = 'CADU'
class MercadosTest(unittest.TestCase):

    def test_dia(self):
        self.assertNotEqual(mercados.intradia('',parametro), "Lo siento no encuentro el intradia de "+ parametro)
        self.assertEqual(mercados.intradia('','Python'), "Lo siento no encuentro el intradia de "+ 'Python')


if __name__ == "__main__":
    unittest.main()

