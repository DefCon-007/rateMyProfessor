from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generatePassword', views.sendPassword, name='sendPassword')
    ]