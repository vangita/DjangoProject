from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
