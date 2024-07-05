from django.shortcuts import render
from main import models 
from rest_framework.response import Response 
from rest_framework.decorators import api_view,APIView
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,DestroyAPIView
from .serializer import productserializer

#public apis 
""" class products(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = productserializer """

@api_view(['GET'])
def products(request):
    items = models.Product.objects.all()
    search = request.query_params.get('search')
    price = request.query_params.get('price')
    if price:
        items = items.filter(price__lte=price)

    if search:
        items = items.filter(name__icontains=search)

    returnproducts = productserializer(items,many=True)
    return Response(returnproducts.data)


#any user api 






#private api 
