from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer, ArticleSerializer,ArticleDetailSerializer
from news.models import Article
# Create your views here.


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BrandDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NewsList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer