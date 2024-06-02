from django.contrib import admin
from .models import MenuItem
# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category', )
    search_fields = ('name', 'description')
    ordering = ('category', 'name')
    fieldsets = (
        (None, {'fields': ('name', 'description', 'price', 'category', 'image')}),
        
    )
    

