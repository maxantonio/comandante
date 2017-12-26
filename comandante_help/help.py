array_respuestas = [
    "Consulto el precio actual del Bitcoin",
    "Puedo responder todo lo referente al cumpleannos del equipo IRSTRAT",
    "Puedo ayudarte en la fecha y hora actual",
    "Para conocer los comandos url teclee >> command"
]
array_comandos = [
    "btc_prize: Conocer precio BITCOIN",
    "hora: Hora actual",
    "fecha: Fecha actual",
    "cumpleanos.dia: Para el cumple de un miembro del equipo",
    "cumpleanos.diasfaltantes: Para conocer los dias faltantes del cumple de un miembro del equipo",
    "cumpleanos.delmes: Para saber los cumples de un mes",
]

def help(accion,_):
    if accion == "comandante.help":
        return array_respuestas

def comando(accion,_):
    if accion == "comandante.help.command":
        return array_comandos




