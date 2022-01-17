from rest_framework import serializers
from . import models


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = models.Article
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        request = self.context.get("request")
        print(request.user)
        print(request.headers)
        if not ((request and hasattr(request, "user")) and not request.user.is_anonymous):
            raise serializers.ValidationError("Authentication error")

        user = request.user
        instance.author = user
        instance.save()
        return instance