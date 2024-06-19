from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cart,CartItem,Product,subscribedEmails
from django.core.mail import send_mail,send_mass_mail

@receiver(post_save,sender=User)
def createcart(sender,instance,created,*args,**kwargs):
    if created:
        Cart.objects.create(user=instance)
    


@receiver(post_save,sender=Product)
def notifyuser(sender,instance,created,*args,**kwargs):
    if created:
        subscribed_emails = subscribedEmails.objects.values_list('email', flat=True)
        subject = 'New Product Created'
        message = f'A new product "{instance.name}" has been added to our store!'
        from_email = 'lewiskinyuanjue.ke@gmail.com'

        messages = [
            (subject, message, from_email, [email]) for email in subscribed_emails
        ]

        send_mass_mail(messages, fail_silently=False)
        # this method has more performarce for more messanges that send_mail class method 
        