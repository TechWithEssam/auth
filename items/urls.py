from django.urls import path
from . import views


app_name = "items"
urlpatterns = [
    path("cart/", views.cart_customer_view, name="cart"),
    path('add-to-cart/', views.add_to_cart_view, name="add_to_cart")
]