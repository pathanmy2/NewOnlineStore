
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
@login_required
def add_product(request):
    if request.method == 'POST':
        seller = request.user
        print(seller,"================================seller login=======")
        category_id = request.POST['category']
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES['image']
        product = Product.objects.create(seller=seller, category_id=category_id, name=name,
                                         description=description, price=price, stock=stock, image=image)
        
        return redirect('seller_view_products')
    else:
        # Retrieve categories for dropdown
        categories = Category.objects.all()
        return render(request, 'add_product.html', {'categories': categories})

@login_required
def view_products(request):
    if request.method=="GET":
        search=request.GET.get("search")
        if search:
            seller_products = Product.objects.filter(seller=request.user,name__icontains=search)
        else:
            seller_products = Product.objects.filter(seller=request.user)
    categories = Category.objects.all()
    
    return render(request, 'view_products.html', {'products': seller_products,"categories":categories})

def view_seller_category_products(request, category_id):
    # categories = Category.objects.all()
    products = Product.objects.filter(seller=request.user,category_id=category_id, stock__gt=0)
    return render(request, 'view_products.html', {'products': products})
@login_required
def addcategory(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST['name'])

        return redirect('seller_add_product')
    else:
    # Retrieve categories for dropdown
        categories = Category.objects.all() 
        return render(request, 'add_category.html', {'categories': categories})


def update_product(request, productid):
    product = get_object_or_404(Product, pk=productid, seller=request.user)
    categories = Category.objects.all()

    if request.method == "POST":
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')

        # Update the product fields
        product.category_id = category_id
        product.name = name
        product.description = description
        product.price = price
        product.stock = stock
        if image:
            product.image = image

        product.save()
        
        return redirect('seller_view_products')
    
    
    else:
        productobj=Product.objects.get(id=productid)
        categories = Category.objects.all()
        return render(request, 'add_product.html', {'categories': categories,"products":productobj})
    
def delete_product(request,productid):

    product = get_object_or_404(Product, pk=productid, seller=request.user)
    product.delete()
    return redirect('seller_view_products')