from django.urls import path, include
from website.views import index, login,ideias

urlpatterns = [
    path('', index),
    path('login', login),
    path('ideias', ideias)
]
