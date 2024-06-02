from django.urls import path
from .views import (MenuItemListCreateView, MenuItemDetailView,
                    MenuItemSearchView)

urlpatterns = [
    path('menu/', MenuItemListCreateView.as_view(), name='menu-list-create'),
    path('menu/<str:pk>/', MenuItemDetailView.as_view(), name='menu-detail'),
    path('menu/search/', MenuItemSearchView.as_view(), name='menu-search'),
]