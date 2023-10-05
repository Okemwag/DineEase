from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
#from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
