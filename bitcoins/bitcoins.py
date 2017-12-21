import json
#preciobtc = json.loads("https://api.coindesk.com/v1/bpi/currentprice.json")
preciobtc = json.loads(open('bitcoins/bitcoins.json').read())


#curl -d '{"result":{"action":"comandante.preguntar.preciobtc"}}' http://localhost:5000/webhook
def devuelve_precio_actual(accion):
    if accion == "comandante.preguntar.preciobtc":
        speech = preciobtc
    return speech






