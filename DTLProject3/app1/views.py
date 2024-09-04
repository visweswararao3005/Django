from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html')


def display(request):
    return render(request, 'display.html')


def update(request):
    return render(request, 'update.html')


def add(request):
    return render(request, 'add.html')
