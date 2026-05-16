from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    # This grabs the actual username instead of just outputting the user's ID number
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    # Grabbing the readable username
    author = serializers.ReadOnlyField(source='author.username')

    # Beauty of the One-to-Many relationship!
    # It nests all comments related to this post directly inside the post's JSON.
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        # We explicitly list the fields we want the API to expose to the frontend
        fields = ['id', 'title', 'slug', 'author', 'content', 'created_at', 'comments']