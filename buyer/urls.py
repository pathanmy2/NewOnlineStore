from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse_products, name='browse_products'),
    path('category/<int:category_id>/', views.view_category_products, name='view_category_products'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path("logout/",views.logout_view,name="logout"),
    path("delete/<int:product_id>/",views.delete,name="delete"),
]
