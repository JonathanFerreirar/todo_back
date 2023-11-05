from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", 'password')

        extra_kwargs = {
            'password': {"write_only": True}
        }

    def create(self, validated_data):

        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.create_user(
            email=email,
            password=password
        )

        return user


# class UpdateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("email", "password")
#         extra_kwargs = {
#             'password': {"write_only": True}
#         }

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)

#         password = validated_data.get('password')
#         if password and check_password(password, instance.password):

#             new_password = validated_data.get('new_password')
#             if new_password:
#                 instance.set_password(new_password)

#             instance.save()
#             return instance

#         raise serializers.ValidationError("Wrong password")

