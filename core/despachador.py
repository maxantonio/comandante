
from conocimientos import cumpleanos
from conocimientos import mercados
from conocimientos import crypto
from conocimientos import help

def makeWebhookResult(req):
    result = req.get("result")
    accion = result.get("action")
    parameters = result.get("parameters")
    methods = accion.split(".")
    m = globals()[methods[1]]
    func = getattr(m, methods[2])
    try:
        speech = func(accion, parameters)
    except:
        speech = "Lo siento no entiendo que preguntas"
    return send_reponse_message(speech)

def send_reponse_message(speech):
    slack_message = {"text": speech}
    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        "source": "apiai-onlinestore-shipping"
    }