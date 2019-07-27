from django.urls import path, include
from website.views import index

urlpatterns = [
    path('', index)
]
