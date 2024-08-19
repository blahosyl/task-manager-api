from django.urls import path
from watchers import views

# URLs for the watchers API
urlpatterns = [
    path('watchers/', views.WatcherList.as_view()),
    path('watchers/<int:pk>/', views.WatcherDetail.as_view())
]
