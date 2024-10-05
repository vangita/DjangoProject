from django.urls import path
from .views import index, about

urlpatterns = [
    path('first/', index, name='index'),
    path('second/', about, name='about'),
]