# views.py

from django.core.cache import cache
from django.http import JsonResponse


def cache_stats(request):
    cache_info = cache.get_stats()
    return JsonResponse(cache_info, safe=False)
