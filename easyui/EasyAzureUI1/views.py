"""
Routes and views for the flask application.
"""

from datetime import datetime
import token
from EasyAzureUI1.modules.azure_rest_resources import get_subscriptions_data
from flask import render_template
from EasyAzureUI1 import app
from EasyAzureUI1.modules import azure_rest_resources as bitazrest

import datetime as bittime

import adal
import requests
import os
import json


# Check context and token
candt = bitazrest.get_context_and_token()
CONTEXT = candt[0]
TOKEN = candt[1]

# EXPIRES_ON = bittime.datetime.strptime(TOKEN["expiresOn"], '%Y-%m-%d %H:%M:%S.%f')

def refresh_token():
    global TOKEN
    global CONTEXT
    now = datetime.now()
    #print(TOKEN["expiresOn"]);
    token_expiration_time = datetime.strptime(TOKEN["expiresOn"], '%Y-%m-%d %H:%M:%S.%f')
    if now >= token_expiration_time:
        newtoken = bitazrest.get_context_and_token()
        TOKEN = newtoken[1]
        CONTEXT = newtoken[0]
        return True
    else:
        return False


@app.route('/')
@app.route('/home')
def home():
    refresh_token()    
    apiResult = bitazrest.get_subscriptions_data(TOKEN)

    return render_template(
        'index.html',
        title='Home Page',
        apiResult = apiResult,
        tokenExpiration = TOKEN["expiresOn"],
        year=datetime.now().year,
    )

@app.route('/resourcegroups')
def resourcegroups():
    refresh_token()    
    apiResult = bitazrest.get_resourcegroups(TOKEN, os.environ['AZURE_DEFAULTSUBSCRIPTION'])
    return render_template(
        'resourcegroups.html',
        title='Resource Group list',
        apiResult = apiResult,
        tokenExpiration = TOKEN["expiresOn"],
        year=datetime.now().year,
        message='Existing resource groups in this subscription:'
    )


@app.route('/vmlist')
def vmlist():
    refresh_token()    
    apiResult = bitazrest.get_vms_all(TOKEN, os.environ['AZURE_DEFAULTSUBSCRIPTION'])
    print(apiResult)
    return render_template(
        'vmlist.html',
        title='List VMs',
        apiResult = apiResult,
        tokenExpiration = TOKEN["expiresOn"],
        year=datetime.now().year,
        message='You have the following Virtual Machines in this subscription:'
    )


@app.errorhandler(500)
def internal_error(error):
    return render_template(
        'error.html',
        title='Error: 500',
        message='Something went wrong. HTTP 500 error.',
        error_message=error
    )
    #return "500 error"

@app.errorhandler(404)
def not_found(error):
    return render_template(
        'error.html',
        title='Error: 404',
        message='Page not found. HTTP 404 error.',
        error_message=error
    )
    #return "404 error",404
