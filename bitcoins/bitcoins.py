import urllib.request
import json
from datetime import datetime

def devuelve_precio_actual(accion,parameters):
    moneda = parameters.get("criptomoneda")
    url = "http://api.coinmarketcap.com/v1/ticker/" + moneda
    speech = "Lo siento no encuentro el valor de " + moneda
    hora = datetime.now().strftime('%Y-%m-%d %H:%m')
    if accion == "mercados.bitcoin.precioactual":
        try:
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            preciobtc = json.loads(response.read())
            speech = "Tomado de " + url +\
                     "\n Actualizado el: " + hora +\
                     "\n Precio USD de:" + moneda + " " + str(preciobtc[0]['price_usd']) + "$"
        except urllib.error.URLError:
            speech = "No se ha podido acceder a " + url
    return speech

# $curl -d '{"result":{"action":"mercados.bitcoin.precioactual","parameters":{"criptomoneda":"Bitcoin"}}}' http://localhost:8080/webhook


