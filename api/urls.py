from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('generatetoken',obtain_auth_token,name='generatetoken'),
    path('checkoutorder/<username>',views.checkorder,name='checkoutorder')

]