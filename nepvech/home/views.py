from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def service(request):
    return render(request, 'home/service.html')

def book(request):
    return render(request, 'home/book.html')

def contact(request):
    return render(request, 'home/contactus.html')