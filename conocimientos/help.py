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
    "conocimientos.cumpleanos.dia: Para el cumple de un miembro del equipo",
    "conocimientos.cumpleanos.diasfaltantes: Para conocer los dias faltantes del cumple de un miembro del equipo",
    "conocimientos.cumpleanos.delmes: Para saber los cumples de un mes",
    "conocimientos.mercados.intradia: Para saber el intradia actual de una emisora"
]

def help(accion,_):
    """
    Devuelve las posibles acciones que realiza el comandante
    >>> help('',_)
    ['Consulto el precio actual del Bitcoin', 'Puedo responder todo lo referente al cumpleannos del equipo IRSTRAT', 'Puedo ayudarte en la fecha y hora actual', 'Para conocer los comandos url teclee >> command']
    """
    return array_respuestas

def comando(accion,_):
    """
    Devuelve los posibles comandos que ejecuta el comandante
    >>> comando('',_)
    ['btc_prize: Conocer precio BITCOIN', 'hora: Hora actual', 'fecha: Fecha actual', 'cumpleanos.dia: Para el cumple de un miembro del equipo', 'cumpleanos.diasfaltantes: Para conocer los dias faltantes del cumple de un miembro del equipo', 'cumpleanos.delmes: Para saber los cumples de un mes']
    """
    return array_comandos



if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)
