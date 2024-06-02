from rest_framework import generics, permissions, status
from .serializers import  MenuItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MenuItem

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class MenuItemSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.query_params.get("query")
        menu_items = MenuItem.objects.filter(name__icontains=query)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
