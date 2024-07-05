from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('products',views.products,name='products'),
    path('secret',views.secret,name='secret'),
    path('generatetoken',obtain_auth_token,name='generatetoken')

]