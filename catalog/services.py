from .models import Product
from django.core.cache import cache


def get_products_by_category(category_id):
    """
    Возвращает QuerySet всех опубликованных продуктов в указанной категории.
    """
    return Product.objects.filter(
        category_id=category_id,
        is_published=True
    ).select_related('category')


def get_published_products():
    cache_key = 'published_products_list'
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(is_published=True).select_related('category'))
        cache.set(cache_key, products, timeout=900)
    return products