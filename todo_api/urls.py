from django.urls import path
from .views import CreateTodo, DeleteTodo, ListTodo, UpdateTodo, DetailTodo


urlpatterns = [
    # Routers about user auth
    path('todo/', ListTodo.as_view(), name='list_todo'),
    path('todo/<int:pk>', DetailTodo.as_view(), name='detail_todo'),
    path('todo/add/', CreateTodo.as_view(), name='todo_add'),
    path('todo/del/<int:pk>', DeleteTodo.as_view(), name='todo_delete'),
    path('todo/upd/<int:pk>', UpdateTodo.as_view(), name='todo_update'),


]
