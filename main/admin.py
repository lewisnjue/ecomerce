from django.contrib import admin
from .models import Product,Cart,CartItem,subscribedEmails
# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(subscribedEmails)
# modify the admin page please