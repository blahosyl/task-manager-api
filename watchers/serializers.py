from django.db import IntegrityError
from rest_framework import serializers
from .models import Watcher


class WatcherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Watcher model
    The create method handles the unique constraint on 'owner' and 'watched'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    watched_title = serializers.ReadOnlyField(source='watched.title')

    class Meta:
        model = Watcher
        fields = ['id', 'created_at', 'owner', 'watched', 'watched_title']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })