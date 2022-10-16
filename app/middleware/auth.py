from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class HomeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response

