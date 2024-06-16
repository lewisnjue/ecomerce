from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Cart,CartItem
from .forms import registeruser
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    products=Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def cart(request):
    user = request.user
    cart_ = Cart.objects.get(user_id=user.id)
    items =cart_.items.all()
    return render(request,'cart.html',{
        'items':items
    })

@login_required(login_url='login')
def checkout(request):
    return render(request,'checkout.html')

def single(request,id):
    product = Product.objects.get(pk=id)

    return render(request,'single-product.html',{
        'product':product
    })


def Register(request):
    if request.method == 'POST':
        form = registeruser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
             messange = messages.error(request,'something went wrong please try agin ')
             return render(request,'register.html',{
        'form': form,
        "messange":messange
    })
    return render(request,'register.html',{
        'form':registeruser()
    })


def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to the home page or another appropriate page
        else:
            messages.error(request, 'Please enter valid credentials!')
    
    return render(request, 'login.html')

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addtocart(request, id, quantity):
    mycart = Cart.objects.get(user_id=request.user.id)
    myproduct = get_object_or_404(Product, id=id)
    quantity = int(quantity)
    
    # Check if the product is already in the cart
    cart_item = CartItem.objects.filter(cart=mycart, product=myproduct).first()
    
    if cart_item:
        # Increase the quantity of the existing cart item
        cart_item.quantity += quantity
        cart_item.save()
    else:
        # Create a new cart item
        CartItem.objects.create(cart=mycart, product=myproduct, quantity=quantity)
    
    # Redirect to the previous page
    previous_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_url)


@login_required(login_url='login')
def addtocart2(request):
    if request.method == 'POST':
        mycart = Cart.objects.get(user_id=request.user.id)
        myproduct = get_object_or_404(Product, id=request.POST.get('id'))
        quantity = int(request.POST.get('number'))
        cart_item = CartItem.objects.filter(cart=mycart, product=myproduct).first()
        
        if cart_item:
            # Increase the quantity of the existing cart item
            cart_item.quantity += quantity
            cart_item.save()
        else:
            # Create a new cart item
            CartItem.objects.create(cart=mycart, product=myproduct, quantity=quantity)

    previous_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_url)
