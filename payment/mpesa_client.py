import requests
from requests.auth import HTTPBasicAuth
import base64
import datetime
from django.conf import settings 
class MpesaClient:
    def __init__(self, consumer_key, consumer_secret, shortcode, passkey):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.shortcode = shortcode
        self.passkey = passkey

    def generate_access_token(self):
        api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        response = requests.get(api_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        json_response = response.json()
        return json_response['access_token']

    def lipa_na_mpesa_online(self, phone_number, amount, account_reference, transaction_desc, callback_url):
        access_token = self.generate_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(self.shortcode.encode() + self.passkey.encode() + timestamp.encode()).decode('utf-8')

        payload = {
            "BusinessShortCode": self.shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",  # Ensure this is correct for PayBill
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": self.shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": callback_url,
            "AccountReference": account_reference,  # This should be the account number (e.g., 1282488023)
            "TransactionDesc": transaction_desc
        }

        response = requests.post(api_url, json=payload, headers=headers)
        return response.json()
