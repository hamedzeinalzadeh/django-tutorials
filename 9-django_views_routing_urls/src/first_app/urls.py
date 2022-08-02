from django.urls import path
from src.first_app import views

# domain.com/first_app/ 
url_patterns = [
    path('', views.simple_view)
]