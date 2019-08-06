import adal
import requests
import os
import json
from os import environ


tenant = environ['AZURE_TENANT']
authority_url = environ['AZURE_AUTHORITYURL'] + tenant
client_id = environ['AZURE_CLIENTID']
client_secret = environ['AZURE_CLIENTSECRET']
resource = environ['AZURE_RESOURCE']


######## FUNCTIONS


def get_context_and_token():
    context = adal.AuthenticationContext(authority_url)
    token = context.acquire_token_with_client_credentials(resource, client_id, client_secret)
    result = []
    result.append(context)
    result.append(token)
    return result


def get_subscriptions_data(token):
    headers = {'Authorization': 'Bearer ' + token['accessToken'], 'Content-Type': 'application/json'}
    params = {'api-version': '2016-06-01'}
    url = resource + 'subscriptions'
    r = requests.get(url, headers=headers, params=params)

    return r.json()["value"]


def get_vms_all(token, subscriptionId):
    headers = {'Authorization': 'Bearer ' + token['accessToken'], 'Content-Type': 'application/json'}
    params = {'api-version': '2018-06-01'}
    url = resource + 'subscriptions/' + subscriptionId + '/providers/Microsoft.Compute/virtualMachines'
    r = requests.get(url, headers=headers, params=params)
    
    return r.json()["value"]


def get_resourcegroups(token, subscriptionId):
    headers = {'Authorization': 'Bearer ' + token['accessToken'], 'Content-Type': 'application/json'}
    params = {'api-version': '2017-05-10'}
    url = resource + 'subscriptions/' + subscriptionId + '/resourcegroups'
    r = requests.get(url, headers=headers, params=params)

    return r.json()["value"]


