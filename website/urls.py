from django.urls import path, include
from website.views import index, login,ideias, lista

urlpatterns = [
    path('', index),
    path('login', login),
    path('ideias', ideias),
    path('lista', lista)
]
