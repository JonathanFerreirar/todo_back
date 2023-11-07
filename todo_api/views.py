from .models import Todo
from .serializers import TodoSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth import authenticate


class ListTodo(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get (self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
    
    def post (self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.create( request, *args, **kwargs)
    
    
class DetailTodo(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get (self, request, pk,*args, **kwargs):
        if request.user.is_authenticated:
            
            todo = Todo.objects.get(id=pk)
            print(todo)
            
            return Response({
                "data": "ok"
            })
            #return self.retrieve(request, *args, **kwargs)
        else:
            return Response({
                "error": "user is not authenticated"
            })
    
    def put (self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.partial_update(request, *args, **kwargs)

    def delete (self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.destroy(request, *args, **kwargs)


