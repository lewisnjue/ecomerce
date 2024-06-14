from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')

def single(request):
    return render(request,'single-product.html')
