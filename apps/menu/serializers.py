from rest_framework import serializers

from .models import  MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    image = serializers.ImageField(required=False)
    menu = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())
    
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'menu']
        exclude = ['id']