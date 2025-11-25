from django.contrib import admin
from .models import Category, Product, ContactInfo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category')
    list_filter = ('category',)  # фильтрация по категории
    search_fields = ('name', 'description')  # поиск по наименованию и описанию


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Запрещаем добавлять более одной записи
        return not ContactInfo.objects.exists()
