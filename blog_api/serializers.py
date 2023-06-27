from rest_framework import serializers
from blog.models import Post, Comment
from django.conf import settings


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.user_name')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner',  'post', 'created', 'image', "author"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", 'image', "title", "author", "excerpt",
                  "content", "status", "slug", "category", "comments", "published"]


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
