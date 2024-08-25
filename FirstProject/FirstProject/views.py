from django.http import HttpResponse


def home(request):
    return HttpResponse(f"Hi this is Visweswararao")

def font_home(request):
    return HttpResponse(f'<h1>I am from Nellore</h1>')


def color_home(request):
    return HttpResponse(f'<h1 style=color:red>I completed my Graduation In 2024</h1>')

def vote_home(request):
    name="Vicky"
    age=23
    if age>18:
        return HttpResponse(f"<h1>{name} is {age} old so he/she is eligible to vote</h1>")
    else:
        return HttpResponse(f"<h1>{name} is {age} old so he/she is not eligible to vote</h1>")
    
def even_home(request):
    l1=[1,5,7,6,9,3,84,3,9,-2,1,48,5,-4,54,15,5,2,4]
    l2=[i for i in l1 if i%2==0 and i>0]
    l3=[i for i in l1 if i%2==1 and i>0]
    return HttpResponse(f"<h1>Original List is :{l1}<br>Even list is : {l2}<br>Odd List is : {l3}</h1>")