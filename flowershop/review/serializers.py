from rest_framework import serializers

from _auth.serializers import CustomerSerializer, ManagerSerializer, ManagerProfileSerializer, UserSerializer
from review.models import Review, Comment, Reply


class postContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('description', 'created_date')


class ReviewSerializer(postContentSerializer):
    customer = CustomerSerializer(read_only=True)


    class Meta(postContentSerializer.Meta):
        model = Review
        fields = postContentSerializer.Meta.fields + ('id', 'title', 'rate', 'customer')

    def validate_rate(self, value):
        if value < 0:
            raise serializers.ValidationError('Рэйтинг должен быть больше нуля')
        return value

    def validate_title(self, value):
        cenzura = ['plohoe slovo', 'jaman soz']
        for slovo in cenzura:
            if slovo in value:
                 raise serializers.ValidationError('Название содержит слова под цензурой')
        return value

class ReplySerializer(postContentSerializer):
    review = ReviewSerializer(read_only=True)
    manager = UserSerializer(read_only=True)


    class Meta(postContentSerializer.Meta):
        model = Reply
        fields = postContentSerializer.Meta.fields + ('review', 'manager')

class ReplyForReviewSerializer(postContentSerializer):
    manager = UserSerializer(read_only=True)


    class Meta(postContentSerializer.Meta):
        model = Reply
        fields = postContentSerializer.Meta.fields + ('manager',)

class ReviewFullSerializer(ReviewSerializer):
    reply = ReplyForReviewSerializer(many= True, read_only=True)
    class Meta(ReviewSerializer.Meta):
        fields = ReviewSerializer.Meta.fields + ('reply',)