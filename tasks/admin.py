from django.contrib import admin
from .models import Task

# manage tasks in the admin panel
admin.site.register(Task)
