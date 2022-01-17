from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import generics
from . import seriliazers


class RegisterView(generics.CreateAPIView):
    """
        Takes a set of credentials to register the user
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = seriliazers.RegisterSerializer