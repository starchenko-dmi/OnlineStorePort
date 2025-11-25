from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, our_contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('our_contacts/', our_contacts, name='our_contacts'),
]