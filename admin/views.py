
# from django.shortcuts import render
# from seller.models import Seller, Product
# from buyer.models import Buyer, Order
from seller.models import Seller, Product, Category
from buyer.models import Buyer, Order

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# from buyer.urls import buyer_browse_products

def view_sellers(request):
    sellers = Seller.objects.all()
    return render(request, 'view_sellers.html', {'sellers': sellers})

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_admin.html', {'products': products})

def view_buyers(request):
    buyers = Buyer.objects.all()
    return render(request, 'view_buyers.html', {'buyers': buyers})

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'view_orders.html', {'orders': orders})

