from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Get profile ID, firstname, lastname and profile image of current user
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_fistname = serializers.ReadOnlyField(
        source='profile.fistname')
    profile_lastname = serializers.ReadOnlyField(source='profile.lastname')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', ' profile_fistname', 'profile_lastname', 
            'profile_image'
        )