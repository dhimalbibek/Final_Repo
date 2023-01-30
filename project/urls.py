"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.models import Infoss
from app.views import homePage
from app.views import form_page, update_form, read, delete_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    path('create/', form_page),
    path('read/<int:id>/', read, name = 'read'),
    path('update/<int:id>/', update_form, name='update'),
    path('delete/<int:id>/', delete_page, name= 'delete')
]
