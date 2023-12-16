from rest_framework import generics, status
import logging
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from _auth.models import Customer, Manager
from _auth.permissions import ManagerPermission, CustomerPermission
from review.models import Review
from review.serializers import ReviewSerializer, ReplySerializer, ReviewFullSerializer


logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([CustomerPermission])
def reviewCreate_view(request):
    customer = Customer.objects.get(id = request.user.id)
    if request.method == 'POST':
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(customer=customer)
            serializer.save()
            logger.debug(f'Review object created, ID: {serializer.instance}')
            return Response(serializer.data, status=201)
        logger.warning(f'Review object was not created')
        logger.error(f'Server error')
        return Response(serializer.errors, status=500)


@api_view(['POST'])
@permission_classes([ManagerPermission])
def replyCreate_view(request, pk):
    review = Review.objects.get(id=pk)
    manager = Manager.objects.get(id = request.user.id)

    if request.method == 'POST':
        serializer = ReplySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(manager=manager, review = review)
            serializer.save()
            logger.debug(f'Reply object created, ID: {serializer.instance}')
            return Response(serializer.data, status=201)
        logger.warning(f'Reply object was not created')
        logger.error(f'Server error')
        return Response(serializer.errors, status=500)


class reviewAPIView(generics.ListAPIView):
    queryset = Review.objects.get_related()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

class reviewFullAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.get_related()
    serializer_class = ReviewFullSerializer
    permission_classes = [IsAuthenticated]