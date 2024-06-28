from django.shortcuts import render

# Create your views here.

from .models import *

from .forms import BookForm

def index (request):


    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        add_book.save()
        if add_book.is_valid():
            add_book.save()



    context ={
        'book': Book.objects.all(),
        'category': Category.objects.all(),
        'form': BookForm()
    }

    return render(request, 'pages\index.html', context)


def book(request):
    context ={
        'book': Book.objects.all(),
        'category': Category.objects.all(),
    }


    return render(request, r'pages\books.html', context)


def update (request):

    return render(request, r'pages\update.html')


def delete (request):

    return render(request, r'pages\delete.html')
