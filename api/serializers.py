from django.contrib.auth.models import User, Group
from rest_framework import serializers
from news.models import Article, Author,ArticleImages



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name','last_name', 'email',)

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Author
        fields = ('user','about',)



class ArticleSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    class Meta:
        model = Article
        fields = ('url', 'title','content')


class ArticleImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImages
        fields = ('image',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    get_images = ArticleImagesSerializer(many=True)
    class Meta:
        model = Article
        fields = ('title','content','status','home_page_status','date','author','get_images',)