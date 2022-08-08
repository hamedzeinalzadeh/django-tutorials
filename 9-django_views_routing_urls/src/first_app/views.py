from ast import arg
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
articles = {
    'sports': 'Sports page',
    'finance': 'Finance page',
    'politics': 'Politics page'
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        #result = 'No page for that topic!'
        #return HttpResponseNotFound(result) --> for debugging
        raise Http404('404 GENERIC ERROR')   #404.html 

# def add_view(request, num1, num2):
#     #domain.com/first_app/num1/num2
#     add_result = num1 + num2
#     result = f"{num1} + {num2} = {add_result}"
#     return HttpResponse(result)    

#domain.com/first_app/0 --> domain.com/first_app/sports
def num_page_view(request, num_page):

    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))