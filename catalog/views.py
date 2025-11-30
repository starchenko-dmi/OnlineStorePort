from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactInfo, Product


def home(request):
    products = Product.objects.all()  # ← получаем все продукты
    print("Products count:", products.count())  # ← временная отладка
    return render(request, 'catalog/home.html', {'products': products})


def contacts(request):
    contact_info = ContactInfo.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(name)
        print(message)
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html', {'contact_info': contact_info})