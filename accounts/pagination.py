from rest_framework.pagination import PageNumberPagination

class PaginationNumber(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    max_page_size = 20
    page_size_query_param = "max_page"