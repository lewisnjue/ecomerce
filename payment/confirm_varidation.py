
import requests
from .import generate_token
from django.conf import settings
def confirm_varidation():
    headers = {
        'Authorization': f'Bearer {generate_token.get_token()}',
        'Content-Type':'application/json'
        }
    body = {
        "ShortCode": settings.MPESA_SHORTCODE,
        "ResponseType": "Completed",
        "ConfirmationURL": "http://localhost:8000/payments/confirm",
        "ValidationURL": "http://localhost:800/payments/validate"
    }
    url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
    requests.post(url,json=body,headers=headers)

