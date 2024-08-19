from django.contrib import admin
from .models import Comment

# manage comments in the admin panel
admin.site.register(Comment)
