from django.shortcuts import render

from .models import Like, Blog, Comment
from .serializers import BlogSerializer, LikeSerializer, CommentSerializer

from rest_framework.authentication import  BasicAuthentication, SessionAuthentication, TokenAuthentication

from rest_fremwork import ListAPIView, RetrieveUpdateDestroyAPIView

class BlogViewAll(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]


class CommentViewAll(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]


class LIkeViewAll(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]


class BlogView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]


class CommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]


class LIkeView(RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]