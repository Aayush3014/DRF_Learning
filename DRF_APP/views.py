from django.http import HttpResponse

# Create your views here.


def index(request):
    """Index Page"""
    return HttpResponse("Hello World")