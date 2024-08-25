from django.shortcuts import render


def home(request):

    x = 10
    y = 20

    numbers = [12, 45, 6, 78, 14, 22, 65, 45, 55]

    names = [[1, 'vicky'], [2, 'ravi'], [3, 'raju'], [4, 'lucky']]

    student_result = {
        'student1': {'python': 20, 'django': 30},
        'student2': {'python': 35, 'django': 34},
        'student3': {'python': 22, 'django': 33},
        'student4': {'python': 23, 'django': 35},
        'student5': {'python': 22, 'django': 23},
    }
    return render(request, "display.html", {"no1": x, 'no2': y, 'numbers': numbers, 'nestednames': names, 'result': student_result})

