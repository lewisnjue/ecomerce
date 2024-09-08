from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.starter, name='checkout'),
    path('confirm',views.confirm,name='confirm'),
    path('validate',views.validate,name='validate')
]