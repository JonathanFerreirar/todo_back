from django.urls import path
from .views import RegisterUser


urlpatterns = [
    
    path('signup/', RegisterUser.as_view(), name='register_user'),
    
  ]
