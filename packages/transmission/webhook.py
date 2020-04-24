#!/usr/bin/env python
"""
Simple webhook listener for stopping processes
"""
import subprocess
from flask import Flask, request

app = Flask(__name__)


def parse_request(req):
    """
    Parses application/json request body data into a Python dictionary
    """
    payload = req.get_json()
    return payload

def perform_action(action, dirname, pname):
    """
    Action
    """
    doaction = subprocess.run(["./s6-action.sh", action, dirname, pname], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return(doaction.stderr)


@app.route('/', methods=['GET'])
def index():
    """ does nothing but returns 200 just in case """
    return ('Nothing interesting here.', 200, None)

@app.route('/killswitch', methods=['POST'])
def print_test():
    """
    Send a POST request to localhost:5000/killswitch (with a JSON body with "action" key, value "kill" or "start"
    """
    payload = parse_request(request)

    if 'action' and 'dirname' and 'pname' in payload:
        doaction = perform_action(payload['action'], payload['dirname'], payload['pname'])
        return(doaction, 200, None)
    else:
        return("Missing action, dirname, or pname key(s)", 400, None)

    print(payload)
    return ("", 200, None)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
