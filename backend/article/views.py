from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
import django_filters.rest_framework

from django.utils.decorators import method_decorator
from rest_framework.response import Response
from . import models
from . import serializers


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['author']

    def create(self, request, *args, **kwargs):
        """ Takes an article credentials to create one """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """ Takes an id to get specific article """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """ Takes an id and credentials to update the article """
        if not request.user.is_authenticated:
            return Response({'error': 'Please Authenticate to continue'}, status=401)

        user = request.user
        pk = kwargs.get("pk")

        if not models.Article.objects.filter(id=pk).exists():
            return Response({'error': 'Article is not found'}, status=404)

        article = models.Article.objects.get(pk=kwargs.get("pk"))

        if article.author == user or (user.is_active and user.is_superuser):
            return super().update(request, *args, **kwargs)
        return Response({'error': 'Not enough rights to delete the article'}, status=403)

    def partial_update(self, request, *args, **kwargs):
        """ Takes an id and credentials to update the article """
        if not request.user.is_authenticated:
            return Response({'error': 'Please Authenticate to continue'}, status=401)

        user = request.user
        pk = kwargs.get("pk")

        if not models.Article.objects.filter(id=pk).exists():
            return Response({'error': 'Article is not found'}, status=404)

        article = models.Article.objects.get(pk=kwargs.get("pk"))

        if article.author == user or (user.is_active and user.is_superuser):
            return super().partial_update(request, *args, **kwargs)
        return Response({'error': 'Not enough rights to delete the article'}, status=403)

    def destroy(self, request, *args, **kwargs):
        """ Takes an id of article to and delete it """
        if not request.user.is_authenticated:
            return Response({'error': 'Please Authenticate to continue'}, status=401)

        user = request.user
        pk = kwargs.get("pk")

        if not models.Article.objects.filter(id=pk).exists():
            return Response({'error': 'Article is not found'}, status=404)

        article = models.Article.objects.get(pk=kwargs.get("pk"))

        if article.author == user or (user.is_active and user.is_superuser):
            return super().destroy(request, *args, **kwargs)
        return Response({'error': 'Not enough rights to delete the article'}, status=403)

    def list(self, request, *args, **kwargs):
        """ List of all articles with pagination of 12 articles per page """
        return super().list(self, request, *args, **kwargs)
