from datetime import datetime
import json

participantes = json.loads(open('cumpleannos/usuarios.json').read())
meses = ["Enero", "Febrero", "Marzo", "Abril",
         "Mayo", "Junio", "Julio", "Agosto",
         "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def devuelve_cumples(accion,parameters):
    speech = "no tengo ese dato todavia"
    if accion == "comandante.cumpleanos.dia":
        usuario = parameters.get("usuarios")
        user = busca_usuario(usuario)
        if(user):
            fecha = user['date']
            datetime_object = datetime.strptime(fecha, '%Y-%m-%d')
            fecha_cumple = str(datetime_object.day) + ' de ' + meses[datetime_object.month-1]
            speech = "Su cumple es el " + fecha_cumple

    return speech

def devuelve_dias_cumples(accion,parameters):
    speech = "no tengo ese dato todavia"
    if accion == "comandante.cumpleanos.diasfaltantes":
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
def cumples_del_mes(accion,parameters):
    speech = "Este mes no hay cumples"
    if accion == "comandante.cumpleanos.delmes":
        mes = datetime.now().month
        msg = ""
        if(parameters.get("meses") != ""):
            mes = parameters.get("meses")
        for i, data in enumerate(participantes):
            fecha = data['date']
            datetime_object = datetime.strptime(fecha, '%Y-%m-%d')
            if(meses[datetime_object.month-1] == mes):
                msg = msg + data["name"] + " el dia " + str(datetime_object.day) + " - "
    if(msg != ""):
        speech = mes + ":" + msg

    return speech




def busca_usuario(usuario):
    for i, data in enumerate(participantes):
        if (data['name'] == usuario):
            return data
    return  False




