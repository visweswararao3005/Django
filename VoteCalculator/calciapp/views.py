from django.shortcuts import render


def home(request):
    return render(request, 'calculator.html')


def display_result(request):
    n1 = int(request.POST['a'])
    n2 = int(request.POST['b'])
    operation = request.POST['operation']
    # print(f"{n1},{n2},{operation}")
    if operation == 'Add':
        result = n1 + n2
    elif operation == 'Sub':
        result = n1 - n2
    elif operation == 'Div':
        try:
            result = n1 / n2
        except:
            result = "n2 is 0 please change "
    elif operation == 'Mul':
        result = n1 * n2
    else:
        n1=None
        n2=None
        result =None

    return render(request, 'calculator.html', {'n1': n1, 'n2': n2, 'res': result})
