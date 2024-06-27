from django.shortcuts import render

# Create your views here.

from .models import *

def index (request):

    context ={
        'book': Book.objects.all(),
        'category': Category.objects.all(),
    }

    return render(request, 'pages\index.html', context)


def book(request):

    return render(request, r'pages\books.html')


def update (request):

    return render(request, r'pages\update.html')


def delete (request):

    return render(request, r'pages\delete.html')
