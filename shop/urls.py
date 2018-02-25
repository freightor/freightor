from django.urls import path
from shop import views

app_name = "shop"
urlpatterns = [
    path("", views.shop_home, name="shop_home"),
    path("store/products/", views.product_list, name="product_list"),
    path("store/orders/", views.order_list, name="order_list"),
    path("store/products/add/", views.new_product, name="new_product"),
    path("products/<uuid:pk>/", views.product_detail, name="product_detail"),
    path("store/products/<uuid:pk>/", views.merchant_product_detail, name="merchant_product_detail"),
    path("store/products/<uuid:pk>/edit/", views.edit_product, name="edit_product"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/<uuid:pk>/add/", views.cart_add, name="cart_add"),
    path("cart/<uuid:pk>/remove/", views.cart_remove, name="cart_remove"),
    path("cart/checkout/", views.cart_checkout, name="checkout"),
    path("store/add/", views.new_store, name="new_store"),
    path("store/edit/", views.edit_store, name="edit_store"),
]
