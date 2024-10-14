from django.urls import path
from .views import index, about, get_category, get_product, category_list_view, category_products_view, \
    product_detail_view

urlpatterns = [
    path('first/', index , name='index'),
    path('second/', about, name='about'),
    path('categories/', get_category, name='get_category'),
    path('products/', get_product, name='get_product'),
    path('category/', category_list_view, name='category_list'),
    path('category/<int:category_id>/products/', category_products_view, name='category_products'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),

]