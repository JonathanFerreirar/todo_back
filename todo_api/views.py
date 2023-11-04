from .models import Todo
from .serializers import TodoSerializer

from rest_framework import mixins
from rest_framework import generics


class ListTodo(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get (self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post (self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)
    
    
class DetailTodo(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get (self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put (self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete (self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


