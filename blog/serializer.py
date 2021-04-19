from rest_framework import serializers
from blog.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'name', 'last_name', 'birthday']