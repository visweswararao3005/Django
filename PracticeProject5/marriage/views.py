from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'marriage.html')


def display():
    return None