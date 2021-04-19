from django.contrib import admin
from blog.models import User

class Users(admin.ModelAdmin):
    list_display = ('id','username', 'name', 'last_name', 'birthday')
    list_display_links = ('id', 'username')
    pass

admin.site.register(User, Users)
