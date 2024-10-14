from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Min, Max, Avg, F,Count, Q ,  DecimalField
from store.models import Category, Product
from django.db.models.functions import Cast


# Create your views here.
def index(request):
     return HttpResponse("Hello, world.")

def category_list_view(request):
    categories = Category.objects.filter(parent=None)
    for category in categories:
        category.product_count = Product.objects.filter(
            Q(category=category) | Q(category__parent=category)
        ).distinct().count()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)



def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id, is_active=True)
    products = Product.objects.filter(
        Q(category=category) | Q(category__parent=category)
    ).distinct()

    products_with_values = products.annotate(
        total_value=F('price') * F('quantity')
    )

    stats = products_with_values.aggregate(
        highest_price=Max('price'),
        lowest_price=Min('price'),
        average_price=Avg('price'),
        total_stock_value=Sum(Cast(F('total_value'), output_field=DecimalField()))
    )

    context = {
        'category': category,
        'products': products_with_values,
        'stats': stats,
    }
    return render(request, 'category_products.html', context)

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)



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
