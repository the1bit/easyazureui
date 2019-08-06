"""
This script runs the EasyAzureUI1 application using a development server.
"""
import time
time.sleep(5)

from os import environ

import json
import sys
import os.path

try:
    configFile = 'EasyAzureUI1/config/config.json'
    
    with open(configFile, 'r') as json_file:
        config = json.load(json_file)
    
    environ['AZURE_TENANT'] = config["tenant"]
    environ['AZURE_DEFAULTSUBSCRIPTION'] = config["default_subscription"]
    environ['AZURE_CLIENTID'] = config["client_id"]
    environ['AZURE_CLIENTSECRET'] = config["client_secret"]
    if config["resource"][-1] != "/":
        environ['AZURE_RESOURCE'] = config["resource"] + "/"
    else:
        environ['AZURE_RESOURCE'] = config["resource"]
    
    if config["authority_url"][-1] != "/":
        environ['AZURE_AUTHORITYURL'] = config["authority_url"] + "/"
    else:
        environ['AZURE_AUTHORITYURL'] = config["authority_url"]


    from EasyAzureUI1 import app

    if __name__ == '__main__':
        HOST = environ.get('SERVER_HOST', '0.0.0.0')
        try:
            PORT = int(environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555
        app.run(HOST, PORT)
except Exception as e:
    import sys
    print(e)
    errorlog = open('error.log','w')
    errorlog.write(e)




