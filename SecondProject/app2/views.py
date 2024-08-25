from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse(f"<h1>Welcome to apps2 of django project</h1>")

def second(request):
    return HttpResponse(f"<h1>Welcome to second function in apps2 of django project</h1>")
