
from cumpleannos import cumpleanos
from bitcoins import bitcoins
from mercados import mercados
from comandante_help import help

def makeWebhookResult(req):
    result = req.get("result")
    accion = result.get("action")
    parameters = result.get("parameters")
    methods = accion.split(".")
    m = globals()[methods[1]]
    func = getattr(m, methods[2])
    try:
        spetch = func(accion, parameters)
    except:
        spetch = "Lo siento no entiendo que preguntas"
    return send_reponse_message(spetch)

def send_reponse_message(speech):
    slack_message = {"text": speech}
    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        "source": "apiai-onlinestore-shipping"
    }