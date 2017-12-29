import urllib.request, json


def intradia(accion,parameters):
    mercado = parameters.get("mercados")
    url_api = "http://h-kont.herokuapp.com/api/intradia/"+mercado
    intradia = False
    speech = "Lo siento no encuentro el intradia de "+mercado
    try:
        with urllib.request.urlopen(url_api) as url:
            data = json.loads(url.read().decode())
            intradia = data["intradia"]
            print(data["intradia"])
    except:
        intradia = False
    if(intradia):
        speech = "El precio actual de "+str(intradia["symbol"])+" es $"+str(intradia["price"])+", con un cambio de "+\
                 str(intradia["percent"])+" y un volumen de "+str(intradia["volume"])+". Obtenido el "+str(intradia["date"])+" a las "+intradia["time"]
    return speech

def haustatus(_,parameters):
    mercado = parameters.get("mercados")
    url_api = "http://h-kont.herokuapp.com/api/fstatus"
    status = False
    speech = "Lo siento no puedo obtener el estado "
    try:
        with urllib.request.urlopen(url_api) as url:
            data = json.loads(url.read().decode())
            status = data["data"]
            print(data["data"])
    except:
        status = False
    if (status):
        speech = "El ultimo mensaje recibido por la HAU fue a las " + str(status["Time_last_message"]) + " de " + str(
            status["Date"])
    return speech

#curl -d '{"result":{"action":"conocimientos.mercados.delmes","parameters":{"meses":"Julio"}}}' http://localhost:8080/webhook
#curl -d '{"result":{"action":"conocimientos.mercados.haustatus"}}' http://localhost:8080/webhook
