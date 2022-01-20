from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def aboutme(request):
    return render(request, 'portfolio/about-me.html')

def projects(request):
    return render(request, 'portfolio/projects.html')