from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.initiate_payment, name='checkout'),
    path('callback/', views.payment_callback, name='payment_callback'),  # Define the callback view later
]