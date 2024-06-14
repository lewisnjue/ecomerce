from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cart,CartItem

@receiver(post_save,sender=User)
def createcart(sender,instance,created,*args,**kwargs):
    if created:
        Cart.objects.create(user=instance)
    


