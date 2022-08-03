from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
articles = {
    'sports': 'Sports page',
    'finance': 'Finance page',
    'politics': 'Politics page'
}

def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    #domain.com/first_app/num1/num2
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(result)    

