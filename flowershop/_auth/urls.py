from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from _auth.views import CustomersViewSet, RegisterAPIView, ManagersViewSet, profileAPIView


router = routers.SimpleRouter()
router.register('customers', CustomersViewSet),
router.register('managers', ManagersViewSet),
# router.register('profile', profileViewSet),


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('profile/', profileAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
]

urlpatterns += router.urls