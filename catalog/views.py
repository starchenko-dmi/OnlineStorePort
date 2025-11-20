from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'catalog.html')
