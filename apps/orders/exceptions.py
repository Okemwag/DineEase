from rest_framework.exceptions import APIException
from django.core.validators import EmailValidator


class OrderException(APIException):
    status_code = 400
    default_detail = "Order Exception"
    default_code = "order_exception"

class OrderItemException(APIException):
    status_code = 400
    default_detail = "Order Item Exception"
    default_code = "order_item_exception"

class OrderItemNotFoundException(APIException):
    status_code = 404
    default_detail = "Order Item Not Found"
    default_code = "order_item_not_found"


class OrderNotFoundException(APIException):
    status_code = 404
    default_detail = "Order Not Found"
    default_code = "order_not_found"

class OrderAlreadyCompletedException(APIException):
    status_code = 400
    default_detail = "Order Already Completed"
    default_code = "order_already_completed"
