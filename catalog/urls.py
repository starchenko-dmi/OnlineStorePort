from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductDeleteView, ProductUpdateView, \
    ProductCreateView, UnpublishProductView, ProductsByCategoryView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/unpublish/<int:pk>/', UnpublishProductView.as_view(), name='product_unpublish'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
]