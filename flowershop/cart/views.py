from decimal import Decimal
import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from _auth.permissions import ManagerPermission, CustomerPermission
from product.models import Flower
from product.serializers import FlowerSerializer


logger = logging.getLogger(__name__)

class CartList(APIView):
    permission_classes = [CustomerPermission]
    def get(self, request):
        if request.session.get('cart'):
            id_list = [data_dict.get('pk') for data_dict in request.session['cart'].values()]
        else:
            return Response('no item in the cart', status=200)

        cart = request.session.get('cart')
        flowers = Flower.objects.filter(pk__in = id_list)

        for flower in flowers:
            cart[str(flower.pk)]['total_product_price'] = float(cart[str(flower.pk)]['quantity'] * flower.price)
            serializer = FlowerSerializer(flower)
            cart[str(flower.pk)]['flower'] = serializer.data
        cart['total_price'] = request.session['total_price']
        return Response(cart, status=200)


class AddtoCart(APIView):
    permission_classes = [CustomerPermission]
    def post(self, request, pk):
        if not request.session.get('cart'):
            request.session['cart'] = dict()
        else:
            request.session['cart'] = dict(request.session['cart'])
        exist = request.session['cart'].get(str(pk))
        product = Flower.objects.get(id= pk)
        serializer = FlowerSerializer(product)
        add_data = {
            'pk': pk,
            'quantity': int(request.POST['quantity']),
            'flower': serializer.data
        }
        if not exist:
            request.session['cart'][str(pk)] = add_data  # {pk:{}, pk:{}, pk:{}}
            request.session['cart'][str(pk)]['total_product_price'] = float(product.price)

        else:
            item_pk = exist['pk']
            request.session['cart'][str(item_pk)]['quantity'] = request.session['cart'][str(item_pk)]['quantity'] + int(
                request.POST.get('quantity'))
            request.session['cart'][str(item_pk)]['total_product_price'] = float(product.price *  request.session['cart'][str(item_pk)]['quantity'])

        cart = request.session['cart']
        total_price = sum([cart_item['total_product_price'] for cart_item in cart.values()])
        request.session['total_price'] = total_price

        request.session.modified = True
        logger.info(f'Cart, ID:{serializer.instance} was created')
        return Response(add_data, status= status.HTTP_201_CREATED)



