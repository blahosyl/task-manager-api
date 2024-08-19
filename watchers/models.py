from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task


class Watcher(models.Model):
    """
    Watcher model, related to 'owner' and 'watched'.
    'owner' is a User that is watching a Task.
    'watched' is a Task that is watched by 'owner'.
    'unique_together' makes sure a user can't 'double watch' the same task.
    """
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='watcher'
                              )
    watched = models.ForeignKey(Task,
                                on_delete=models.CASCADE,
                                related_name='watched'
                                )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'watched']

    def __str__(self):
        return f'{self.owner} {self.watched}'
