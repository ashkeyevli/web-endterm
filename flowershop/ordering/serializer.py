from rest_framework import serializers

from ordering.models import OrderItem, Order




class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('total_price', 'comment', 'created_at', 'order_date', 'delivery_type', 'status', 'items')

    def validate_total_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Вы не заказали ничего')
        return value

class OrderCustomerSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('total_price', 'comment', 'created_at', 'order_date', 'delivery_type', 'status', 'items')

    def validate_total_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Вы не заказали ничего')
        return value

class OrderListrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer','total_price', 'comment', 'created_at', 'order_date', 'delivery_type', 'status')
    def validate_total_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Вы не заказали ничего')
        return value

