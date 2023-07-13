# from django.shortcuts import render,redirect
# from .models import Product, Order
# from seller.models import Category
# from buyer.models import Buyer
from django.shortcuts import render, redirect
from .models import Product, Order, Buyer
from seller.models import Category
from django.contrib.auth import logout

def browse_products(request):
    count=0
    if request.method=="GET":
        search=request.GET.get("search")
        if search:
            products = Product.objects.filter(name__icontains=search).exclude(stock=0)
        else:
            products = Product.objects.exclude(stock=0)
    if request.user.is_authenticated:
        try:
            order_len=Order.objects.get(buyer__user=request.user)
            count=order_len.products.all().count()
        except:
            pass
    else:
        count=0
    categories = Category.objects.all()
    

    return render(request, 'browse_products.html', {'categories': categories, 'products': products,"login":request.user.is_authenticated,"orderscount":count})

def view_category_products(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id, stock__gt=0)
    return render(request, 'browse_products.html', {'categories': categories, 'products': products})

def add_to_cart(request, product_id):
   
    if request.user.is_authenticated:
        buyer,created = Buyer.objects.get_or_create(user=request.user)
        buyer.save()
        product = Product.objects.get(pk=product_id)
        
        order, created = Order.objects.get_or_create(buyer=buyer)
        
        order.products.add(product)
        return redirect('browse_products')
    else:
        return redirect("login")
    

# def viewSure! Here's the remaining code for views and templates:

# **Views (continued):**

# ```python
# # buyer/views.py
def view_cart(request):
    if request.user.is_authenticated:
        print(request.user,"======request.user")
        buyer = Buyer.objects.get(user=request.user)
        order = Order.objects.filter(buyer=buyer).last()
        categories = Category.objects.all()
        order = Order.objects.filter(buyer=buyer).last()
        order_len=Order.objects.get(buyer__user=request.user)
        count=order_len.products.all().count()
        return render(request, 'view_cart.html', {'order': order,'categories': categories,"orderscount":count})
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    categories = Category.objects.all()
    products = Product.objects.exclude(stock=0)
    return redirect('browse_products')
    # return render(request, 'browse_products.html', {'categories': categories, 'products': products,"login":request.user.is_authenticated})
def delete(request, product_id):
    categories = Category.objects.all()
    ord = Order.objects.get(buyer__user=request.user)
    productobj=Product.objects.get(id=product_id)
    productobj.stock=productobj.stock+1
    productobj.save()
    ord.products.remove(productobj)
    ord.save()
    buyer = Buyer.objects.get(user=request.user)
    order = Order.objects.filter(buyer=buyer).last()
    order_len=Order.objects.get(buyer__user=request.user)
    count=order_len.products.all().count()
    return render(request, 'view_cart.html', {'order': order,'orderscount':count,"categories":categories})
    
    