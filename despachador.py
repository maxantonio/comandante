from cumpleannos import cumpleanos
from mercados import mercado
def makeWebhookResult(req):
    # accionando = req.get("result").get("action")
    result = req.get("result")
    accion = result.get("action")
    parameters = result.get("parameters")

    if accion == "preguntar.cumpleanos.dia":
        return cumpleanos.devuelve_cumples(accion,parameters)
    if accion == "preguntar.cumpleanos.diasfaltantes":
        return cumpleanos.devuelve_dias_cumples(accion,parameters)
    if accion == "preguntar.cumpleanos.delmes":
        return cumpleanos.cumples_del_mes(accion,parameters)
    if accion == "preguntar.cumpleanos.proximo":
        return cumpleanos.proximo_cumple()
    if accion == "preguntar.mercados.intradia":
        return mercado.getintradia(parameters)
    else:
        return {
            "speech": "ni idea",
            "displayText": "speech",
            "data": {},
            # "contextOut": [],
            "source": "apiai-onlinestore-shipping"
        }
