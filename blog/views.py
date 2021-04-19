from rest_framework import viewsets
from blog.models import User 
from blog.models import Post
from blog.serializer import UserSerializer
from blog.serializer import  PostSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewsSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer