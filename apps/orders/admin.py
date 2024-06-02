from django.contrib import admin
from .models import Order
from django.db.models import Count
from django.utils import timezone

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'customer', 'total_items', 'total_price')

    def total_items(self, obj):
        return obj.items.count()

    def total_price(self, obj):
        return obj.total_price

    def get_total_orders(self, request):
        return Order.objects.count()
    get_total_orders.short_description = 'Total Orders'

    def get_daily_orders(self, request):
        today = timezone.now().date()
        return Order.objects.filter(timestamp__date=today).count()
    get_daily_orders.short_description = 'Daily Orders'

    def get_popular_items(self, request):
        return Order.objects.values('items').annotate(num_orders=Count('id')).order_by('-num_orders')[:10]
    get_popular_items.short_description = 'Popular Items'
