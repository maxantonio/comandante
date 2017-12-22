
from cumpleannos import cumpleanos
from bitcoins import bitcoins
from mercados import mercado
from comandante_help import comandante_help

def makeWebhookResult(req):
    result = req.get("result")
    accion = result.get("action")
    parameters = result.get("parameters")
    speech = get_manager_response(accion,parameters)
    return send_reponse_message(speech(accion,parameters))

def get_manager_response(accion):
    try:
        return {
            'comandante.help': comandante_help.devuelve_listado_help,
            'comandante.help.command': comandante_help.devuelve_listado_comando,
            'mercados.bitcoin.precioactual':bitcoins.devuelve_precio_actual,
            'comandante.cumpleanos.dia':cumpleanos.devuelve_cumples,
            'comandante.mercados.intradia': mercado.getintradia,
            'comandante.cumpleanos.diasfaltantes':cumpleanos.devuelve_dias_cumples,
            'comandante.cumpleanos.delmes':cumpleanos.cumples_del_mes,
            'comandante.cumpleanos.proximo':cumpleanos.proximo_cumple
        }[accion]
    except:
        return hook_not_found

def hook_not_found( _ , _2 ):
    return "Lo siento no entiendo que preguntas"

def send_reponse_message(speech):
    slack_message = {"text": speech}
    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        "source": "apiai-onlinestore-shipping"
    }