from django import http
from django.http.response import HttpResponse

def home_view(request):
    return HttpResponse('Home View!')
    