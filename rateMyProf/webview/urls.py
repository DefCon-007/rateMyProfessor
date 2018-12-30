from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generatePassword', views.sendPassword, name='sendPassword'),
    path('addrating', views.addRating, name="addrating"),
    path('login', views.Userlogin, name='login'),
    path('getrating', views.getRating, name="getrating")

    ]