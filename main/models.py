from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='product_images',blank=False,null=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100,decimal_places=2)
    