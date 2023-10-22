from .models import Todo
from .serializers import TodoSerializer

from rest_framework import generics, status
from rest_framework.response import Response


class GetAllTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request):

        todos = self.get_queryset()
        if not todos:
            return Response({"error": "No todos found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            todo = serializer.data.get('todo')
            create_at = serializer.data.get('create_at')
            updated_at = serializer.data.get('updated_at')

            return Response({
                "data": {
                    "todo": todo,
                    "create_at": create_at,
                    "updated_at": updated_at
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "failed", "details": serializer.errors
            })


class UpdateTodo(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({"message": f"'{instance.todo}' was updated successfully"}, status=status.HTTP_200_OK)


class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def destroy(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        todo = instance.todo

        self.perform_destroy(instance)

        return Response(
            {"message": f" '{todo}' was deleted successfully"}, status=status.HTTP_200_OK
        )
