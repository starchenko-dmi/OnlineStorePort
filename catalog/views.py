from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import FormView
from .forms import ContactForm, ProductForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .mixins import OwnerRequiredMixin, ProductDeletePermissionMixin
from .models import ContactInfo, Product, Category
from django.core.paginator import Paginator

from .services import get_products_by_category, get_published_products


class UnpublishProductView(PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'catalog.can_unpublish_product'  # обязательно с app_label!
    template_name = 'products/unpublish_confirm.html'
    fields = []  # не редактируем поля, только действие

    def form_valid(self, form):
        # Отменяем публикацию
        self.object.is_published = False
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_queryset(self):
        return get_published_products()


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


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price', 'is_published']
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # ← автоматически назначаем владельца
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(LoginRequiredMixin, ProductDeletePermissionMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductsByCategoryView(ListView):
    model = Product
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = get_object_or_404(Category, id=category_id)
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'
    paginate_by = 12  # например, 12 категорий на страницу

    def get_queryset(self):
        # Сортируем категории по имени (алфавиту)
        return Category.objects.all().order_by('name')