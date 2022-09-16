from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    Location = models.CharField(max_length=100)
    city = models.CharField(max_length=20)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name