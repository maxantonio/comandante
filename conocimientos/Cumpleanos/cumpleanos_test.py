import unittest
from conocimientos import Cumpleanos
import cumpleannos

parametro = 'Yadier Abel de Quesada'
mes = 'Julio'
class CumpleanosTest(unittest.TestCase):

    def test_dia(self):
        self.assertEqual(Cumpleanos.dia('',parametro), "Su cumple es el 16 de Julio")
        self.assertEqual(cumpleannos.dia('','Python'), "no tengo ese dato todavia")

    def test_diasfaltantes(self):
        self.assertNotEqual(cumpleannos.diasfaltantes('', parametro), "no tengo ese dato todavia")
        self.assertEqual(cumpleannos.diasfaltantes('', 'Python'), "no tengo ese dato todavia")

    def test_busca_usuario(self):
        self.assertEqual(cumpleannos.busca_usuario(parametro),{'name': 'Yadier Abel de Quesada', 'date': '1987-07-16'})
        self.assertFalse(cumpleannos.busca_usuario('Python'))

    def test_delmes(self):
        self.assertNotEqual(cumpleannos.diasfaltantes('', parametro), "no tengo ese dato todavia")
        speech = "Este mes no hay cumples"
        msg = ""
        mes = datetime.now().month
        if (parameters.get("meses") != ""):
            try:
                mes = parameters.get("meses")
            except:
                mes = parameters
        for i, data in enumerate(participantes):
            fecha = data['date']
            datetime_object = datetime.strptime(fecha, '%Y-%m-%d')
            if (meses[datetime_object.month - 1] == mes):
                msg = msg + data["name"] + " el dia " + str(datetime_object.day) + " - "
        if (msg != ""):
            speech = mes + ":" + msg
        return speech

    # segun la fecha actual responde cual es el proximo cumpleano
    def proximo(accion, _):
        actual = datetime.now()
        menor_dif = -1
        cumpleanero = ""
        for i, data in enumerate(participantes):
            fecha_str = data['date']
            nace = datetime.strptime(fecha_str, '%Y-%m-%d')
            cumple = nace.replace(actual.year)
            diferencia = cumple - actual
            if (diferencia.days < 0):
                cumple = nace.replace(actual.year + 1)
                diferencia = cumple - actual
            if (diferencia.days < menor_dif) or (menor_dif < 0):
                menor_dif = diferencia.days
                cumpleanero = data["name"]
        speech = "El proximo cumple es de " + cumpleanero + " y es dentro de " + str(menor_dif) + " dias"
        return speech


if __name__ == "__main__":
    unittest.main()

