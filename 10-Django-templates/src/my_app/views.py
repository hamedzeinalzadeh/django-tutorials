from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/template/my_app/example.html
    return render(request, 'my_app/example.html')