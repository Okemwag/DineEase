from django.db import models


# Create your models here.
class Customer(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Customer'
        db_table = 'customers'
        
    def __str__(self):
        return self.username