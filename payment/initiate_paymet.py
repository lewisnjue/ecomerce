import requests 
from . import generate_token
from django.conf import settings 
import datetime
import base64

def initiate_payment():
    # Generate Timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    print(timestamp)
    
    # Generate Password
    password = base64.b64encode(f"{settings.MPESA_SHORTCODE}{settings.PASSKEY}{timestamp}".encode()).decode('utf-8')
    
    headers = {
        'Authorization': f'Bearer {generate_token.get_token()}',
        'Content-Type': 'application/json'
    }
    
    body = {
        "BusinessShortCode": 174379,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254708374149",  # Customer's phone number
        "PartyB": settings.MPESA_SHORTCODE,  # Your PayBill number (e.g., 174379 in sandbox)
        "PhoneNumber": "254708374149",  # Same as PartyA
        "CallBackURL": "https://yourdomain.com/callback",  # Replace with your callback URL
        "AccountReference": "Order001",  # Unique identifier for the transaction
        "TransactionDesc": "Payment for Order 001"
    }
    
    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
   
    response = requests.post(url, headers=headers, json=body)
    return response.json()
