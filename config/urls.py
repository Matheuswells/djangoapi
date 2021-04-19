from django.contrib import admin
from django.urls import path, include
from blog.views import  UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),


]
