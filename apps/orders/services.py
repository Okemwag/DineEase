#Service for orders 
import json


import pika
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.utils import timezone


from .exceptions import OrderException
from .models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer
from .utils import get_order_total

params = pika.URLParameters(settings.RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="order", durable=True)


def create_order(customer, items):
    """
    Create an order for a customer
    """
    with transaction.atomic():
        order = Order.objects.create(customer=customer)
        for item in items:
            order_item = OrderItem.objects.create(
                order=order,
                menu_item_id=item["menu_item_id"],
                price=item["price"],
                quantity=item["quantity"],
            )
            order.items.add(order_item)
        order.total_price = get_order_total(order)
        order.save()
        return order


def update_order(order, items):
    """
    Update an order
    """
    with transaction.atomic():
        order.items.all().delete()
        for item in items:
            order_item = OrderItem.objects.create(
                order=order,
                menu_item_id=item["menu_item_id"],
                price=item["price"],
                quantity=item["quantity"],
            )
            order.items.add(order_item)
        order.total_price = get_order_total(order)
        order.save()
        return order


def cancel_order(order):
    """
    Cancel an order
    """
    order.cancelled = True
    order.save()
    return order


def complete_order(order):
    """
    Complete an order
    """
    order.status = Order.OrderStatus.COMPLETED
    order.save()
    return order


def get_order(order_id):
    """
    Get an order by id
    """
    try:
        order = Order.objects.get(order_id=order_id)
        return order
    except ObjectDoesNotExist:
        raise OrderException("Order not found")


def get_orders(customer):
    """
    Get all orders for a customer
    """
    orders = Order.objects.filter(customer=customer)
    return orders
    