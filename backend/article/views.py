from rest_framework import viewsets

from . import models
from . import serializers


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()

    def create(self, request, *args, **kwargs):
        """
            Takes an article credentials to create one
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            Takes an id to get specific article
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
            Takes an id and credentials to update the article
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
            Takes an id and credentials to update the article
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
            Takes an id of article to and delete it
        """
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
            List of all articles with pagination of 12 articles per page
        """
        return super().list(self, request, *args, **kwargs)
