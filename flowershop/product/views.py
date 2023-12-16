from django.shortcuts import render
from rest_framework import generics, status, permissions
import logging
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from rest_framework.viewsets import GenericViewSet

from _auth.permissions import ManagerPermission, AdminPermission
from product.models import Category, Flower
from product.serializers import CateogriesSerializer, FlowerSerializer, FlowerNewSerializer


logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = AllowAny
    # queryset = Book.objects.all()
    # serializer_class = EventSerializer
    queryset = Category.objects.all()
    serializer_class = CateogriesSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [ManagerPermission]
        return [permission() for permission in permission_classes]
    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Category object created, ID: {serializer.instance} by {self.request.user.username}')



    #
    # def get_queryset(self):
    #     return Events.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return EventSerializer
    #     elif self.action == 'create':
    #         return EventSerializer
    #     return FullEventSerializer


# @api_view(['GET', 'POST'])
# def categories_view(request):
#     if request.method == 'GET':
#         category_items = Category.objects.all()
#         serializer = CateogriesSerializer(category_items, many=True)
#         return Response(serializer.data, status=200)
#     elif request.method == 'POST':
#         serializer = CateogriesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=500)

# class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CateogriesSerializer


# class CategoryFlowers(generics.ListCreateAPIView):
#     queryset = Flower.objects.all()
#     serializer_class = FlowerSerializer


class CategoryFlowerViewSet(
                  viewsets.GenericViewSet):
    queryset = Flower.objects.all()
    lookup_field = 'pk'
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [AllowAny]

    def list(self, request, pk):
        queryset = Flower.objects.filter(category_id=pk)
        logger.debug('Category Flowers')
        serializer = FlowerNewSerializer(queryset, many=True)
        return Response(serializer.data)


class FlowerViewSet(viewsets.ModelViewSet):
     serializer_class = FlowerNewSerializer
     queryset = Flower.objects.all()
     parser_classes = [MultiPartParser, FormParser, JSONParser]

     def get_permissions(self):
         if self.action == 'list':
             permission_classes = [AllowAny]
         elif self.action == 'retrieve':
             permission_classes = [AllowAny]
         else:
             permission_classes = [ManagerPermission]
         return [permission() for permission in permission_classes]

     def perform_create(self, serializer):
         serializer.save()
         logger.debug(f'Flower object created, ID: {serializer.instance} by {self.request.user.username}')

     @action(methods=['GET'], detail=False, url_path='unavailable', permission_classes =(ManagerPermission),)
     def not_active(self, request):
         logger.debug('unavailable flowers')
         queryset = Flower.objects.filter(available=False)
         serializer = FlowerNewSerializer(queryset, many=True)
         return Response(serializer.data)


