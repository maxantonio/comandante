#!/usr/bin/env python

import json
import os

from flask import Flask
from flask import make_response
from flask import request

import despachador

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
#definiendo la macroruta desde donde se extrae el api

def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    res = despachador.makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print ("Starting app on port %d")
    # % port
    app.run(debug=True, port=port, host='0.0.0.0')
