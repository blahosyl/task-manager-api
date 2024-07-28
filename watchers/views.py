from rest_framework import generics, permissions
from api_task_manager.permissions import IsOwnerOrReadOnly
from .models import Watcher
from .serializers import WatcherSerializer


class WatcherList(generics.ListCreateAPIView):
    """
    List watch instances or watch a task if logged in.
    """
    serializer_class = WatcherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Watcher.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WatcherDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a watch instance, or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WatcherSerializer
    queryset = Watcher.objects.all()