from rest_framework import pagination
class MyPagination(pagination.PageNumberPagination):
    page_size = 99999999999
    page_size_query_param = 'count'
    max_page_size = 999999999999999