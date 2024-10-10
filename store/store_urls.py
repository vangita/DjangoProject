from django.urls import path
from .views import index, about, get_category, get_product

urlpatterns = [
    path('first/', index, name='index'),
    path('second/', about, name='about'),
    path('categories/', get_category, name='get_category'),
    path('products/', get_product, name='get_product'),
]