from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "year.html")


def display(request):
    year = int( request.POST['year'] )
    if (year % 400 == 0) and (year % 100 == 0):
        res = f"{year} is a leap year"
    elif (year % 4 == 0) and (year % 100 != 0):
        res = f"{year} is a leap year"
    else:
        res = f"{year} is not a leap year"
    return render(request, "year.html", {"res": res, "year": year})
