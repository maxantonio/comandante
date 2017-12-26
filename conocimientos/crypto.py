import urllib.request
import json
from datetime import datetime

def precioactual(accion,parameters):
    url = "http://api.coinmarketcap.com/v1/ticker/"
    speech = {}
    hora = datetime.now().strftime('%Y-%m-%d %H:%m')
    if accion == "mercados.bitcoin.precioactual":
        moneda = parameters.get("cryptomonedas")
        url = url + moneda
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        preciobtc = json.loads(response.read())
        speech[0] = "Tomado de http://api.coinmarketcap.com/v1/ticker/"
        speech[1] = "Actualizado el: " + hora
        speech[2] = "Precio USD de:" + moneda + " " + str(preciobtc[0]['price_usd']) + "$"
    return speech

# $curl -d '{"result":{"action":"mercados.bitcoin.precioactual","parameters":{"criptomoneda":"Bitcoin"}}}' http://localhost:8080/webhook
