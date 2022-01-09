from django.urls import path
from django.urls import include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from . import views



urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]