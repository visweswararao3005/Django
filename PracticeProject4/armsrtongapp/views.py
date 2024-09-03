from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse(f"<h1>Welcome to armstrong number</h1>")

def check(request,i):
    e=len(str(i))
    a=i
    sum=0
    while a>0:
        r=a%10
        sum+=r**e
        a//=10
    if i==sum:
        return HttpResponse(f'{i} is an Armstrong Number')
    else:
        return HttpResponse(f'{i} is not an Armstrong Number')