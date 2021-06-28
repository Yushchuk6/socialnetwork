from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'post_date', 'likes']

