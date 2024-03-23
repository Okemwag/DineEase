from django.urls import path
from .views import ReviewViewSet

urlpatterns = [
    path('reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='reviews'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review-detail'),
]


