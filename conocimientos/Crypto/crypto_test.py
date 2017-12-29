import unittest
import crypto

parametro = 'Bitcoin'
url = "http://api.coinmarketcap.com/v1/ticker/" + parametro
class CryptoTest(unittest.TestCase):

    def test_precioactual_dia(self):
        self.assertNotEqual(crypto.precioactual('', parametro),"Lo siento no encuentro el valor de " + parametro)
        self.assertEqual(crypto.precioactual('', 'Python'), "Lo siento no encuentro el valor de " + 'Python')

if __name__ == "__main__":
    unittest.main()
