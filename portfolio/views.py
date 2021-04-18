from rest_framework import viewsets
from portfolio.models import User 
from portfolio.serializer import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer