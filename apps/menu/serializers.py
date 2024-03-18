from rest_framework import serializers

from .models import Menu, MenuItem


class MenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    items = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Menu
        fields = ['name', 'description', 'items']
        read_only_fields = ['items']
        exclude = ['id']