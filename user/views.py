from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import generics, status,mixins
from rest_framework.response import Response

User = get_user_model()

class RegisterUser(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

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
        
# class ListUser(generics.ListCreateAPIView) :
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
    