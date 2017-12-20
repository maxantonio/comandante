Usando comando curl para probar webhook
========================================

#. Testing para conocer los cumples  del mes actual o un mes en particular
------------------------------------------------------------------------
 * $ curl -d  '{"result":{"action":"preguntar.cumpleanos.delmes","parameters":{"meses":"Julio"}}}'  http://localhost:5000/webhook/cumpleanero
 * $ curl -d  '{"result":{"action":"preguntar.cumpleanos.delmes","parameters":{"meses":""}}}'  http://localhost:5000/webhook/cumpleanero

#. Para conocer  el dia segun un usuario en particular
----------------------------------------------------
 * $ curl -d  '{"result":{"action":"preguntar.cumpleanos.dia","parameters":{"usuarios":"Yadier Abel de Quesada"}}}'  http://localhost:5000/webhook/cumpleanero
 * $ curl -d  '{"result":{"action":"preguntar.cumpleanos.dia","parameters":{"usuarios":"Jerry Jimenez Tamayo"}}}'  http://localhost:5000/webhook/cumpleanero
 * $ curl -d  '{"result":{"action":"preguntar.cumpleanos.dia","parameters":{"usuarios":"MAX LOVERA"}}}'  http://localhost:5000/webhook/cumpleanero

#. Para conocer los dias que faltan para el cumpleaños de un usuario en particular
---------------------------------------------------------------------------------
 * $ curl -d '{"result":{"action":"preguntar.cumpleanos.diasfaltantes","parameters":{"usuarios":"Yadier Abel de Quesada"}}}' http://localhost:5000/webhook/cumpleanero