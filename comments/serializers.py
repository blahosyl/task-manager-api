from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds 8 extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_firstname = serializers.ReadOnlyField(
            source='owner.profile.firstname')
    owner_lastname = serializers.ReadOnlyField(source='owner.profile.lastname')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Show created_at field as "x hours ago"
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Show updated_at field as "x hours ago"
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'owner_firstname', 'owner_lastname',
            'profile_id', 'profile_image',
            'task', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Task is a read only field so that we dont have to set it on each update
    """
    task = serializers.ReadOnlyField(source='task.id')
