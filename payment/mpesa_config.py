
from django.conf import settings
MPESA_ENVIRONMENT = settings.MPESA_ENVIRONMENT  
# Sandbox credentials
CONSUMER_KEY = settings.MPESA_CONSUMER_KEY
CONSUMER_SECRET = settings.MPESA_CONSUMER_SECRET

BUSINESS_SHORTCODE = settings.BUSINESS_SHORTCODE
LIPA_NA_MPESA_ONLINE_SHORTCODE = ''  # For sandbox
PASSKEY = settings.PASSKEY

# URLs
MPESA_API_BASE_URL = 'https://sandbox.safaricom.co.ke' if MPESA_ENVIRONMENT == 'sandbox' else 'https://api.safaricom.co.ke'
CONFIRMATION_URL = 'https://localhost/payments/<>/confirmation' # finish later
VALIDATION_URL = 'https://yourdomain.com/api/v1/validation'