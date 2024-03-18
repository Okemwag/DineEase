#utils for Order Service

def get_order_total(order):
    """
    Get the total amount of an order
    """
    total = 0
    for item in order.items.all():
        total += item.price * item.quantity
    return total


