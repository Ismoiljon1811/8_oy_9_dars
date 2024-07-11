from rest_framework import serializers
from .models import Like, Comment, Blog


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        media = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        media = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        media = Blog
        fields = '__all__'