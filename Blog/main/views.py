from django.shortcuts import render
from .models import *


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    data={
        'blog':Maqola.objects.all()
    }
    return render(request, 'blog.html',data)

def maqola(request,son):
    data={
        'data':Maqola.objects.get(id=son)
    }
    return render(request, 'maqola.html',data)
