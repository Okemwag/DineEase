from django.urls import path
from .views import (OrderListCreateView, OrderDetailView, OrderItemDetailView, OrderAnalyticsView)

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<str:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order-items/<str:pk>/', OrderItemDetailView.as_view(), name='order-item-detail'),
    path('order-analytics/', OrderAnalyticsView.as_view(), name='order-analytics'),
]