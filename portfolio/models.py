from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()


    def __str__(self):
        return self.username
    pass

