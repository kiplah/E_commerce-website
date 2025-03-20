from django.urls import path
from . import views
from .views import cart_view, add_to_cart, remove_from_cart

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_view, name='cart'),  # 👈 Moved this above category slug
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),  # 👈 Keep this last

    
]
