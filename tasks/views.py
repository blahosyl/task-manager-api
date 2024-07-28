from rest_framework import permissions, generics
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
    queryset = Task.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task and edit or delete it if you own it.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all().order_by('-created_at')
