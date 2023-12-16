from django.urls import path
from rest_framework import routers

from cart.views import CartList, AddtoCart
urlpatterns = [
    path('', CartList.as_view()),
    path('post/<int:pk>', AddtoCart.as_view())

]