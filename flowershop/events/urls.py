from django.urls import path
from events.views import EventViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', EventViewSet)


urlpatterns = router.urls