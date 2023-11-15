from django.contrib.auth import get_user_model
from .serializers import UserSerializer, GoogleSerializer
from rest_framework import generics, status, mixins
from rest_framework.response import Response

from google.oauth2 import id_token
from google.auth.transport import requests

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class GoogleLogin(generics.GenericAPIView):
    serializer_class = GoogleSerializer
    queryset = User
    
    def post(self, request, *args, **kwargs):
        
        try:
            googleRequest = requests.Request()

            token = request.data['id_token']
            
            

            id_info = id_token.verify_oauth2_token(
                token, googleRequest, 'my.app.account')

            name = id_info['name']
            email = id_info['email']
            photo = id_info['picture']
            
            exist = User.objects.filter(
                email=email
            ).exists()
            
            if not exist:
                created_user = User.objects.create(
                    name=name,
                    email=email, 
                    photo=photo
                )
                token = RefreshToken.for_user(user=created_user)
                
                
                return Response(
                    {
                            'token': str(token.access_token),
                            'refresh': str(token)
                    }, status=status.HTTP_201_CREATED
                )
        
            
            else:
                user = User.objects.get(email=email)
                token = RefreshToken.for_user(user=user)
  
                return Response(
                    {
                        'token': str(token.access_token),
                        'refresh': str(token)
                    }, status=status.HTTP_200_OK
                )
        except:
            return  Response({
            "error": "inválid token"
        }, status=status.HTTP_400_BAD_REQUEST)    


class RegisterUser(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            email = serializer.data.get('email')

            return Response({"user":
                             serializer.validated_data,
                             'token': str(refresh.access_token),
                             'refresh': str(refresh)
                             })

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ListUser(generics.ListCreateAPIView) :
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
