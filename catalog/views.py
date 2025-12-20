from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from .models import ContactInfo
from .forms import ContactForm

from .models import ContactInfo, Product
from django.core.paginator import Paginator

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ContactsView(FormView):
    template_name = 'catalog/contacts.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        print(f"Имя: {name}\nТелефон: {phone}\nСообщение: {message}")

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

