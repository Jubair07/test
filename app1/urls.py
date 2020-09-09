from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home page'),
    path('profile',views.profile, name='profile page'),
    path('update',views.update, name='update page'),
    path('expression',views.expression, name='expression value')
]