from django.shortcuts import render


def calculate_mccabe(request):
    if request.method == 'GET':
        return render(request, 'calculate_mccabe.html')
    print(request.POST)
    return render(request, 'calculate_mccabe.html')

