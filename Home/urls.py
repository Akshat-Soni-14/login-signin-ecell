from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
       path("", views.index, name='home'),
       path("signup", views.signup, name='signup'),
       path("login", views.loginUser, name='login'),
       path("logout", views.logoutUser, name='logout'),
]