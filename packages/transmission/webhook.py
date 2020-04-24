#!/usr/bin/env python
"""
Simple webhook listener for stopping processes
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """ does nothing but returns 200 just in case """
    return ('Nothing interesting here.', 200, None)

@app.route('/killswitch', methods=['POST'])
def print_test():
    """
    Send a POST request to bobarr-transmission:5000/killswitch
    OR localhost:5000/killswitch (with a JSON body with "action" key, value "kill" or "revive"
    """
    payload = request.get_json()

    if 'action' not in payload:
        return("No action in payload", 400, None)

    elif payload['action'] == 'kill':
        print("Action is kill")
        return("Killed Transmission", 200, None)

    elif payload['action'] == 'revive':
        print("Action is revive")
        return("Re/vived Transmission", 200, None)

    else:
        print("Action is unknown")
        return("Action not recognized")

    print(payload)
    return ("", 200, None)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
