from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics, views
from . import models
from . import seriliazers


class RegisterView(generics.CreateAPIView):
    """ Takes a set of credentials to register the user """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = seriliazers.RegisterSerializer


class UserEmailVerificationView(views.APIView):
    """
        Takes a set of credentials: username and code to activate the account.
        If the code was wrong then the code is reset and resent again
    """
    serializer_class = seriliazers.UserEmailVerificationSerializer
    model = models.UserEmailVerification

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('user')
            code = serializer.validated_data.get('code')
        else:
            return Response(serializer.errors)

        if not self.model.objects.filter(user=username, code=code).exists():
            self.model.objects.get(user=username).save()
            return Response({'code': 'is not valid, a new code was sent'})

        user = models.User.objects.get(username=username)
        user.is_active = True
        user.save()

        return Response('OK')
