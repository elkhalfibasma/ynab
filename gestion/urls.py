"""
URL configuration for YNAB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('login/', login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

   
    path('budgetisation',budgetisation, name='budgetisation'),
   
    path('register',views.register, name='inscription'),
    path('info',info, name='informations'),
    
    
    
   
]
