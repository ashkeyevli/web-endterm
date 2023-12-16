from django.urls import path
from rest_framework import routers

from ordering.views import order_view, OrdersViewSet

router = routers.SimpleRouter()
router.register('', OrdersViewSet)

urlpatterns = [
    path('create', order_view),

]
urlpatterns += router.urls