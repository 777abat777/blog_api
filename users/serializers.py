from rest_framework import serializers
from blog_api.serializers import CommentSerializer, PostSerializer
from users.models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class userSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    blog_posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = NewUser
        fields = ["id", 'user_name', "blog_posts", "comments", 'about']
