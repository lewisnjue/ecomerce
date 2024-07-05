from rest_framework import serializers 
from main.models import Product 

class productserializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name','price']

