# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from _auth.models import Customer
from _auth.permissions import ManagerPermission, CustomerPermission
from ordering.models import Order, OrderItem
from ordering.serializer import OrderSerializer, OrderItemSerializer, OrderListrSerializer
from product.models import Flower
import logging

logger = logging.getLogger(__name__)





class OrdersViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [ManagerPermission]
    queryset = Order.objects.get_related()
    serializer_class = OrderListrSerializer

@api_view(['POST'])
@permission_classes([CustomerPermission])
def order_view(request):
    # del request.session['cart']
    # return Response("ok", status=201)
    order = OrderSerializer()
    customer = Customer.objects.get(username=request.user)
    session_key = request.session.session_key
    # cart = request.session.get('cart')
    # print(type(cart))
    total_price = request.session['total_price']
    context = {
        "total_price": total_price,
        "customer": customer
    }
    try:
        order = Order.objects.create(customer = customer, total_price=total_price,
                         comment=request.data["comment"], session_key=session_key)

        # order = OrderSerializer(data = request.data, context = context )

        # products = Flower.objects.filter(pk__in=cart.keys())
        # for product in products:
        #     cart[str(product.id)]['flower'] = product
        #
        # for item in cart.values():
        #     # flower = Flower.objects.create(flower = item['flower'])
        #     order_item = OrderItem.objects.create(order=order,
        #                              flower=item['flower'],
        #                              quantity=item['quantity']
        #                              )
        #
        # result = OrderItem.objects.filter(order=order.id)

        serializer = OrderSerializer(order)
        del request.session['cart']
        logger.info(f'Order object created, ID: {serializer.instance}')
        return Response(serializer.data, status=201)
    except:
        logger.error(f'Order object was not created')
        return Response('Serializer error', status=500)