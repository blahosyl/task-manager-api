from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    Adds 5 extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    assigned_count = serializers.ReadOnlyField()
    watched_count = serializers.ReadOnlyField()
    owned_count = serializers.ReadOnlyField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'firstname', 'lastname',
            'pronouns', 'role', 'about', 'image', 'is_owner', 'assigned_count',
            'watched_count', 'owned_count',
        ]