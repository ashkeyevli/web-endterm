from rest_framework import serializers

from product.models import Category, Flower


class CateogriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    image = serializers.ImageField()

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class FlowerNewSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    color = serializers.CharField()
    stock = serializers.IntegerField()
    available = serializers.BooleanField()

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Цена должна быть больше нуля')
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('Скидка должна быть больше нуля')
        return value

    def create(self, validated_data):
        flower = Flower.objects.create(**validated_data)
        return flower

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.color = validated_data.get('color', instance.color)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Цена должна быть больше нуля')
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('Скидка должна быть больше нуля')
        return value
