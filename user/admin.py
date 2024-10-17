from django.contrib import admin

from user.models import User

# Register your models here.
# admin.site.register(User, CustomUserAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'city', 'country')
    list_filter = ('is_active',)

admin.site.register(User, CustomUserAdmin)