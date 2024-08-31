from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Slideshow,Service

# Create your views here.

def home(request):
    slideshows=Slideshow.objects.all();
    return render(request, 'index.html',{'slides':slideshows})

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request, 'contact.html')


def team(request):
    return render(request, 'team.html')


def expertise(request):
    return render(request,'services.html')


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html', {'service': service})

def services_list(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})
