from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# 自定義分頁器
class PageNum(PageNumberPagination):
    page_size_query_param = 'pagesize'
    max_page_size = 10

    #指定返回方法
    def get_paginated_response(self, data):
        return Response({
            "counts": self.page.paginator.count,
            "lists": data,
            "page": self.page.number,
            "pages": self.page.paginator.num_pages,
            "pagesize": self.max_page_size,
        })
