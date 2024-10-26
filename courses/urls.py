from django.urls import path
from .views import courses, add_to_cart, cart, remove_from_cart,search_products

urlpatterns = [
    path('', courses, name='courses'),
    path('add_to_cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('remove_from_cart/<int:id>', remove_from_cart, name='remove_from_cart'),
    path('search/', search_products, name='search'),
]
