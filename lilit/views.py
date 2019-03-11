from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'lilit/home.html', {})

def cv(request):
    return render(request, 'lilit/cv.html', {})