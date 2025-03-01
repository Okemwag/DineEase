from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem
from .analytics import get_total_orders, get_daily_orders, get_popular_items


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product_id", "quantity", "price"]
        extra_kwargs = {
            "id": {"read_only": True}
        }


class OrderSerializer(ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "table_id", "status", "created_at", "order_items"]
        extra_kwargs = {
            "id": {"read_only": True}
        }

    def create(self, validated_data):
        order_items = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(order=order, **item)
        return order


    def update(self, instance, validated_data):
        order_items = validated_data.pop("order_items")
        instance.table_id = validated_data.get("table_id", instance.table_id)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        for item in order_items:
            order_item = OrderItem.objects.get(order=instance, product_id=item["product_id"])
            order_item.quantity = item["quantity"]
            order_item.price = item["price"]
            order_item.save()
        return instance


class OrderAnalyticsSerializer(serializers.Serializer):
    total_orders = serializers.IntegerField(read_only=True)
    daily_orders = serializers.IntegerField(read_only=True)
    popular_items = serializers.ListField(read_only=True)

    def to_representation(self, instance):
        return {
            "total_orders": get_total_orders(),
            "daily_orders": get_daily_orders(instance.get("date")),
            "popular_items": get_popular_items()
        }
