from .models import Order
from django.db.models import Count

def get_total_orders():
    return Order.objects.count()

def get_daily_orders(date):
    return Order.objects.filter(timestamp__date=date).count()

def get_popular_items():
    return Order.objects.values('items').annotate(num_orders=Count('id')).order_by('-num_orders')[:10]


