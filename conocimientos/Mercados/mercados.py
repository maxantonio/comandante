import urllib.request, json


def intradia(accion,parameters):
    try:
        mercado = parameters.get("mercados")
    except:
        mercado = parameters
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