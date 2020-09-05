from django.shortcuts import render
from .models import Photos,Videos

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'home.html',{})

def photo(request):
    pics = Photos.objects.all()
    return render(request, 'photos.html', {'pics':pics})

def video(request):
    videos = Videos.objects.all()
    return render(request, 'videos.html', {'videos':videos})
