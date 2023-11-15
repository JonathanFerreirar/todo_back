from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "email", 'password', 'photo', 'name')

        extra_kwargs = {
            'password': {"write_only": True}
        }

    def create(self, validated_data):

        email = validated_data.get('email')
        password = validated_data.get('password')
        photo = validated_data.get('photo')
        name = validated_data.get('name')

        user = User.objects.create_user(
            email=email,
            password=password,
            photo=photo,
            name=name
        )

        return user
    

class GoogleSerializer(serializers.Serializer):
    id_token = serializers.CharField()
    


