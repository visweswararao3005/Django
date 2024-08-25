from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'votecheck.html')


def check(request):
    ope = request.POST['operation']
    if ope == 'Submit':
        name = request.POST['name']
        age = int(request.POST['age'])
        if age > 18:
            result = f"{name} is Eligible"
        else:
            result = f"{name} is Eligible"
    else:
        name = ''
        age = None
        result = ''


    return render(request, "votecheck.html", {"name": name, "age": age, "res": result})
