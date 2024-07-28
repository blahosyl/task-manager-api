#3rd party
from rest_framework import serializers
# Project-specific
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Define the task serializer classs
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        """
        Image validation: no larger than 3 MB & no wider/higher than 4096 px
        """
        if value.size > 3 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 3MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Check if the owner of the resource is making the request
        """
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        """
        Specify model & fields
        """
        model = Task
        fields = [
            'id', 'author', 'created_at', 'updated_at', 'title', 'excerpt'
            'description', 'assignee', 'image', 'priority', 'status',
            'due_date', 'is_owner', 'profile_id', 'profile_image',
        ]