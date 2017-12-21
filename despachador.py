from cumpleannos import cumpleanos
from bitcoins import bitcoins
from comandante_help import comandante_help

def makeWebhookResult(req):
    result = req.get("result")
    accion = result.get("action")
    parameters = result.get("parameters")
    speech = "Lo siento, no tengo ese dato todavia"

    #ayuda del comandante
    if accion == "comandante.help":
        speech = comandante_help.devuelve_listado_help(accion)
    if accion == "comandante.help.command":
        speech = comandante_help.devuelve_listado_comando(accion)

    #api BTC
    if accion == "comandante.preguntar.preciobtc":
        speech = bitcoins.devuelve_precio_actual(accion)

    #api cumpleannos
    if accion == "comandante.cumpleanos.dia":
        speech = cumpleanos.devuelve_cumples(accion,parameters)
    if accion == "comandante.cumpleanos.diasfaltantes":
        speech = cumpleanos.devuelve_dias_cumples(accion,parameters)
    if accion == "comandante.cumpleanos.delmes":
        speech = cumpleanos.cumples_del_mes(accion,parameters)

    return send_reponse_message(speech)



def send_reponse_message(speech):
    slack_message = {"text": speech}
    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        "source": "apiai-onlinestore-shipping"
    }
