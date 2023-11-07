from django.urls import path
from .views import RegisterUser

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    
    path('signup/', RegisterUser.as_view(), name='register_user'),
    path('login/', TokenObtainPairView.as_view(), name='register_user'),
    path('login/refresh/', TokenRefreshView.as_view(), name='register_user'),
    
    
  ]
