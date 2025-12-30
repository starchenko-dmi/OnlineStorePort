from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import ContactForm, ProductForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')