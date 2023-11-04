from django.urls import path
from .views import ListTodo, DetailTodo


urlpatterns = [
    
    path('todo/', ListTodo.as_view(), name='list_todo'),
    path('todo/<int:pk>/', DetailTodo.as_view(), name='detail_todo'),
  ]
