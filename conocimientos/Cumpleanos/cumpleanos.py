from datetime import datetime
from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://comandante-189618.firebaseio.com/', None)

participantes = firebase.get('/usuarios', None) #pendiente registrar los usuarios en firebase
# participantes = json.loads(open('conocimientos/Cumpleanos/usuarios.json').read())
meses = ["Enero", "Febrero", "Marzo", "Abril",
         "Mayo", "Junio", "Julio", "Agosto",
         "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def dia(accion,parameters):
    speech = "no tengo ese dato todavia"
    usuario = parameters.get("usuarios")
    user = busca_usuario(usuario)
    if(user):
        fecha = user['date']
        datetime_object = datetime.strptime(fecha, '%Y-%m-%d')
        fecha_cumple = str(datetime_object.day) + ' de ' + meses[datetime_object.month-1]
        speech = "Su cumple es el " + fecha_cumple
    return speech

def diasfaltantes(accion,parameters):
    speech = "no tengo ese dato todavia"
    usuario = parameters.get("usuarios")
    user = busca_usuario(usuario)
    if (user):
        fecha = user['date']
        fecha_actual = datetime.now()
        print(fecha_actual)
        fecha_final_date = datetime.strptime(fecha, '%Y-%m-%d')
        fecha_final = str(fecha_final_date.day) + "-" + str(fecha_final_date.month) + "-" + str(fecha_actual.year)
        fecha_final_obj = datetime.strptime(fecha_final, '%d-%m-%Y')
        diferencia = fecha_final_obj - fecha_actual
        if (diferencia.days < 0):
            #msg = "Han pasado:" + str(abs(diferencia.days)) + "dias "
            fecha_final = str(fecha_final_date.day) + "-" + str(fecha_final_date.month) + "-" + str(fecha_actual.year + 1)
            fecha_final_obj = datetime.strptime(fecha_final, '%d-%m-%Y')
            diferencia = fecha_final_obj - fecha_actual
        speech =  "Faltan: " + str(abs(diferencia.days)) + " dias para su cumple"
    return speech

#recorre el arreglo de usuarios para encontrar fechas correspondientes
# con el mes en curso o con un mes pasado x parametros
def delmes(accion,parameters):
    speech = "Este mes no hay cumples"
    msg = ""
    mes = datetime.now().month
    if(parameters.get("meses") != ""):
        mes = parameters.get("meses")
    for i, data in enumerate(participantes):
        data = participantes[data]
        print(data)
        fecha = data['date']
        datetime_object = datetime.strptime(fecha, '%Y-%m-%d')
        if(meses[datetime_object.month-1] == mes):
            msg = msg + data["name"] + " el dia " + str(datetime_object.day) + " - "
    if(msg != ""):
        speech = mes + ":" + msg
    return speech

# segun la fecha actual responde cual es el proximo cumpleano
def proximo(accion,parameters):
    speech = "Aun no se responder"
    actual = datetime.now()
    menor_dif = -1
    cumpleanero = ""
    for i, data in enumerate(participantes):
        fecha_str = data['date']
        nace = datetime.strptime(fecha_str, '%Y-%m-%d')
        cumple = nace.replace(actual.year)
        diferencia = cumple-actual
        if(diferencia.days<0):
            cumple = nace.replace(actual.year+1)
            diferencia = cumple-actual
        if(diferencia.days<menor_dif) or (menor_dif<0):
            menor_dif = diferencia.days
            cumpleanero = data["name"] 
    speech = "El proximo cumple es de "+cumpleanero+" y es dentro de "+str(menor_dif)+" dias"
    return speech
    
def busca_usuario(usuario):
    for i, data in enumerate(participantes):
        if (data['name'] == usuario):
            return data
    return  False



if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)
