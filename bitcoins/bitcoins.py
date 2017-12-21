import json
#preciobtc = json.loads("https://api.coindesk.com/v1/bpi/currentprice.json")
preciobtc = json.loads(open('bitcoins/bitcoins.json').read())

def devuelve_precio_actual(accion):
    if accion == "preguntar.preciobtc":
        speech = preciobtc
    return speech






