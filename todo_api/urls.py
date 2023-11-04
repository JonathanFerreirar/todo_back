from django.urls import path
from .views import CreateTodo, DeleteTodo, ListTodo, UpdateTodo


urlpatterns = [
    # Routers about user auth
    path('todo/', ListTodo.as_view(), name='todo'),
    path('todo/add/', CreateTodo.as_view(), name='todo_add'),
    path('todo/del/<int:pk>', DeleteTodo.as_view(), name='todo_delete'),
    path('todo/upd/<int:pk>', UpdateTodo.as_view(), name='todo_update'),


]
