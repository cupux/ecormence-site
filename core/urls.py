from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    CheckoutView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_from_cart,
    PaymentView,
    Chargess,
    home,
    AddCouponView,
    RequestRefundView,
    search
)
app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(), name="index"),
    path('home/',home, name="home"),
    path('checkout/',CheckoutView.as_view(), name="checkout"),
    path('product/<slug>/',ItemDetailView.as_view(), name="product"),
    path('add_to_cart/<slug>/',add_to_cart, name="add_to_cart"),
    path('add_coupon/',AddCouponView.as_view(), name="add_coupon"),
    path('remove_from_cart/<slug>/',remove_from_cart, name="remove_from_cart"),
    path('order_summary/',OrderSummaryView.as_view(), name="order_summary"),
    path('payment/<payment_option>/',PaymentView.as_view(), name="payment"),
    path('remove_single_from_cart/<slug>/',remove_single_from_cart, name="remove_single_from_cart"),
    path('charge/',Chargess, name="charge"),
    path('request_refund/',RequestRefundView.as_view(), name='request_refund'),
    path('search/',search, name="search"),

]