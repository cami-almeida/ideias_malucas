from django.urls import path, include
from website.views import index, login,ideias, lista, remover_ideia

urlpatterns = [
    path('', index),
    path('login', login),
    path('ideias', ideias),
    path('lista', lista),
    path('remover_ideia/<int:id>', remover_ideia)
]
