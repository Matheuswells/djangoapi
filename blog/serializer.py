from rest_framework import serializers
from blog.models import User
from blog.models import Post
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'name', 'last_name', 'birthday']
    pass
class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ['id', 'title', 'content', 'likes']
    pass
