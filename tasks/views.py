from django.db.models import Count
from rest_framework import permissions, generics, filters
from api_task_manager.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    """
    List tasks or create a task if logged in
    The perform_create method associates the task with the logged in user.
    """
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Task.objects.annotate(
        watchers_count=Count('watched', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'watchers_count',
        'updated_at',
        'due_date',
        'status',
        'priority',
    ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task and edit or delete it if you own it.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.annotate(
        watchers_count=Count('watched', distinct=True),
    )