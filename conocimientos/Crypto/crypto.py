import urllib.request
import json
from datetime import datetime

def precioactual(accion,parameters):
    try:
        moneda = parameters.get("criptomoneda")
    except:
        moneda = parameters
    url = "http://api.coinmarketcap.com/v1/ticker/" + moneda
    hora = datetime.now().strftime('%Y-%m-%d %H:%m')
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        preciobtc = json.loads(response.read())
        speech = "Tomado de " + url +\
                 "\n Actualizado el: " + hora +\
                 "\n Precio USD de:" + moneda + " " + str(preciobtc[0]['price_usd']) + "$"
    except:
        speech = "Lo siento no encuentro el valor de " + moneda
    return speech

# $curl -d '{"result":{"action":"comandante.bitcoins.precioactual","parameters":{"criptomoneda":"Bitcoin"}}}' http://localhost:8080/webhook


