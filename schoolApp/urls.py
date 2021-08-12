"""schoolApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from admissions.views import main
import finance
from django.contrib import admin
from django.urls import path, include
from admissions.views import main



urlpatterns = [

    #------This url opens when server starts and it will guide you-------------
    path('',main),

    #------ADMIN URLS mapping---------    
    path('admin/', admin.site.urls),

    #------URL mapping for admissions app-------
    path('ad/', include('admissions.urls') ),

    #------URL mapping for finance app---------
    path('fin/', include('finance.urls') ),

]
