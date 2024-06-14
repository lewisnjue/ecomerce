from django.shortcuts import render
from .models import Product
from .forms import registeruser
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    products=Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')

def single(request,id):
    product = Product.objects.get(pk=id)

    return render(request,'single-product.html',{
        'product':product
    })


def Register(request):
    return render(request,'register.html',{
        'form':registeruser()
    })

def loginview(request):
    return render(request,'login.html')

