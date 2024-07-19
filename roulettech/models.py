
from django.db import models

# Create your models here.

#Model for User Messages
class Messages(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    message = models.TextField()

    def _str_(self):
        return self.name

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    user_id = models.IntegerField()
    is_used = models.BooleanField(default=False)


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username =  models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     phone = models.CharField(max_length=10, null=True)
#     country = models.CharField(max_length=63)



    