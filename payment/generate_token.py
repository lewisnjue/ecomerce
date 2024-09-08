from django.conf import settings
import requests 
from requests.auth import HTTPBasicAuth
def get_token():
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    username = settings.MPESA_CONSUMER_KEY
    password = settings.MPESA_CONSUMER_SECRET
    access_token = requests.get(url,auth=HTTPBasicAuth(username,password)).json()['access_token']
    return access_token