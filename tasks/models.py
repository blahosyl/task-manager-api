from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Task model, related to 'owner' and 'assignee' both User instances
    All fields are optional except 'title'
    """
    PRIORITY_OPTIONS = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),

    ]

    STATUS_OPTIONS = [
        ('TO-DO', 'To do'),
        ('IN-PROGRESS', 'In progress'),
        ('DONE', 'Done'),
    ]

    owner = models.ForeignKey(User, blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              related_name='task_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=1000, blank=True,)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(User, blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='assignee')
    image = models.ImageField(
        upload_to='images/', blank=True, null=True
    )
    priority = models.CharField(max_length=255,
                                choices=PRIORITY_OPTIONS,
                                default='LOW')
    status = models.CharField(max_length=255,
                              choices=STATUS_OPTIONS,
                              default='TO-DO')
    # change from DateTimeField to Date Field suggested by tutor Thomas
    due_date = models.DateField(blank=True, null=True)

    # list tasks from most to least recently created
    class Meta:
        ordering = ['-created_at']

    # show task id & title
    def __str__(self):
        return f'{self.id} {self.title}'
