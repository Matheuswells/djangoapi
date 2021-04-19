from rest_framework import viewsets
from blog.models import User 
from blog.serializer import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer