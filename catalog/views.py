from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import ContactInfo


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(name)
        print(message)
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


def our_contacts(request):
    contact_info = ContactInfo.objects.first()  # Получаем первую (и единственную) запись
    return render(request, 'catalog/contacts.html', {'contact_info': contact_info})
