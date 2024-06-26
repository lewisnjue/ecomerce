from django.db import models
from django.contrib.auth.models import User
# Create your models here.



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
