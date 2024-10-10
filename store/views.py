from itertools import product

from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from store.models import Category, Product


# Create your views here.
def index(request):

    return HttpResponse("Hello, world.")

def about(request):

    return HttpResponse("About store")

def get_category(request):
    categories = Category.objects.all()
    json_files = []

    for category in categories:
        json_file = {
            'ID': category.id,
            'name': category.name,
            'description': category.description,
            'slug': category.name,
            'is_active': category.is_active,
            'created_at': category.created_at,
            'updated_at': category.updated_at,
        }
        if category.parent_id:
            parent = Category.objects.get(id=category.parent_id)
            json_file['parent'] = {
                        'parent_name': parent.name,
                        'parent_id': parent.id,
                    }
        else:
            json_file['parent'] = {'parent_name': None,
                        'parent_id': None}

        json_files.append(json_file)
    return JsonResponse(json_files, safe=False)

from django.http import JsonResponse

def get_product(request):
    products = Product.objects.all()
    json_files = []

    for product in products:
        json_file = {
            'ID': product.id,
            'name': product.name,
            'description': product.description,
            'slug': product.slug,
            'image_URL': request.build_absolute_uri(product.image.url) if product.image else None,
            'price': product.price,
            'is_in_stock': product.is_in_stock,
            'created_at': product.created_at,
            'updated_at': product.updated_at,
            'parent_categories': []
        }

        parent_categories = product.category.all()

        for parent_category in parent_categories:
            print(parent_category)
            category_data = {
                'parent_name': parent_category.name,
                'parent_id': parent_category.id
            }
            json_file['parent_categories'].append(category_data)

        json_files.append(json_file)

    return JsonResponse(json_files, safe=False)
