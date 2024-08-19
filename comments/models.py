from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task


class Comment(models.Model):
    """
    Comment model, related to User and Task
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

# show comment body, task title & comment owner in the admin panel
    def __str__(self):
        return f'"{self.content}" on: {self.task} by: {self.owner}'
