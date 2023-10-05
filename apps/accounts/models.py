from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    