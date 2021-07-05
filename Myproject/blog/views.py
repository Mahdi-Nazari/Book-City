from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def home(request):
    context = {
        "books" : Book.objects.filter(status = "p").order_by('-publish')
    }
    return render(request, 'blog/home.html', context)

def detail(request, slug):
    context = {
        "book": Book.objects.get(slug = slug)
    }
    return render(request, 'blog/detail.html', context)