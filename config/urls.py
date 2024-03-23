from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from config.views import cache_stats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cache/', cache_page(60 * 15)(cache_stats), name='cache_stats'),
    path('api/', include('apps.reviews.urls')),

]
