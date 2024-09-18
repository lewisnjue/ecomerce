from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('single/<int:pk>',views.single.as_view(),name='single'),
    path('register',views.Register,name='register'),
    path('login',views.loginview,name='login'),
    path('logout',views.logoutview,name="logout"),
    path('addtocart',views.addtocart, name='addtocart'),
    #password reseting 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('subscribe',views.subscribe,name="subscribe"),
    path('search',views.product_search,name="search"),
    path('sendadminmail',views.sendadminmail,name='sendadminmail'),

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

