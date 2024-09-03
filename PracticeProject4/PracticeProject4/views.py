from django.http import HttpResponse


def home(request):
    return HttpResponse(f"<h1>Welcome to Practice Progect4 on Django</h1>")

def list_of_apps(request):
    return HttpResponse(f'<h1>1.Armstrong<br>2.Palindrome</h2>')