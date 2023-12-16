from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
from rest_framework import serializers
from _auth.models import Customer, Manager, User, CustomerProfile, ManagerProfile
from ordering.serializer import OrderSerializer, OrderCustomerSerializer
from events.serializers import EventSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name',  'last_name', 'role')


class CustomerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Customer
        fields = UserSerializer.Meta.fields + ('username', 'email', 'data_joined', 'customer_type', 'location')


class ManagerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Manager
        fields = UserSerializer.Meta.fields + ('username', 'email', 'data_joined', 'salary',
                                               'is_staff', 'is_superuser')

class ManagerProfileSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer()
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = ManagerProfile
        fields = '__all__'

class CustomerProfileSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    related_orders = OrderCustomerSerializer(many=True, read_only=True)

    class Meta:
        model = CustomerProfile
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    encoder = BCryptSHA256PasswordHasher()
    class Meta:
        model = Customer
        fields = ('username', 'password', 'email', 'first_name')
    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = self.encoder.encode(password, salt=self.encoder.salt())
        user = Customer.objects.create(password=hashed_password,  role= 3, **validated_data)
        user.save()
        return user

class RegisterManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    encoder = BCryptSHA256PasswordHasher()
    class Meta:
        model = Manager
        fields = ('username', 'password', 'email', 'first_name')
    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = self.encoder.encode(password, salt=self.encoder.salt())
        user = Manager.objects.create(password=hashed_password, role=2, **validated_data)
        user.save()
        return user