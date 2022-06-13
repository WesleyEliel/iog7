from django.shortcuts import render

from core.models import Surfer


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_from_request(request):
    surfer_ip = get_client_ip(request=request)
    try:
        return Surfer.objects.get(ip_address=surfer_ip)
    except Exception as exc:
        print(exc)
        return None

"""
def handle_404(request):
    return render(request, "errors/404.html", locals())

"""

def handle_404(request):
    context = {}
    return render(request, 'errors/404.html', context, status=404)

def handle_500(request):
    context = {}
    return render(request, 'errors/500.html', context, status=500)

def handle_400(request):
    context = {}
    return render(request, 'errors/400.html', context, status=400)

def handle_403(request):
    context = {}
    return render(request, 'errors/403.html', context, status=403)