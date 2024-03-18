#Handle orders placed and enqueue them for processing
from celery import shared_task

from .exceptions import OrderException
from .models import Order
from .services import OrderService


@shared_task
def process_order(order_id):
    try:
        order = Order.objects.get(pk=order_id)
        OrderService.process_order(order)
    except Order.DoesNotExist:
        raise OrderException("Order not found")
    except OrderException as e:
        raise e
    return order_id


