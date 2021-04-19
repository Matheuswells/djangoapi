from django.contrib import admin
from django.urls import path, include
from blog.views import  UsersViewSet
from blog.views import PostViewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'posts', PostViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
