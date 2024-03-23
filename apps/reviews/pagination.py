from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ReviewPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })
    
    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'next': {'type': 'string', 'nullable': True},
                'previous': {'type': 'string', 'nullable': True},
                'count': {'type': 'integer'},
                'results': schema,
            }
        }
    
    def get_paginated_response_schema_ref(self, schema):
        return {
            'type': 'object',
            'properties': {
                'next': {'type': 'string', 'nullable': True},
                'previous': {'type': 'string', 'nullable': True},
                'count': {'type': 'integer'},
                'results': {'$ref': schema},
            }
        }
    