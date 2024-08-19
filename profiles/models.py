from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    firstname = models.TextField(max_length=255, blank=True)
    lastname = models.TextField(max_length=255, blank=True)
    pronouns = models.TextField(max_length=255, blank=True)
    role = models.TextField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_bfkzff'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

# automatically create profile model every time a user is created


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
