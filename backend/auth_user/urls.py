from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('verification/', views.UserEmailVerificationView.as_view(), name='verification'),
]