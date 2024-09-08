from django.shortcuts import render
from django.http import JsonResponse
from .mpesa_client import MpesaClient
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def initiate_payment(request):
    if request.method == 'POST':
        phone_number = request.POST['phone']
        amount = request.POST['amount']
        account_reference = settings.BUSINESS_SHORTCODE  # Your Account Number
        transaction_desc = 'Payment for goods'
        callback_url = 'https://localhost:8000/payments/callback/'  # Ensure this URL is publicly accessible

        mpesa_client = MpesaClient(
            consumer_key=settings.MPESA_CONSUMER_KEY,
            consumer_secret=settings.MPESA_CONSUMER_SECRET,
            shortcode=settings.MPESA_SHORTCODE,
            passkey=settings.PASSKEY
        )
        response = mpesa_client.lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(response)

    return render(request, 'payments/initiate_payment.html')

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        mpesa_response = request.body
        # Process the M-Pesa response here, e.g., save it to the database
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
    return JsonResponse({"ResultCode": 1, "ResultDesc": "Rejected"})
