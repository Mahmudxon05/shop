from django.urls import path
from .views import *
#---------  URL -----------#
urlpatterns = [    
    path('product/',product_view),
    path('category/',category_view),
    path('rootcategory/',root_category_view),
    path('subcategory/',sub_category_view),
    path('size/',size_view),
    path('color/',color_view),
    path('productlist/', ProductList.as_view()),
    path('create-cart/<int:pk>/', create_cart),
    path('create-oreder/', create_order),
    # path('cart/',cart_view),
    path('orderitems/<int:pk>/',order_item_view),
    path('delete-color/<int:pk>/',delete_color_view),
]   