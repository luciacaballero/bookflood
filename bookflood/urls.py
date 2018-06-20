from django.contrib import admin
from django.urls import path
from bookflood.views import home

urlpatterns = [
    path('', home),
]
