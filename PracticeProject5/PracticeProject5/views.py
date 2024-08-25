from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "grade.html")


def display_result(request):
    ope = request.POST['check']
    name = request.POST['name']
    python = int(request.POST['python'])
    java = int(request.POST['java'])
    mysql = int(request.POST['mysql'])
    html = int(request.POST['html'])
    django = int(request.POST['django'])
    if python > 100 or java > 100 or mysql > 100 or html > 100 or django > 100:
        result = "Please Enter Proper Details"
    else:
        if ope == 'Total':
            total_value = python + java + mysql + html + django
            result = f"{name} got {total_value} marks out of 500 "
        elif ope == 'Percentage':
            per_value = int((python + java + mysql + html + django) / 500 * 100)
            result = f'{name} got {per_value}%'
        elif ope == 'Grade':
            per_value = int((python + java + mysql + html + django) / 500 * 100)
            if 90 < per_value:
                grade = 'A'
            elif 80 < per_value <= 90:
                grade = 'B'
            elif 70 < per_value <= 80:
                grade = 'C'
            elif 60 < per_value <= 70:
                grade = 'D'
            elif 50 < per_value <= 60:
                grade = 'E'
            else:
                grade = 'F'
            result = f'{name} got {grade}-Grade'
        elif ope == 'Status':
            per_value = int((python + java + mysql + html + django) / 500 * 100)
            if per_value > 50:
                status = 'Pass'
            else:
                status = 'Fail'
            result = status
        else:
            name = ''
            python = None
            java = None
            mysql = None
            html = None
            django = None
            result = ''

    return render(request, "grade.html", {"name": name, 'python': python, 'java': java, 'mysql': mysql, 'html': html,
                                          'django': django, 'result': result})
