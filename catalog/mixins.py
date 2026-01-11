from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin


class OwnerRequiredMixin:
    """Разрешает доступ только владельцу объекта"""
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")
        return obj


class ProductDeletePermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        # Владелец может удалять
        if product.owner == request.user:
            return super().dispatch(request, *args, **kwargs)
        # Модератор (с правом delete_product) — тоже может
        if request.user.has_perm('catalog.delete_product'):
            return super().dispatch(request, *args, **kwargs)
        # Иначе — отказ
        raise PermissionDenied("У вас нет прав на удаление этого продукта.")