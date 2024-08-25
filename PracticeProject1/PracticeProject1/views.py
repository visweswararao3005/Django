from django.http import HttpResponse


def home(request):
    return HttpResponse(f"<h1>Welcome to fibbonacci series !</h1>")

def tennumbers_home(request):
    x,y=0,1
    ls=[]
    i=0
    while i<10:
        ls=ls+[x]
        x,y=y,x+y
        i+=1
    return HttpResponse(f"First 10 numbers in fibbonacci series is :{ls} ")
    
def belowhundred_home(request):
    x,y=0,1
    ls=[]
    while(x<100):
        ls=ls+[x]
        x,y=y,x+y
    return HttpResponse(f"Fibbonacci series below 100 is :{ls} ")

def reverseten_home(request):
    x,y=0,1
    ls=[]
    i=0
    while i<10:
        ls=[x]+ls
        x,y=y,x+y
        i+=1
    return HttpResponse(f"First 10 numbers in fibbonacci series is :{ls} ")
    