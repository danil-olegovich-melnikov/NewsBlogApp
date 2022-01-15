from django.shortcuts import render
from rest_framework import viewsets

from . import serializers
from . import models

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()