
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from api_task_manager.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        # count tasks where this user is the assignee
        assigned_count=Count('owner__assignee', distinct=True),
        # count tasks this user is watching
        watched_count=Count('owner__watcher', distinct=True),
        # count tasks this user created
        owned_count=Count('owner__task_owner', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        # all profiles assigned to tasks the selected profile is watching
       'owner__assignee__watched__owner__profile',
   ]

    search_fields = [
        'owner__username',
        'firstname',
        'lastname',
        'role',
        'about',
    ]

    ordering_fields = [
        'assigned_count',
        'watched_count',
        'owned_count',
        'created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        # count tasks where this user is the assignee
        assigned_count=Count('owner__assignee', distinct=True),
        # count tasks this user is watching
        watched_count=Count('owner__watcher', distinct=True),
        # count tasks this user created
        owned_count=Count('owner__task_owner', distinct=True)
    ) 
    serializer_class = ProfileSerializer
