from datetime import datetime
import json

preciobtc = json.loads("https://api.coindesk.com/v1/bpi/currentprice.json")


def devuelve_precio_actual(accion,parameters):
    speech = "no tengo ese dato todavia"
    if accion == "preguntar.preciobtc":
        speech = preciobtc
    return speech






