from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "job"

 
urlpatterns = [
    path('sign_up',views.sign_up, name='sign_up'),
]