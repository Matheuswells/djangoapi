from django.contrib import admin
from blog.models import User
from blog.models import Post
class Users(admin.ModelAdmin):
    list_display = ('id','username', 'name', 'last_name', 'birthday')
    list_display_links = ('id', 'username')
    pass

class Posts(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'likes')
    list_display = ('id', 'title')
    pass

admin.site.register(User, Users)
admin.site.register(Post, Posts)
