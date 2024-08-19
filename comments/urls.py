from django.urls import path
from comments import views

# URLs for the comment API
urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view())
]
