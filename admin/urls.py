from django.urls import path
from . import views


urlpatterns = [
    path('view_sellers/', views.view_sellers, name='admin_view_sellers'),
    path('admin_view_products/', views.view_products, name='admin_view_products'),
    path('view_buyers/', views.view_buyers, name='admin_view_buyers'),
    path('view_orders/', views.view_orders, name='admin_view_orders'),
]
