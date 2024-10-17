from django.contrib import admin

from store.models import Category, Product

# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity', 'description')
    list_filter = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')
    list_filter = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin,)