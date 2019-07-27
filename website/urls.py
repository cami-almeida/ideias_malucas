from django.urls import path, include
from website.views import index, login

urlpatterns = [
    path('', index),
    path('login', login)
]
