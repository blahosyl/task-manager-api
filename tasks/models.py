from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Task model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
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
                                    on_delete=models.SET_NULL)
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
        upload_to='images/', default='../default_post_w2n3ng', blank=True
    )
    priority = models.CharField(max_length=255,
                                choices=PRIORITY_OPTIONS,
                                default='LOW')
    status = models.CharField(max_length=255,
                                 choices=STATUS_OPTIONS,
                                 default='TO-DO')
    due_date = models.DateField(blank=True, null=True)


    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.id} {self.title}'