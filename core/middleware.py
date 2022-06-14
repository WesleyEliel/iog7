from .models import Surfer
from django.shortcuts import render

from .utils.utils import get_client_ip


class BanSurferMiddleware:
    """Users Management"""

    def __init__(self, get_response):
        if get_response is None:
            raise ValueError('get_response must be provided.')
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = self.get_response(request)
        if not request.path.split('/')[1] == "admin":
            surfer_ip = get_client_ip(request=request)
            surfer, created = Surfer.objects.get_or_create(ip_address=surfer_ip)

            if not created:
                if Surfer.objects.all().filter(is_banned=True, ip_address=surfer_ip):
                    return render(request, 'errors/ban.html')
        return response
