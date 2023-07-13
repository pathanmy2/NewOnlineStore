from django.shortcuts import render

# Create your views here.
from seller.models import Seller, Product, Category
from buyer.models import Buyer, Order

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from Users.forms import RegisterForm
def register(request):
    print(request.POST,"=======request")
    categories = Category.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(form,"=============form===")
        if form.is_valid():
            print("welcome form")
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form,"categories":categories})



# def user_login(request):
#     categories = Category.objects.all()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('browse_products')  
#         else:
#             return render(request, 'login.html', {'error_message': 'Invalid username or password',"categories":categories})
#     else:
#         return render(request, 'login.html',{"categories":categories})


def user_login(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.account_type == 'Seller':
                return redirect('seller_view_products')  # Redirect to the seller dashboard
            elif user.account_type == 'Admin':
                return redirect('admin_view_products')  # Redirect to the admin dashboard
            else:
                return redirect('browse_products')  # Redirect to the normal user page
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password', "categories": categories})
    else:
        return render(request, 'login.html', {"categories": categories})

