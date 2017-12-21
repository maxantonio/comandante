Usando comando curl para probar webhook
========================================

#. Testing para conocer los cumples  del mes actual o un mes en particular
------------------------------------------------------------------------
 * $ curl -d  '{"result":{"action":"comandante.cumpleanos.delmes","parameters":{"meses":"Julio"}}}'  http://localhost:5000/webhook
 * $ curl -d  '{"result":{"action":"comandante.cumpleanos.delmes","parameters":{"meses":""}}}'  http://localhost:5000/webhook

#. Para conocer  el dia segun un usuario en particular
----------------------------------------------------
 * $ curl -d  '{"result":{"action":"comandante.cumpleanos.dia","parameters":{"usuarios":"Yadier Abel de Quesada"}}}'  http://localhost:5000/webhook
 * $ curl -d  '{"result":{"action":"comandante.cumpleanos.dia","parameters":{"usuarios":"Jerry Jimenez Tamayo"}}}'  http://localhost:5000/webhook
 * $ curl -d  '{"result":{"action":"comandante.cumpleanos.dia","parameters":{"usuarios":"MAX LOVERA"}}}'  http://localhost:5000/webhook

#. Para conocer los dias que faltan para el cumpleaños de un usuario en particular
---------------------------------------------------------------------------------
 * $ curl -d '{"result":{"action":"comandante.cumpleanos.diasfaltantes","parameters":{"usuarios":"Yadier Abel de Quesada"}}}' http://localhost:5000/webhook

#. Para consultar la ayuda
--------------------------
 * $ curl -d '{"result":{"action":"comandante.help"}}' http://localhost:5000/webhook

#. Para consultar precios de criptomonedas
------------------------------------------
 * $ curl -d '{"result":{"action":"mercados.bitcoin.precioactual","parameters":{"criptomoneda":"Bitcoin"}}}' http://localhost:5000/webhook