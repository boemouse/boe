from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order
from .forms import CheckoutForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .forms import SignUpForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order(product=product, quantity=1)
    order.save()
    return render(request, 'store/cart.html', {'orders': Order.objects.all()})

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_confirmation')
    else:
        form = CheckoutForm()
    
    return render(request, 'store/checkout.html', {'form': form})

def order_confirmation(request):
    return render(request, 'store/order_confirmation.html')
	
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form': form})