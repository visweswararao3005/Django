from django.http import HttpRequest, HttpResponse


def home(request):
    return HttpResponse(f'<h1>Welcome to project 2 where we use apps also..!</h1>')