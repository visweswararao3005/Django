from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse(f"<h1>Welcome to Trainer App</h1>")
def task(request):
    return HttpResponse(f"<h1>Trainer Task is completed</h1>")