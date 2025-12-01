from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactInfo, Product
from django.core.paginator import Paginator


def home(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 8)  # 8 товаров на страницу (можно изменить)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

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


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)