from django.urls import path
from src.my_app import views

urlpatterns = [
    path('', views.example_view),
    path('variable/', views.variable_view)
]