from django.shortcuts import render
import logging
# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from _auth.models import Manager
from _auth.permissions import ManagerPermission
from events.models import Event
from events.serializers import EventSerializer, FullEventSerializer

logger = logging.getLogger(__name__)
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        elif self.action == 'retrieve':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (ManagerPermission,)

        return [permission() for permission in permission_classes]

    @action(methods=['POST'], detail=False, url_path='create', permission_classes=(ManagerPermission,))
    def create_event(self, request):
        manager = Manager.objects.get(id = request.user.id)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(manager=manager)
            serializer.save()
            logger.info(f'Event object was created, ID:{serializer.instance.id}')
            return Response(serializer.data, status=201)
        logger.warning(f'Event object was not created by {manager.username}')
        logger.error(f'Server error')
        return Response(serializer.errors, status=500)
