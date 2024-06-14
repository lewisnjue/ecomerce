from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path ('about',views.about,name='about'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('single/<int:id>',views.single,name='single'),
    path('register',views.Register,name='register'),
    path('login',views.loginview,name='login')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
