import uuid

#from django.utils import timezone
from django.db import models

from apps.accounts.models import Customer
from apps.menu.models import MenuItem
from django_tenants.model import TenantMixin


class Order(models.Model):
    
    class OrderStatus(models.TextChoices):
        PENDING = 'pending'
        PROCESSING = 'processing'
        COMPLETED = 'completed'
        CANCELLED = 'cancelled'
    
    
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    cancelled = models.BooleanField(default=False)
    status = models.CharField(max_length=20, 
                              choices=OrderStatus.choices,
                              default=OrderStatus.PENDING)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Orders'
        db_table = 'orders'
        index_together = ['customer', 'created']

    def __str__(self):
        return f"Order by {self.customer.username} on {self.created}"
    
    
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
     
    
    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} in {self.order}"
    
    
    def get_total_item_price(self):
        return self.quantity * self.menu_item.price
    
