#!/usr/bin/env python


# [START app]
import logging
import json
import os

from flask import Flask
from flask import make_response
from flask import request

import despachador


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World hook!'

@app.route('/webhook', methods=['POST'])
#definiendo la macroruta desde donde se extrae el api
def cumpleanero():
    req = request.get_json(silent=True, force=True)
    #res = cumpleanos.despachador(req)
    res = despachador.makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
