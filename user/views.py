from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response

User = get_user_model()

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():

            user = serializer.save()

            #refresh = RefreshToken.for_user(user)

            email = serializer.data.get('email')

            return Response({"user": {
                "email": email
            },   #'token': str(refresh.access_token),
                #'refresh': str(refresh)
            })

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)