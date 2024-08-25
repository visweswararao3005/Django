from django.shortcuts import render


# Create your views here.
def home(request):
    x = 10
    y = 4
    z = 6
    list1=[45,2,69,78,23,52,22,48,12,54,55]
    return render(request, 'index.html', {'x1': x, 'x2': y, 'x3': z, 'elements':list1})
