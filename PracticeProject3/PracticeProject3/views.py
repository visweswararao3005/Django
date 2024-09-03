from django.http import HttpResponse


def home(request):
    return HttpResponse(f"<h1>Welcome to Practice Progect3 on Django</h1>")