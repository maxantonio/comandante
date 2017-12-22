import urllib.request, json


def getintradia(parameters):
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
    slack_message = {"text": speech}
    return send_reponse_message(speech, slack_message)

def send_reponse_message(speech,slack_message):
    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        "source": "apiai-onlinestore-shipping" #preguntar por que este source
    }