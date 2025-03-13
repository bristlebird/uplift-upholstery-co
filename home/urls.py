"""
Urls for the home page app!
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
