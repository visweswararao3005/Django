from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(f"<h1>Welcome to thrid Django Project ..!</h1>")

def templates(request):
    return render(request,'index.html')

def table(request):
    return render(request,'forms.html')

def display_Data(request):
    name = request.GET["txtname"]
    age = request.GET["txtage"]
    email = request.GET["txtemail"]
    mobile = request.GET["txtnumber"]
    place = request.GET["txtplace"]
    # return HttpResponse(f"<h1>Hi my self {name}<br>"
    #                     f"my age is {age}<br>"
    #                     f"my Email ID is {email}<br>"
    #                     f"my mobile number is {mobile}<br>"
    #                     f"my Birth Place is {place}</h1>")
    return render(request,'display.html',{'name':name,'age':age,'email':email,'mobile':mobile,'place':place})