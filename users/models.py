from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', null=True, blank=True)
    country = models.CharField(max_length=150, verbose_name='Страна', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
