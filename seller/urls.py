from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='seller_add_product'),
    path('view_products/', views.view_products, name='seller_view_products'),
    path('sellercategory/<int:category_id>/', views.view_seller_category_products, name='view_seller_category_products'),
    path("addcategory/",views.addcategory,name="seller_addcategory"),
    path('update/<int:productid>/',views.update_product,name="update_product"),
    path('sellerproductdelete/<int:productid>/',views.delete_product,name="delete_product"),
    
]
