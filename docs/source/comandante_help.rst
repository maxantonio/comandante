Ayuda del Bot Comandante
========================

#. Contenido
------------

* Bot comandante es un ejemplo de webhook para consultar y devolver datos e informacion.

* El bot comandante responde lo que puede hacer y un listado de sus comandos para las consultas tipo curl
  $ curl -d '{"result":{"action":"comandante.help.help"}}' http://localhost:5000/webhook
  $ curl -d '{"result":{"action":"comandante.help.command"}}' http://localhost:5000/webhook
  $ curl -d '{"result":{"action":"comandante.cumpleanos.delmes","parameters":{"meses":"julio"}}}' http://localhost:8080/webhook
