from .models import Todo
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"
        
    def validate_user(self, value):
        try:
            user_obj = User.objects.get(id=value)
            print(user_obj)
            return user_obj
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        
