from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'image')

    def validate_title(self, value):
        if ';' in value:
            raise serializers.ValidationError('invalid chars in title')
        return value

class FullEventSerializer(EventSerializer):
    class Meta(EventSerializer.Meta):
        model = Event
        fields = EventSerializer.Meta.fields + ('manager', 'description')



