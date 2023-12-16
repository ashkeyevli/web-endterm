from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from _auth.models import Customer, Manager
from _auth.permissions import ManagerPermission, AdminPermission, CustomerPermission
from _auth.serializers import RegisterSerializer, UserSerializer, CustomerSerializer, ManagerSerializer, \
    CustomerProfileSerializer, ManagerProfileSerializer, RegisterManagerSerializer
from rest_framework import mixins, viewsets



class RegisterAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer


class CustomersViewSet(mixins. ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [ManagerPermission]
    queryset = Customer.objects.get_related()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        elif self.action == 'retrieve':
            return CustomerProfileSerializer
        return CustomerSerializer

    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes = (CustomerPermission,)
        else:
            permission_classes = (ManagerPermission,)

        return [permission() for permission in permission_classes]


class ManagersViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminPermission]
    queryset = Manager.objects.get_related()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        elif self.action == 'create':
            return RegisterManagerSerializer
        elif self.action == 'retrieve':
            return ManagerProfileSerializer

        return ManagerSerializer


class profileAPIView(APIView):
    def get(self, request):
        customer = Customer.objects.get(username=request.user)
        serializer = CustomerProfileSerializer(customer)
        return Response(serializer.data)