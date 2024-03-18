from django.db import models
from django_tenants.models import DomainMixin, TenantMixin

# Create your models here.

class MenuItem(TenantMixin):
    name = models.CharField(max_length=255, primary_key=True,
                            db_index=True,
                            blank=False,
                            null=False)
    category = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True,
                              blank=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Menu Items'
        db_table = 'menu_items'
        index_together = ['name', 'category']

    def __str__(self):
        return self.name
    
    @property
    def price_in_dollars(self):
        return self.price / 144.00