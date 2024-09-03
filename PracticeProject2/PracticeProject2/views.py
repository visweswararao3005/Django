from django.http import HttpResponse

def home(request):
    return HttpResponse(f'<h1>Welcome to Prime numbers</h1>')

def prime_home(request):
    num=25
    isPrime=True
    for i in range(2,num):
        if num%i==0:
            isPrime=False
    if isPrime:
        return HttpResponse(f"<h1>{num} is a prime nummber</h1>")
    else:
        return HttpResponse(f"<h1>{num} is not a prime nummber</h1>")
        
def primebelow100_home(request):
    ls=[]
    for i in range(2,101):
        isPrime=True
        for j in range(2,int(i**0.5) + 1):
            if i%j==0:
                isPrime=False
        if isPrime:
            ls=ls+[i]
    return HttpResponse(f'Prime numbers below 100 : {ls}')
def reverseprimebelow100_home(request):
    ls=[]
    for i in range(2,101):
        isPrime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                isPrime=False
        if isPrime:
            ls=[i]+ls
    return HttpResponse(f'Prime numbers below 100 : {ls}')