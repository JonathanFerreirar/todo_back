from .models import Todo
from .serializers import TodoSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework import permissions, exceptions

from user.models import User


class isOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            if request.data['user'] == request.user.id:
                return True

            raise exceptions.PermissionDenied(detail='request not allowed')
        return True


class IsOnwerUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user.id == request.user.id:
            return True

        raise exceptions.NotFound(detail="Not found", code=404)


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [isOwner]

    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(user=user.id)

        return queryset

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOnwerUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
