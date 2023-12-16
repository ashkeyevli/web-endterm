from django.urls import path
from rest_framework import routers

from product.views import CategoryViewSet, FlowerViewSet, CategoryFlowerViewSet

category_flowers = CategoryFlowerViewSet.as_view({
    'get': 'list'
})
router = routers.SimpleRouter()
router.register('flowers', FlowerViewSet ),
router.register('category', CategoryViewSet ),
urlpatterns = [
    path('category/<int:pk>/flowers', category_flowers),
]
urlpatterns += router.urls