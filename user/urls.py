from django.urls import path
from .views import index

urlpatterns = [
    path('first/', index, name='index'),
]