from .models import Post, Album, Files
from rest_framework import serializers
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Post
        #fields = '__all__'
        fields = ('pk', 'title', 'content', 'author_name')

class AlbumSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source = 'author.username')
    image = serializers.ImageField(use_url=True) #이미지가 잘 올라갔는지 url로 확인
    
    class Meta:
        model = Album
        #fields = '__all__'
        fields = ('pk', 'image', 'content', 'author_name')


class FilesSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source = 'author.username')
    filename = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        #fields = '__all__'
        fields = ('pk', 'filename', 'content', 'author_name')