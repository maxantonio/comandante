from datetime import datetime
from firebase import firebase
firebase = firebase.FirebaseApplication('https://comandante-189618.firebaseio.com/', None)

datos = firebase.get('/datos', None) #pendiente registrar los usuarios en firebase

def edad(accion,parameters):
    fecha = datos["fecha"]
    datetime_object = datetime.strptime(fecha, '%Y-%m-%d')
    fecha_actual = datetime.now()
    diferencia = fecha_actual - datetime_object
    anos = fecha_actual.year-datetime_object.year
    speech = "Mi edad es de "
    if anos == 0:
        dias = diferencia.days
        speech = speech + str(dias) + " dias"
    else:
        speech = speech + str(anos) + " años"
    return speech

def nombre(accion,parameters):
    nombre = datos["nombre"]
    speech = "Mi nombre completo es "+nombre
    return speech

def objetivo(accion,parameters):
    nombre = datos["nombre"]
    speech = "Mi objetivo es "+objetivo
    return speech


