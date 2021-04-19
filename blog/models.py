from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()

    def __str__(self):
        return self.username
    pass

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.CharField(max_length=1200, blank=False, null=False)
    likes = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title
    pass