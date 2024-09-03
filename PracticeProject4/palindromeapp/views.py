from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse(f'Welcome to Palindrome .!')

def string(request,i):
    str1=i
    l=len(str1)
    for i in range(l):
        if str1[i]==str1[l-1-i]:
            pass
        else:
            return HttpResponse(f'{str1} is not a palindrome')
    return HttpResponse(f'{str1} is a palindrome')
    
def number(request,i):
    a=str(i)
    return string(request,a)
#     num1=str(i)
#     l=len(num1)
#     for i in range(l):
#         if num1[i]==num1[l-1-i]:
#             pass
#         else:
#             return HttpResponse(f'{num1} is not a number palindrome')
#     return HttpResponse(f'{num1} is a number palindrome')