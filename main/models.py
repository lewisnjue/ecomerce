from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from PIL import  Image
from django.core.files.uploadedfile import   SimpleUploadedFile
from io import BytesIO
import io 
""" 
the above three imporrs 
image, simpleuploaded files and bytesio are used for image manipulation 
in my project 
lets go 
 """
class ProductManager(models.Manager):
    def search(self, query):
        return self.filter(name__icontains=query)
    

class Product(models.Model):
    image = models.ImageField(upload_to='product_images', blank=False, null=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name
        
    objects = ProductManager()
    def save(self,*args,**kwargs):
        if self.image and not self.image.name.endswith('.webp'):
            img = Image.open(self.image)
            # convert the image to webp
            img_io = BytesIO() # creating an inmemory place to save my image 
            img.save(img_io,format='WEBP',quality=85) # saving image tempolary to the inmemroy place 
            # get the file name and covert to web extension 
            image_name = f'{self.image.name.rsplit(".",1)[0]}.webp'
            # save the webp image in place of the original one 
            self.image = SimpleUploadedFile(name=image_name,content=img_io.getvalue(),content_type='image/webp')


        super().save(*args,**kwargs)
        #  that is perfect now 


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='cart')
    def __str__(self) -> str:
        return self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Ensures positive quantity

    # Calculate the total price for each CartItem instance
    @property
    def total(self):
        return self.quantity * self.product.price

    # Consider adding a method to save the total for efficiency (optional)
    def save(self, *args, **kwargs):
        # you can do here your thing before savingthe cart item 
        super().save(*args, **kwargs)  # Call the parent's save method

    def __str__(self) -> str:
        return f'this cart belong to {self.cart.user.username}'

class subscribedEmails(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email
